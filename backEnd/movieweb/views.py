# views.py
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

# 유저 커스텀

from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer






# 챗봇 만들기

import json
import os
import openai
from dotenv import load_dotenv



# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 불러오기
openai.api_key = os.getenv('OPENAI_API_KEY')

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import json
import openai
import logging

logger = logging.getLogger(__name__)

class GPTChatView(APIView):
    permission_classes = [IsAuthenticated]

    def handle_no_permission(self):
        return Response({'response': '로그인 해주세요.'}, status=403)

    def post(self, request):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        try:
            data = json.loads(request.body)
            user_message = data.get('message')

            if user_message:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=150
                )
                return Response({'response': response.choices[0].message['content'].strip()})
            else:
                return Response({'error': 'No message provided'}, status=400)
        except json.JSONDecodeError as e:
            logger.error(f"JSONDecodeError: {e}")
            return Response({'error': 'Invalid JSON'}, status=400)
        except openai.error.InvalidRequestError as e:
            logger.error(f"InvalidRequestError: {e}")
            return Response({'error': str(e)}, status=400)
        except Exception as e:
            logger.error(f"Exception: {e}")
            return Response({'error': str(e)}, status=500)

    def get(self, request):
        return Response({'error': 'Invalid request method'}, status=405)





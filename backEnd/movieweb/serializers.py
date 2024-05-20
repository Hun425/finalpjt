from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['age'] = self.validated_data.get('age', '')
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', '')
        user.save()
        return user

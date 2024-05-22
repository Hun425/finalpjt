# hangul_utils.py
HANGUL_BEGIN_UNICODE = 44032
HANGUL_END_UNICODE = 55203
HANGUL_BASE = 588
CHOSUNG = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

def is_hangul_char(c):
    return HANGUL_BEGIN_UNICODE <= ord(c) <= HANGUL_END_UNICODE

def get_chosung(char):
    if is_hangul_char(char):
        return CHOSUNG[(ord(char) - HANGUL_BEGIN_UNICODE) // HANGUL_BASE]
    return char

def get_chosung_string(string):
    return ''.join(get_chosung(c) for c in string)

def chosungIncludes(source, target):
    source_chosung = get_chosung_string(source)
    target_chosung = get_chosung_string(target)
    return target_chosung in source_chosung

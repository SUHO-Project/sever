import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기)
def listen(recognizer):
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    # Google Web Speech API를 사용하여 음성 인식
    try:
        text =  recognizer.recognize_google(audio, language='ko-KR')
        print("[사용자] " + text)
        return text
    except sr.UnknownValueError:
         speak("다시 말씀해 주세요.")
         listen(recognizer)
    except sr.RequestError as e:
         print("요청 실패 : {0}".format(e)) 
         
# 소리내어 읽기(TTS)
def speak(text):
    if not text:  # text가 비어있으면 오류 방지
        print("오류: 출력할 텍스트가 없습니다.")
        return
    print('[키오스크]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    
    playsound(file_name)
    if os.path.exists(file_name):  # voice.mp3 파일 삭제
        os.remove(file_name)


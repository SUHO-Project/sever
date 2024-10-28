import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        text = text.strip()  # 앞뒤 공백 제거
        print('[사용자]' + text)
        answer(text)
    except sr.UnknownValueError:
        print("인식 실패")  # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print("요청 실패 : {0}".format(e))  # API Key 오류, 네트워크 단절 등

# 대답 카페
def answer(input_text):
    answer_text = ''
    drink_list = ['아메리카노', '바닐라라떼', '카페라떼', '카라멜마끼아또', '카페모카', '카푸치노', '플레인요거트스무디', 
                  '딸기요거트스무디', '망고요거트스무디', '쿠키프라페', '초코프라페', '민트프라페', '레몬에이드', 
                  '블루레몬에이드', '자몽에이드', '청포도에이드', '딸기라떼', '딸기주스', '녹차', '얼그레이', 
                  '캐모마일', '복숭아아이스티', '유자차', '레몬차']
    
    option_list = ['핫', '아이스', '연하게', '샷추가', '2샷추가']
    credits_list = ['카드', '삼성페이', '앱카드', 'QR/바코드', '쿠폰사용']

    selected_drink = None
    selected_option = None
    selected_credit = None

    if '카페' in input_text or '커피' in input_text:
        answer_text = '원하시는 음료를 선택해주세요'
    else:
        for drink in drink_list:
            if drink in input_text:
                selected_drink = drink
                break

        if selected_drink:
            for option in option_list:
                if option in input_text:
                    selected_option = option
                    break

            if selected_option:
                answer_text = f'({selected_option}){selected_drink}를 선택하셨나요? 맞으시면 확인 아니면 취소 버튼을 눌러주세요'
            #else:
            #   answer_text = f'{selected_drink}를 선택하셨나요? 온도와 농도를 선택해주세요. 핫, 아이스, 연하게, 샷추가, 2샷추가' 
            
    
    if '확인' in input_text:
        answer_text = '결제 수단을 선택해주세요'
        
    elif '취소' in input_text:
        answer_text = '원하시는 음료를 선택해주세요'
        
        
    if '카드' in input_text or '삼성페이' in input_text or '앱카드' in input_text or 'QR/바코드' in input_text or '쿠폰사용' in input_text:
        for credit in credits_list:
            if credit in input_text:
                selected_credit = credit
                break

        if selected_credit:
            if selected_credit in ['카드', '삼성페이']:
                answer_text = f'{selected_credit}를 선택하셨나요? 신용/체크카드를 넣어주세요'
            elif selected_credit in ['앱카드', 'QR/바코드']:
                answer_text = f'{selected_credit}를 선택하셨나요? 화면을 리더기에 인식해주세요'
            elif selected_credit == '쿠폰사용':
                answer_text = f'{selected_credit}를 선택하셨나요? 바코드를 인식해주세요'
                # 결제 완료 후 메시지 추가
            answer_text += ' 결제가 완료되었습니다. 다음에 또 이용해주세요!'
        else:
            answer_text = '결제 수단을 다시 말씀해주시겠어요?'

    if not answer_text:  # answer_text가 여전히 빈 문자열이라면
        answer_text = '다시 한 번 말씀해주시겠어요?'

    speak(answer_text)

# 소리내어 읽기(TTS)
def speak(text):
    if not text:  # text가 비어있으면 오류 방지
        print("오류: 출력할 텍스트가 없습니다.")
        return
    print('[인공지능]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):  # voice.mp3 파일 삭제
        os.remove(file_name)

# 메인 실행
r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)

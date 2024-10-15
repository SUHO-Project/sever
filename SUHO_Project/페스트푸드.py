import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        text = text.strip()  # 앞뒤 공백 제거
        print('[김태기]' + text)
        answer(text)
    except sr.UnknownValueError:
        print("인식 실패")  # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print("요청 실패 : {0}".format(e))  # API Key 오류, 네트워크 단절 등

# 대답 페스트푸드
def answer(input_text):
    answer_text = ''
    burger_list = ['데리버거', '치킨버거', '새우버거', '불고기버거', '치즈버거', '더블데리버거']
    side_list = ['감자튀김', '치즈스틱', '치킨너겟', '롱치즈스틱']
    drink_list = ['콜라', '사이다', '아이스티', '레몬에이드', '오렌지주스']
    credits_list = ['카드', '삼성페이', '앱카드', 'QR/바코드', '쿠폰사용']

    selected_burger = None
    selected_side = None
    selected_drink = None
    selected_credit = None

    # 세트 또는 단품 선택 여부
    is_set = False

    # 단품인지 세트인지 먼저 확인
    if '단품' in input_text:
        answer_text = f'단품을 선택하셨습니다. 버거 메뉴는 {", ".join(burger_list)} 중에서 선택해주세요.'
    
    elif '세트' in input_text:
        is_set = True
        answer_text = f'세트를 선택하셨습니다. 버거 메뉴는 {", ".join(burger_list)} 중에서 선택해주세요.'

    # 버거 선택 여부 확인
    for burger in burger_list:
        if burger in input_text:
            selected_burger = burger
            break

    if selected_burger:
        if is_set:
            # 세트일 경우 사이드 선택 요청
            answer_text = f'{selected_burger} 세트를 선택하셨습니다. 사이드 메뉴는 {", ".join(side_list)} 중에서 하나를 선택해주세요.'
        else:
            # 단품일 경우 바로 결제 단계로 이동
            answer_text = f'{selected_burger} 단품을 선택하셨습니다. 결제 수단을 선택해주세요.'

    # 사이드 선택 여부 확인
    for side in side_list:
        if side in input_text:
            selected_side = side
            break

    if selected_side:
        if is_set:
            # 세트일 경우 음료 선택 요청
            answer_text = f'{selected_side}를 선택하셨습니다. 음료는 {", ".join(drink_list)} 중에서 하나를 선택해주세요.'

    # 음료 선택 여부 확인
    for drink in drink_list:
        if drink in input_text:
            selected_drink = drink
            break

    if selected_drink:
        # 세트일 경우 음료 선택 후 결제 단계로 이동
        answer_text = f'{selected_drink}를 선택하셨습니다. 결제 수단을 선택해주세요.'

    # 결제 수단 확인
    if '확인' in input_text:
        answer_text = '결제 수단을 선택해주세요.'
        
    elif '취소' in input_text:
        answer_text = '원하시는 음식을 다시 선택해주세요.'
        
    # 결제 로직
    if '카드' in input_text or '삼성페이' in input_text or '앱카드' in input_text or 'QR/바코드' in input_text or '쿠폰사용' in input_text:
        for credit in credits_list:
            if credit in input_text:
                selected_credit = credit
                break

        if selected_credit:
            if selected_credit in ['카드', '삼성페이']:
                answer_text = f'{selected_credit}를 선택하셨나요? 신용/체크카드를 넣어주세요.'
            elif selected_credit in ['앱카드', 'QR/바코드']:
                answer_text = f'{selected_credit}를 선택하셨나요? 화면을 리더기에 인식해주세요.'
            elif selected_credit == '쿠폰사용':
                answer_text = f'{selected_credit}를 선택하셨나요? 바코드를 인식해주세요.'
            
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

speak('단품 또는 세트를 선택해주세요.')
stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)

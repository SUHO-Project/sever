# 🧓 디지털 소외계층을 위한 대화형 교육 키오스크 시스템

> **고령층의 디지털 접근성을 높이고, 음성 기반 대화형 인터페이스를 통해 쉽고 친숙한 교육 경험을 제공하는 키오스크 시스템입니다.**

---

[![시연 영상 썸네일](https://github.com/Agayeon/assets/blob/main/elderly-kiosk-thumbnail.png?raw=true)](https://drive.google.com/file/d/1hqrVp58GPIEAkL7ACWudB-fUo6VItSXc/view?usp=drive_link)
> 🎥 이미지를 클릭하면 **시연 영상(Google Drive)** 으로 이동합니다.

---

## 📖 프로젝트 개요

- **프로젝트명**: 디지털 소외계층을 위한 대화형 교육 키오스크 시스템  
- **개발 기간**: 2024.06 ~ 2024.10  
- **개발 인원**: 4명  
- **개발 목적**: 고령자들이 키오스크 사용법을 쉽고 편리하게 익힐 수 있도록 음성 대화형 학습 환경을 제공하는 시스템 구축.

---

## 💡 주요 기능

| 기능 | 설명 |
|------|------|
| 🎙️ **음성 인식(STT)** | 사용자의 음성을 명령어로 인식 |
| 🔊 **음성 출력(TTS)** | 시스템 응답을 음성으로 안내 |
| 🖱️ **터치 기반 UI** | 메뉴 선택·결제 등 인터랙션 지원 |
| 🪟 **팝업창 UI** | 주문/결제/취소 등 상황별 팝업 제공 |
| 🧭 **학습 모드** | 단계별 교육 및 연습 기능 제공 |
| 🏠 **초기화 기능** | 학습 종료 후 자동으로 첫 화면 복귀 |

---

## 🧱 시스템 구조

Frontend (HTML / CSS / JS)
│
▼
Flask Backend (Python)
│
├── SpeechRecognition (STT)
├── gTTS (TTS)
└── REST API 통신

yaml
코드 복사

---

## 🧑‍💻 기술 스택

| 구분 | 사용 기술 |
|------|------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python (Flask), Django |
| **AI/Voice** | gTTS, SpeechRecognition |
| **DB** | Django ORM / SQLite |
| **배포** | AWS EC2 |
| **기타** | REST API, LAN 통신 기반 |

---

🏆 수상 및 성과
팀 프로젝트 우수상 (캡스톤디자인)
발표 주제: “고령층을 위한 음성 기반 대화형 키오스크 교육 시스템”

📂 발표 자료 & 🎥 시연 영상
📘 프로젝트 발표 PPT: PPT 보기

🎬 시연 영상: 영상 보기

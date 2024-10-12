# KNUE Noti Bot

![GitHub License](https://img.shields.io/github/license/kadragon/knue-noti-bot)
![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)

KNUE Noti Bot은 한국교원대학교 대표 홈페이지 및 기타 사이트의 공지사항을 자동으로 수집하여 Telegram 그룹에 요약된 정보를 전송하는 봇입니다. 이 봇은 최신 공지사항을 신속하게 확인하고 공유하는 데 도움을 줍니다.

## 📖 목차

- [기능](#기능)
- [설치](#설치)
- [사용 방법](#사용-방법)
- [환경 변수 설정](#환경-변수-설정)
- [기여하기](#기여하기)
- [라이센스](#라이센스)

## 기능

1. **RSS 수집**: 한국교원대학교 대표 홈페이지 등에서 공지사항 RSS 피드를 수집합니다.
2. **중복 확인**: 수집한 RSS 정보를 GitHub Gist에 저장된 기존 정보와 비교하여 새로 올라온 글을 식별합니다.
3. **요약 생성**: GPT를 이용하여 새로 올라온 공지사항을 요약합니다.
4. **Telegram 전송**: 요약된 공지사항을 특정 Telegram 그룹에 메시지로 전송합니다.
5. **자동화**: GitHub Actions를 통해 평일 오전 9시부터 오후 6시까지 매 정시에 자동으로 실행됩니다.

## 설치

### 1. 클론하기

```bash
git clone https://github.com/yourusername/knue-noti-bot.git
cd knue-noti-bot
```

### 2. 종속성 설치

```bash
pip install -r requirements.txt
```

## 사용 방법

1. 환경 변수 설정: 다음 섹션에서 설명하는 환경 변수를 설정합니다.
2. GitHub Gist 생성: 새 공지사항을 추적하기 위해 Gist를 생성하고 Gist ID를 환경 변수에 추가합니다.
3. Telegram Bot 생성: [BotFather](https://telegram.me/BotFather)를 통해 Telegram 봇을 생성하고, 봇 토큰 및 대상 그룹 ID를 환경 변수에 추가합니다.
4. GitHub Actions 활성화: .github/workflows/main.yml 파일을 확인하고 필요한 설정을 완료합니다.

## 환경 변수 설정

프로젝트는 다음 환경 변수를 필요로 합니다:

- RSS_FEEDS: 모니터링할 RSS 피드 URL 목록 (쉼표로 구분)
- GIST_ID: RSS 정보를 저장할 GitHub Gist ID
- OPENAI_API_KEY: GPT 요약을 위한 OpenAI API 키
- TELEGRAM_BOT_TOKEN: Telegram 봇 토큰
- TELEGRAM_CHAT_ID_1: 메시지를 보낼 Telegram 그룹의 채팅 ID_1
- TELEGRAM_CHAT_ID_2: 메시지를 보낼 Telegram 그룹의 채팅 ID_2
- TELEGRAM_CHAT_ID_3: 메시지를 보낼 Telegram 그룹의 채팅 ID_3

> 주의: .env 파일에는 민감한 정보가 포함되어 있으므로 절대 공개 저장소에 업로드하지 마세요.

## 기여하기

기여를 환영합니다! 버그 리포트나 기능 요청은 [Issues](https://github.com/kadragon/knue-noti-bot/issues)에 작성해 주세요. 풀 리퀘스트도 환영합니다.

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)에 따라 라이선스가 부여됩니다.

---

© 2024 [kadragon](https://github.com/kadragon)

---

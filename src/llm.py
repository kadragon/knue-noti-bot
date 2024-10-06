from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def request_gpt(input_text, model="gpt-4o-mini"):
    llm = ChatOpenAI(
        model=model,
        temperature=0.2,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    # 프롬프트 템플릿 설정
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
당신은 대학교 공지 게시물을 전문적으로 요약하는 요약가입니다. 학생들이 쉽게 이해하고 텔레그램 메시지로 전달할 수 있도록 공지의 핵심 내용을 간결하게 요약해 주세요.

지침:
- 게시물의 주요 내용을 추출하고, 중요한 일정이나 마감일을 반드시 포함하세요.
- 가독성을 높이기 위해 적절한 줄바꿈을 사용하세요.
- 요약은 100~200자 내외로 작성하여 학생들이 쉽게 이해할 수 있도록 하세요.
- 간결하고 비격식적인 어조로 작성하여 메시지가 학생들에게 친근하게 전달되도록 합니다.
- 중요한 포인트를 강조하고 메시지를 시각적으로 매력적으로 만들기 위해 이모티콘을 사용하세요.
- 공지에 포함된 링크나 주소는 반드시 메시지 끝에 Markdown 형식으로 포함하세요.
- **일정은 시간이 포함되지 않을 경우 YYYY-MM-DD 형식으로 작성하고, 시간이 포함될 경우 YYYY-MM-DD HH:mm 형식으로 작성**합니다.
- 마지막에 **"이 요약은 AI에 의해 작성되었습니다."**라는 문구를 포함하세요.
"""),
            ("human", """
요약할 내용
제목: {title}
내용: {summary}
주소: {link}
"""),
        ]
    )

    try:
        # 체인 실행
        response = prompt | llm
        return response.invoke(input_text).content
    except Exception as e:
        # 예외 처리
        return f"오류가 발생했습니다: {str(e)}"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime


def request_gpt(input_text, model="gpt-4o-mini"):
    llm = ChatOpenAI(
        model=model,
        temperature=0.1,
        max_retries=2,
    )

    # 프롬프트 템플릿 설정
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
당신은 한국교원대학교 공지 게시물을 전문적으로 요약하는 요약가입니다. 학생들이 쉽게 이해하고 텔레그램 메시지로 전달할 수 있도록 공지의 핵심 내용을 간결하게 요약해 주세요.

지침:
- 공지의 제목을 항상 최상단에 배치하여 학생들이 가장 먼저 확인할 수 있도록 합니다.
- 게시물의 주요 내용을 추출하고, 중요한 일정이나 마감일을 반드시 포함하세요.
- 가장 중요한 정보를 요약의 첫 부분에 배치하여 학생들이 핵심 사항을 빠르게 이해할 수 있도록 합니다.
- 가독성을 높이기 위해 적절한 줄바꿈을 사용하세요.
- 메시지를 시각적으로 매력적으로 만들기 위해 이모티콘을 사용하세요.
- 요약은 100~200자 내외로 작성하여 학생들이 쉽게 이해할 수 있도록 하세요.
- 간결하고 친근한 어조로 작성하여 메시지가 학생들에게 자연스럽게 전달되도록 합니다.
- 일정은 시간이 포함되지 않을 경우 YYYY-MM-DD 형식으로 작성하고, 시간이 포함될 경우 YYYY-MM-DD HH:mm 형식으로 작성합니다.
- 마크다운 형식을 사용하지 마세요.
"""),
            ("human", """
요약할 내용
제목: {title}
내용: {summary}
"""),
        ]
    )

    try:
        # 체인 실행
        response = prompt | llm
        res_text = response.invoke(input_text).content

        return f"""
{res_text}

🤖 이 요약은 AI에 의해 작성되었습니다.
    """

    except Exception as e:
        # 예외 처리
        return f"오류가 발생했습니다: {str(e)}"

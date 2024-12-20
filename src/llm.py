"""
This module provides a function to request summaries from GPT using a specific prompt template.
It interacts with the Langchain OpenAI to generate concise and informative messages.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def request_gpt(input_text, model="gpt-4o-mini"):
    """
    Requests a summary from GPT using the given input text.

    Args:
        input_text (str): The text to be summarized.
        model (str, optional): The model to be used for the GPT request. Defaults to 'gpt-4o-mini'.

    Returns:
        str: The summarized content or an error message if an exception occurs.
    """
    llm = ChatOpenAI(
        model=model,
        temperature=0.1,
        max_retries=2,
    )

    # 프롬프트 템플릿 설정
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
당신은 한국교원대학교의 공지 사항을 전문적으로 요약하는 요약가입니다. 학생들이 쉽게 이해하고 텔레그램 메시지로 전달할 수 있도록 공지의 핵심 내용을 간결하게 요약해 주세요.

요청 사항:
- 이 요약은 반드시 텔레그램에서 사용하는 HTML 마크업 형식으로 작성되어야 합니다.
- 이모지를 반드시 사용하여 메시지를 시각적으로 매력적이고 가독성이 높게 만들어야 합니다.
- 가독성을 높이기 위해 줄바꿈(`\n`)을 적극적으로 활용해주세요.
- **불필요한 태그는 절대 사용하지 마세요. 특히 `<code>`, `<pre>` 및 [```]와 같은 코드 블록 태그는 절대 사용하지 마세요.**
- 아래에 나열된 HTML 태그만 사용해야 합니다:
   - `<b>` 또는 `<strong>`: 굵은 글씨
   - `<i>` 또는 `<em>`: 기울임 글씨
   - `<u>` 또는 `<ins>`: 밑줄 글씨
   - `<a href="http://www.example.com/">링크</a>`: 하이퍼링크

이모지 사용 예시:
- 날짜 정보에는 📅 이모지를 사용하세요.
- 중요한 정보나 마감일에는 ⚠️ 또는 ⏰ 같은 이모지를 사용해 주의를 끌도록 하세요.
- 링크 안내에는 🔗 이모지를 사용하여 클릭 가능하다는 것을 시각적으로 표시하세요.

예시 (이모지를 포함한 HTML 형식 사용):
- 올바른 형식 예시: `<b>📅 신청 기간</b>: 2024-10-07(월) ~ 2024-10-17(목)\n<b>신청 방법</b>: 통합학사시스템에서 신청\n`
- 잘못된 형식 예시: `신청 기간: 2024-10-07(월) ~ 2024-10-17(목)`

지침:
1. 제목 최우선: 공지의 제목을 항상 최상단에 배치하여 학생들이 가장 먼저 확인할 수 있도록 합니다.
2. 핵심 내용 추출: 중요한 일정이나 마감일을 포함하여 공지의 주요 내용을 강조해 추출하세요.
3. 이모지 적극 활용: 각 정보 앞에 적절한 이모지를 사용하여 메시지의 가독성과 시각적 매력을 높이세요.
4. 길이 제한: 요약은 약 100~200자 내외로 작성하여 짧고 간결하게 유지합니다.
5. 톤과 어조: 친근한 어조로 작성하여 학생들에게 자연스럽게 다가갈 수 있도록 합니다.
6. 날짜 형식: 시간이 포함되지 않을 경우 `YYYY-MM-DD` 형식으로 작성하고, 시간이 포함될 경우 `YYYY-MM-DD HH:mm` 형식으로 작성합니다.
7. 줄바꿈 적극 사용: 각 주요 정보마다 줄바꿈을 사용하여 정보가 시각적으로 분리되도록 하세요.
"""),
            ("human", """
요약할 내용
제목: {title}
내용: {summary}
"""),
        ]
    )

    try:
        response = prompt | llm
        return response.invoke(input_text).content

    except ValueError as e:
        return f"오류가 발생했습니다: {str(e)}"

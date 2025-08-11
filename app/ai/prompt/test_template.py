# 테스트용 프롬프트
from langchain_core.prompts import ChatPromptTemplate

TEST_PROMPT = """
가장 맛있는 과일과 그 과일이 가장 많이 생산되는 지역을 알려줘

[출력 형식]
{format}
"""

# 테스트용 프롬프트 템플릿
test_template = ChatPromptTemplate.from_messages([
    ("human", TEST_PROMPT)
])

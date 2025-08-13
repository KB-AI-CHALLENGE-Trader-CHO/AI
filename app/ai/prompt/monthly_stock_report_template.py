from langchain_core.prompts import ChatPromptTemplate

from app.ai.prompt.common_template import COMMON_SYSTEM_MESSAGE

# 월간 종목 평가 프롬프트
monthly_stock_reports_prompt = '''
제가 이번주에 진행한 종목 중 하나의 매매들의 평가는 다음과 같습니다.
{stock_reports}
'''

mission = '''
저의 매매 평가들을 바탕으로 아래와 같이 월간 단일 종목 매매에 대한 종합 분석 결과를 500자 이내로 말해주세요.

[월간 단일 종목 매매 분석 결과]
내용 응답

출력은 반드시 다음 형식을 따르고, 다른 텍스트는 절대 출력하지 마세요.
{format_instructions}
'''

# 월간 종목 평가 프롬프트 템플릿
monthly_stock_report_template = ChatPromptTemplate.from_messages([
    ("system", COMMON_SYSTEM_MESSAGE),
    ("human", monthly_stock_reports_prompt)
]).partial(mission=mission)

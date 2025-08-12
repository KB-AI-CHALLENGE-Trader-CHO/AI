from langchain_core.prompts import ChatPromptTemplate

from app.ai.prompt.common_template import COMMON_SYSTEM_MESSAGE

# 매매별 평가 프롬프트
trade_prompt = '''
제 거래 정보와 제가 생각해서 적은 메모는 다음과 같습니다.
{trade_info}

이를 토대로 판단한 분봉 및 일봉 평가 지표는 다음과 같습니다. 분봉은 infra, 일봉은 daily로 접두사로 시작합니다.
{trade_evaluation}
'''

mission = '''
제가 작성한 매매 일지와 주가 정보들을 바탕으로 어떤 점에서 잘된 매매이고, 어떤 점에서 부족한 매매인지, 향후에 어떤 식으로 하면 좋을지를
[잘한점]
내용 응답

[못한점]
내용 응답

[향후 개선 방향]
내용 응답

위와 같이 응답해주세요. 매수일 경우 avg_buy_price의 값을 신경쓰지 말고 답변해주세요.

출력은 반드시 다음 형식을 따르고, 다른 텍스트는 절대 출력하지 마세요.
{format_instructions}
'''

# 매매별 프롬프트 템플릿
trade_report_template = ChatPromptTemplate.from_messages([
    ("system", COMMON_SYSTEM_MESSAGE),
    ("human", trade_prompt)
]).partial(mission=mission)

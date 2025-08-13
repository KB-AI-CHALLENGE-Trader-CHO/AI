from pydantic import BaseModel, Field


class TestModel(BaseModel):
    """LLM 테스트용 모델"""

    name: str = Field(description="과일의 이름")
    region: str = Field(description="과일이 가장 많이 생산되는 지역")


class TradeReport(BaseModel):
    """매매별 분석 리포트"""

    good: str = Field(description="[잘한점]에 이어서 나오는 내용")
    bad: str = Field(description="[못한점]에 이어서 나오는 내용")
    suggestions: str = Field(description="[향후 개선 방향]에 이어서 나오는 내용")

    def get_suggestions_string(self):
        return f"[잘한 점]\n{self.good}\n\n[못한 점]\n{self.bad}\n\n[향후 개선 방향]\n{self.suggestions}"


class WeeklyReport(BaseModel):
    """주간 매매 일지 종합 분석 리포트"""

    summary: str = Field(description="[주간 매매 일지 종합 분석 결과]에 이어서 나오는 내용")


class MonthlyStockReport(BaseModel):
    """월간 종목별 매매 분석 리포트"""

    analysis_detail: str = Field(description="[월간 단일 종목 매매 분석 결과]에 이어서 나오는 내용")


class MonthlyReport(BaseModel):
    """월간 매매 일지 종합 분석 리포트"""

    summary: str = Field(description="월간 매매 종합 분석 결과")

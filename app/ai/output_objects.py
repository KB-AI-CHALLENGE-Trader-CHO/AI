from pydantic import BaseModel, Field


class TestModel(BaseModel):
    """LLM 테스트용 모델"""

    name: str = Field(description="과일의 이름")
    region: str = Field(description="과일이 가장 많이 생산되는 지역")


class DailyReport(BaseModel):
    """일별 매매 일지 분석 리포트"""

    analysis_details: str = Field(description="매매 일지 분석 결과")
    suggestions: str = Field(description="분석 결과에 따른 매매 관련 제안")


class WeeklyReport(BaseModel):
    """주간 매매 일지 종합 분석 리포트"""

    summary: str = Field(description="주간 매매 일지 종합 분석 결과")


class MonthlyStockReport(BaseModel):
    """월간 종목별 매매 분석 리포트"""

    analysis_details: str = Field(description="매매 일지 분석 결과")
    suggestions: str = Field(description="분석 결과에 따른 매매 관련 제안")


class MonthlyReport(BaseModel):
    """월간 매매 일지 종합 분석 리포트"""

    summary: str = Field(description="월간 매매 일지 종합 분석 결과")

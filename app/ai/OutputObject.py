from pydantic import BaseModel, Field


# LLM 테스트용 모델
class TestModel(BaseModel):
    name: str = Field(description="과일의 이름")
    region: str = Field(description="과일이 가장 많이 생상되는 지역")


# 주 단위로 매매 건수 별로 생성
class DailyReport(BaseModel):
    analysis_details: str = Field(description="매매 일지 분석 결과")
    suggestions: str = Field(description="분석 결과에 따른 매매 관련 제안")


# 주 단위로 일별 매매 건수를 모두 합쳐서 생성
class WeeklyReport(BaseModel):
    summary: str = Field(description="주간 매매 일지 종합 분석 결과")


# 월 단위로 매매한 종목 별로 생성
class MonthlyStockReport(BaseModel):
    analysis_details: str = Field(description="매매 일지 분석 결과")
    suggestions: str = Field(description="분석 결과에 따른 매매 관련 제안")


# 월 단위로 매매한 모든 종목 요약
class MonthlyReport(BaseModel):
    summary: str = Field(description="월간 매매 일지 종합 분석 결과")

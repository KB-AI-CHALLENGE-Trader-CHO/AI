from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class BaseOutputParser(BaseModel):
    def get_output_parser(self) -> PydanticOutputParser:
        return PydanticOutputParser(pydantic_object=self)


# 주 단위로 매매 건수 별로 생성
class DailyReport(BaseOutputParser):
    analysis_details: str = Field(description="매매 일지 분석 결과")
    suggestions: str = Field(description="분석 결과에 따른 매매 관련 제안")


# 주 단위로 일별 매매 건수를 모두 합쳐서 생성
class WeeklyReport(BaseOutputParser):
    summary: str = Field(description="주간 매매 일지 종합 분석 결과")


# 월 단위로 매매한 종목 별로 생성
class MonthlyStockReport(BaseOutputParser):
    analysis_details: str = Field(description="매매 일지 분석 결과")
    suggestions: str = Field(description="분석 결과에 따른 매매 관련 제안")


# 월 단위로 매매한 모든 종목 요약
class MonthlyReport(BaseOutputParser):
    summary: str = Field(description="월간 매매 일지 종합 분석 결과")

from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain_core.language_models import LLM
from langchain_core.prompts import PromptTemplate
from typing import Optional
import logging

from app.ai.llm_model import llm_model
from app.ai.prompt.monthly_report_template import monthly_report_template
from app.ai.prompt.monthly_stock_report_template import monthly_stock_report_template
from app.ai.prompt.weekly_report_template import weekly_report_template
from app.schemas.report_schema import TestModel, TradeReport, WeeklyReport, MonthlyStockReport, MonthlyReport
from app.ai.prompt.test_template import test_template
from app.ai.prompt.trade_report_template import trade_report_template

logger = logging.getLogger(__name__)


class LLMChain:
    def __init__(
            self,
            prompt: PromptTemplate,
            model: LLM,
            parser: PydanticOutputParser
    ) -> None:
        self.prompt = prompt
        self.model = model
        self.output_parser = parser

    def invoke(self, prompt_parameter: dict) -> Optional[str]:
        try:
            if not self.model:
                logger.error("LLM 모델이 초기화되지 않았습니다.")
                return None

            chain = self.prompt | self.model | self.output_parser
            result = chain.ainvoke(prompt_parameter)
            logger.info("동기 체인 실행 성공")
            return result
        except Exception as e:
            logger.error(f"동기 프롬프트 실행 실패: {e}")
            return None

    def batch(self, prompt_parameter: list[dict], batch_size: int = 5) -> Optional[list[str]]:
        try:
            if not self.model:
                logger.error("LLM 모델이 초기화되지 않았습니다.")
                return None

            chain = self.prompt | self.model | self.output_parser
            result = chain.abatch(prompt_parameter, config={"max_concurrency": batch_size})
            logger.info("동기 배치 체인 실행 성공")
            return result
        except Exception as e:
            logger.info(f"동기 배치 프롬프트 실행 실패: {e}")
            return None

    async def ainvoke(self, prompt_parameter: dict) -> Optional[str]:
        try:
            if not self.model:
                logger.error("LLM 모델이 초기화되지 않았습니다.")
                return None

            chain = self.prompt | self.model | self.output_parser
            result = await chain.ainvoke(prompt_parameter)
            logger.info("비동기 체인 실행 성공")
            return result
        except Exception as e:
            logger.error(f"비동기 프롬프트 실행 실패: {e}")
            return None

    async def abatch(self, prompt_parameter: list[dict], batch_size: int = 5) -> Optional[list[str]]:
        try:
            if not self.model:
                logger.error("LLM 모델이 초기화되지 않았습니다.")
                return None

            chain = self.prompt | self.model | self.output_parser
            result = await chain.abatch(prompt_parameter, config={"max_concurrency": batch_size})
            logger.info("비동기 배치 체인 실행 성공")
            return result
        except Exception as e:
            logger.info(f"비동기 배치 프롬프트 실행 실패: {e}")
            return None


test_chain = LLMChain(
    prompt=test_template.partial(format_instructions=PydanticOutputParser(pydantic_object=TestModel).get_format_instructions()),
    model=llm_model.get_model(),
    parser=PydanticOutputParser(pydantic_object=TestModel)
)

# 매매별 분석 체인
trade_report_parser = PydanticOutputParser(pydantic_object=TradeReport)
fixing_parser = OutputFixingParser.from_llm(parser=trade_report_parser, llm=llm_model.get_model())
trade_report_chain = LLMChain(
    prompt=trade_report_template.partial(format_instructions=fixing_parser.get_format_instructions()),
    model=llm_model.get_model(),
    parser=fixing_parser,
)

# 주간 종합 분석 체인
weekly_report_parser = PydanticOutputParser(pydantic_object=WeeklyReport)
weekly_fixing_parser = OutputFixingParser.from_llm(parser=weekly_report_parser, llm=llm_model.get_model())
weekly_report_chain = LLMChain(
    prompt=weekly_report_template.partial(format_instructions=weekly_fixing_parser.get_format_instructions()),
    model=llm_model.get_model(),
    parser=weekly_fixing_parser,
)

# 월간 종목 분석 체인
monthly_stock_report_parser = PydanticOutputParser(pydantic_object=MonthlyStockReport)
monthly_stock_fixing_parser = OutputFixingParser.from_llm(parser=monthly_stock_report_parser, llm=llm_model.get_model())
monthly_stock_report_chain = LLMChain(
    prompt=monthly_stock_report_template.partial(format_instructions=monthly_stock_fixing_parser.get_format_instructions()),
    model=llm_model.get_model(),
    parser=monthly_stock_fixing_parser,
)

# 월간 종합 분석 체인
monthly_report_parser = PydanticOutputParser(pydantic_object=MonthlyReport)
monthly_fixing_parser = OutputFixingParser.from_llm(parser=monthly_report_parser, llm=llm_model.get_model())
monthly_report_chain = LLMChain(
    prompt=monthly_report_template.partial(format_instructions=monthly_fixing_parser.get_format_instructions()),
    model=llm_model.get_model(),
    parser=monthly_fixing_parser,
)

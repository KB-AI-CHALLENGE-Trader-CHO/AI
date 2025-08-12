from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain_core.language_models import LLM
from langchain_core.prompts import PromptTemplate
from typing import Optional
import logging

from app.ai.llm_model import llm_model
from app.schemas.report_schema import TestModel, TradeReport
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

    async def abatch(self, prompt_parameter: list[dict], batch_size: int = 5) -> Optional[str]:
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
    prompt=test_template.partial(
        format_instructions=PydanticOutputParser(pydantic_object=TestModel).get_format_instructions()),
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

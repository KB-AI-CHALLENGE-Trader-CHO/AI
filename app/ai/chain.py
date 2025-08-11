from langchain.output_parsers import PydanticOutputParser
from langchain_core.language_models import LLM
from langchain_core.prompts import PromptTemplate
from typing import Any, Optional
import logging

from .llm_model import llm_model
from .output_objects import TestModel
from .prompt_template import test_template

logger = logging.getLogger(__name__)


class LLMChain:
    def __init__(
            self,
            prompt: PromptTemplate,
            model: LLM,
            parser: PydanticOutputParser
    ) -> None:
        self.prompt = prompt.partial(format=parser.get_format_instructions())
        self.model = model.get_model()
        self.output_parser = parser

    async def ainvoke(self) -> Optional[str]:
        try:
            if not self.model:
                logger.error("LLM 모델이 초기화되지 않았습니다.")
                return None

            chain = self.prompt | self.model | self.output_parser
            result = await chain.ainvoke({})
            logger.info("비동기 체인 실행 성공")
            return result
        except Exception as e:
            logger.error(f"비동기 프롬프트 실행 실패: {e}")
            return None

    async def abatch(self) -> Optional[str]:
        try:
            if not self.model:
                logger.error("LLM 모델이 초기화되지 않았습니다.")
                return None

            chain = self.prompt | self.model | self.output_parser
            result = await chain.abatch({})
            logger.info("비동기 배치 체인 실행 성공")
            return result
        except Exception as e:
            logger.error(f"비동기 배치 프롬프트 실행 실패: {e}")
            return None


test_chain = LLMChain(
    prompt=test_template,
    model=llm_model,
    parser=PydanticOutputParser(pydantic_object=TestModel)
)

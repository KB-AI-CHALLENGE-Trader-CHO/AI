from langchain.output_parsers import PydanticOutputParser
from langchain_core.language_models import LLM
from langchain_core.prompts import PromptTemplate

import logging

from app.ai.llm_model import llm_model
from app.ai.OutputObject import TestModel
from app.ai.prompt_template import test_template

logger = logging.getLogger(__name__)


class LlmChain:

    def __init__(self, prompt: PromptTemplate, model: LLM, parser: PydanticOutputParser):
        self.prompt = prompt.partial(format=parser.get_format_instructions())
        self.model = model.get_model()
        self.output_parser = parser

    async def ainvoke(self):
        try:
            chain = self.prompt | self.model | self.output_parser
            return await chain.ainvoke({})
        except Exception as e:
            logging.error(f"비동기 프롬프트 실행 실패: {e}")

    async def abatch(self):
        try:
            chain = self.prompt | self.model | self.output_parser
            return await chain.abatch({})
        except Exception as e:
            logging.error(f"비동기 배치 프롬프트 실행 실패: {e}")


test_chain = LlmChain(prompt=test_template, model=llm_model,
                      parser=PydanticOutputParser(pydantic_object=TestModel))

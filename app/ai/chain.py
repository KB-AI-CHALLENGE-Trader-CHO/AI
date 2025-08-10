from langchain_core.language_models import LLM
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import PromptTemplate

import logging

from app.ai.llm_model import llm_model
from app.ai.output_parser import DailyReport
from app.ai.prompt_template import daily_template

logger = logging.getLogger(__name__)


class LlmChain:

    def __init__(self, prompt: PromptTemplate, model: LLM, parser: BaseOutputParser):
        self.prompt = prompt
        self.model = model
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

daily_report_chain = LlmChain(daily_template, llm_model, DailyReport().get_output_parser())
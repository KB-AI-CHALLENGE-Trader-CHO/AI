from langchain_openai import ChatOpenAI
from app.config import settings
import logging

logger = logging.getLogger(__name__)


class LLMService:

    def __init__(self):
        self.llm = None
        self._initialize_llm()

    def _initialize_llm(self):
        try:
            self.llm = ChatOpenAI(
                model=settings.OPENAI_MODEL_NAME,
                temperature=settings.OPENAI_TEMPERATURE,
                max_tokens=settings.OPENAI_MAX_TOKENS)
        except Exception as e:
            logger.error(f"LLM 초기화 실패: {e}")
            self.llm = None


llm_service = LLMService()

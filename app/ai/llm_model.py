from langchain_openai import ChatOpenAI
import logging

from app.config import settings

logger = logging.getLogger(__name__)


class LLM:

    def __init__(self,
                 model: str = "gpt-4.1-nano",
                 temperature: float = 0.7,
                 max_tokens: int = 1000,
                 max_retries: int = 3):
        self.llm = None
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.openai_api_key = settings.OPENAI_API_KEY
        self._initialize_llm()

    def _initialize_llm(self):
        try:
            self.llm = ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                max_retries=self.max_retries,
                openai_api_key=self.openai_api_key
            )
        except Exception as e:
            logger.error(f"LLM 초기화 실패: {e}")
            self.llm = None

    def get_model(self):
        return self.llm


llm_model = LLM("gpt-4.1-nano", 0.7, 1000, 3)

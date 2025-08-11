from langchain_openai import ChatOpenAI
from typing import Optional
import logging

from app.config import settings

logger = logging.getLogger(__name__)


class LLMModel:

    def __init__(
            self,
            model: str = "gpt-4o-mini",
            temperature: float = 0.7,
            max_tokens: int = 1000,
            max_retries: int = 3
    ) -> None:
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.openai_api_key = settings.OPENAI_API_KEY
        self._llm: Optional[ChatOpenAI] = None
        self._initialize_llm()

    def _initialize_llm(self) -> None:
        try:
            self._llm = ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                max_retries=self.max_retries,
                openai_api_key=self.openai_api_key
            )
            logger.info(f"LLM 모델 '{self.model}' 초기화 성공")
        except Exception as e:
            logger.error(f"LLM 초기화 실패: {e}")
            self._llm = None

    def get_model(self) -> Optional[ChatOpenAI]:
        return self._llm

    @property
    def is_initialized(self) -> bool:
        return self._llm is not None


# 기본 LLM 모델 인스턴스
llm_model = LLMModel("gpt-4o-mini", 0.7, 1000, 3)

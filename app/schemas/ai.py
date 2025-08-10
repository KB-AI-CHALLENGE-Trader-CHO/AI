from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class Message(BaseModel):
    """채팅 메시지 스키마"""
    role: str = Field(..., description="메시지 역할 (user, assistant, system)")
    content: str = Field(..., description="메시지 내용")


class ChatRequest(BaseModel):
    """채팅 요청 스키마"""
    messages: List[Message] = Field(..., description="대화 메시지 목록")
    system_prompt: Optional[str] = Field(None, description="시스템 프롬프트")
    temperature: Optional[float] = Field(0.7, description="창의성 조절 (0.0-1.0)")
    max_tokens: Optional[int] = Field(1000, description="최대 토큰 수")


class ChatResponse(BaseModel):
    """채팅 응답 스키마"""
    success: bool = Field(..., description="요청 성공 여부")
    response: Optional[str] = Field(None, description="AI 응답 내용")
    model: Optional[str] = Field(None, description="사용된 모델명")
    usage: Optional[Dict[str, Any]] = Field(None, description="토큰 사용량 정보")
    error: Optional[str] = Field(None, description="오류 메시지")

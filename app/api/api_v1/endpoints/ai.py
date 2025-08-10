from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.llm_service import llm_service
from app.schemas.ai import (
    ChatRequest,
    ChatResponse
)
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_completion(
        request: ChatRequest,
        db: Session = Depends(get_db)
):
    """AI 채팅 완성 API"""
    try:
        result = await llm_service.chat_completion(
            messages=request.messages,
            system_prompt=request.system_prompt
        )

        if result["success"]:
            return ChatResponse(
                success=True,
                response=result["response"],
                model=result["model"],
                usage=result.get("usage", {})
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result["error"]
            )

    except Exception as e:
        logger.error(f"채팅 완성 API 오류: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

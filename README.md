- Python 3.11 권장
- 의존성 설치 후 `.env`에 `OPENAI_API_KEY` 설정
- 서버 실행: `python run.py`
- 확인: `GET /health`, LLM 테스트: `GET /test`

### 1) 가상환경 및 의존성 설치
```bash
cd /Users/prefer52/Desktop/dev/ai
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip setuptools wheel
pip install -r requirements.txt
```

### 2) 환경변수 설정 (.env 파일 생성)
프로젝트 루트에 `.env` 파일 생성:
```bash
cat > .env << 'EOF'
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
OPENAI_MODEL_NAME=gpt-4o-mini
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=1000

# 선택: LangSmith 사용 시
LANGSMITH_API_KEY=
LANGSMITH_ENDPOINT=
LANGSMITH_PROJECT=trader-cho
LANGSMITH_TRACING=True
EOF
```

필수: `OPENAI_API_KEY`를 유효한 키로 설정해야 `/test` 엔드포인트가 동작합니다.

### 3) 서버 실행
```bash
python run.py
```
또는
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4) 동작 확인
- 헬스체크: `http://localhost:8000/health`
- 기본: `http://localhost:8000/`
- LLM 테스트: `http://localhost:8000/test`  (OpenAI 키 필요)

참고: 스케줄러는 등록만 되어 있고 시작은 안 되어 있어요. 필요하면 `startup` 이벤트에서 `JobManager.start_scheduler()`를 호출하도록 추가하면 됩니다.

- 변경 요약
  - 실행 엔트리포인트: `run.py`로 `uvicorn` 실행
  - API 엔드포인트: `/`, `/health`, `/test`
  - 환경설정: `.env`로 읽힘 (`app/config.py`의 `Settings`)
# FastAPI Backend Project

FastAPI를 사용한 백엔드 API 서버 프로젝트입니다.

## 기능

- FastAPI 기반 REST API
- SQLAlchemy를 사용한 데이터베이스 연동
- Pydantic을 사용한 데이터 검증
- JWT 인증
- 자동 API 문서 생성
- **LangChain을 통한 LLM 통합**
- **LangSmith를 통한 AI 모델 추적 및 모니터링**
- **LangGraph를 통한 워크플로우 및 도구 실행**

## 설치 방법

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate  # Windows
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 환경변수 설정
```bash
cp env.example .env
# .env 파일을 편집하여 데이터베이스 연결 정보 등을 설정
```

## 실행 방법

개발 서버 실행:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

프로덕션 서버 실행:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## AI 서비스 API

### 채팅 API
- `POST /api/v1/ai/chat` - AI와의 대화
- `GET /api/v1/ai/models/info` - 사용 가능한 모델 정보

### 워크플로우 API
- `POST /api/v1/ai/workflow/create` - 새 워크플로우 생성
- `POST /api/v1/ai/workflow/{name}/execute` - 워크플로우 실행
- `GET /api/v1/ai/workflows` - 워크플로우 목록
- `GET /api/v1/ai/workflow/{name}` - 워크플로우 정보

### 도구 API
- `POST /api/v1/ai/tools/execute` - 도구 실행

### 모니터링 API
- `GET /api/v1/ai/langsmith/status` - LangSmith 상태
- `GET /api/v1/ai/health/ai` - AI 서비스 헬스 체크

## 프로젝트 구조

```
app/
├── __init__.py
├── main.py              # FastAPI 앱 진입점
├── config.py            # 설정 관리
├── database.py          # 데이터베이스 연결
├── models/              # SQLAlchemy 모델
├── schemas/             # Pydantic 스키마
├── api/                 # API 라우터
├── core/                # 핵심 기능 (인증, 보안 등)
└── utils/               # 유틸리티 함수
```

## 데이터베이스 초기화

SQLite 데이터베이스를 사용하는 경우, 애플리케이션을 처음 실행하면 자동으로 테이블이 생성됩니다.

## 테스트

```bash
pytest
```

## CLI 도구

AI 서비스를 위한 명령행 도구가 포함되어 있습니다:

```bash
# AI와 채팅
python -m app.cli chat "안녕하세요"

# 시스템 프롬프트와 함께 채팅
python -m app.cli chat "파이썬 코드 작성해줘" --system "당신은 유능한 프로그래머입니다"

# 워크플로우 목록 조회
python -m app.cli workflow list

# 워크플로우 정보 조회
python -m app.cli workflow info --name workflow_name

# 도구 실행
python -m app.cli tool duckduckgo_search "파이썬 프로그래밍"

# AI 서비스 예제 실행
python -m app.cli examples

# AI 서비스 상태 확인
python -m app.cli status

# 모델 정보 조회
python -m app.cli models
```

FROM python:3.12-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 작업 디렉터리 설정
WORKDIR /flask-gateway

# Poetry 설치
RUN pip install poetry

# Poetry 설정 (가상환경 컨테이너 내부에 생성하지 않게)
RUN poetry config virtualenvs.create false

# pyproject.toml, poetry.lock 복사
COPY pyproject.toml poetry.lock* ./

# 의존성 설치 (여기서 requests, flask, sqlalchemy 등 모두 설치됨)
RUN (poetry check || poetry lock) && poetry install --no-root

# 소스 복사
COPY . .

# Flask 실행 (개발용)
CMD ["python", "app.py"]
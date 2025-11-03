# 빌드 스테이지 (Go 코드를 빌드)
FROM golang:1.25-alpine AS builder

# 작업 디렉토리 설정
WORKDIR /app

# go.mod, go.sum 먼저 복사 후 의존성 다운로드
COPY go.mod go.sum ./
RUN go mod download

# 나머지 소스 코드 복사
COPY . .

# Go 실행 파일 빌드
RUN go build -o main ./cmd/server

# 런타임 스테이지 (최종 실행 이미지)
FROM alpine:latest

WORKDIR /app

# builder에서 빌드된 실행파일만 복사
COPY --from=builder /app/main .

# 컨테이너가 8080 포트 사용
EXPOSE 8080

# 실행 명령
CMD ["./main"]
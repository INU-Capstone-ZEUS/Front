# 1. 베이스 이미지 설정
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /code

# 3. 필요한 패키지 설치 (Chrome 및 의존성 포함)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    ca-certificates \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 4. Google Chrome의 GPG 키 및 리포지토리 추가
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && apt-get install -y google-chrome-stable

# 5. 인증서 파일 복사
COPY ./app/fullchain.pem /etc/ssl/certs/fullchain.pem
COPY ./app/privkey.pem /etc/ssl/private/privkey.pem

# 6. 파이썬 의존성 파일 복사 및 설치
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 7. 애플리케이션 파일 복사
COPY ./app /code/app

# 8. FastAPI에서 사용할 포트 열기
EXPOSE 8080

# 9. FastAPI 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--ssl-keyfile", "/etc/ssl/private/privkey.pem", "--ssl-certfile", "/etc/ssl/certs/fullchain.pem"]

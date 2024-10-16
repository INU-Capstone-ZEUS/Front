import uvicorn
import subprocess
from config.settings import IP_NUM, PORT_NUM
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.root import router as root_router
from routers.crawl_and_analyze import router as crawl_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 요청을 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 (GET, POST, PUT, DELETE 등)를 허용
    allow_headers=["*"],  # 모든 헤더를 허용
)

app.include_router(root_router)
app.include_router(crawl_router)


if __name__ == '__main__':
    command = f"uvicorn main:app --host {IP_NUM} --port {PORT_NUM} --workers 1"
    subprocess.run(command, shell=True)
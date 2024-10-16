from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any
from .crawl_news import crawl_news
from .analyze_news import analyze_news

router = APIRouter()

class CrawlAndAnalyzeRequest(BaseModel):
    company_code: str
    page: int
    company_name: str

@router.post("/crawl_and_analyze")
async def crawl_and_analyze(request: CrawlAndAnalyzeRequest) -> Dict[str, Any]:
    company_code = request.company_code
    page = request.page
    company_name = request.company_name

    # 크롤링 단계
    articles = crawl_news(company_code, page)

    # 분석 단계
    analyzed_articles = analyze_news(articles, company_name)

    # 응답 데이터 생성
    response = {
        "status": "success",
        "total_articles": len(analyzed_articles),
        "analysis": analyzed_articles
    }

    return response

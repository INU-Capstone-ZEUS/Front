import os
import google.generativeai as genai
from dotenv import load_dotenv
import typing_extensions as typing
from fastapi import APIRouter
from typing import Dict, Any, List
import json

class Analysis(typing.TypedDict):
    evaluation: str
    reason: str
    summary: str

router = APIRouter()

def configure_gemini_api():
    load_dotenv()
    GOOGLE_API_KEY = os.getenv('MY_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)


def analyze_article(article_content: str, company_name: str):
    prompt = f"""
    다음의 Article을 바탕으로, 이 기사가 ${company_name} 종목에 대해 긍정적인 평가를 내리고 있는지, 부정적인 평가를 내리고 있는지, 또는 종목과 관련이 없는지 판단해줘. [긍정 / 관련 없음 / 부정] 중 하나의 단어로 평가를 내려주고, 그렇게 판단한 이유는 'reason'에 저장해줘. 또한 이 기사의 종목 관련 중요 내용을 요약해서 'summary'에 저장해줘. 반환 결과는 반드시 JSON 형식이어야 해.

    Article:
    {article_content}

    반환 형식은 아래와 같아:
    Analysis = {{'evaluation': str, reason: str, 'summary': str}}
    Return: Analysis
    """
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content(prompt)
        
        # API에서 반환된 텍스트 정리
        result_text = result.candidates[0].content.parts[0].text
        cleaned_response = result_text.replace("```json", "").replace("```", "").strip()
        
        # JSON 형식으로 변환
        analysis_result = json.loads(cleaned_response)
        
        return analysis_result  # 분석 결과 반환
    
    except Exception as e:
        print(f"Error during analysis: {e}")
        return {
            "evaluation": "Error",
            "reason": "API 요청에 실패했습니다.",
            "summary": "분석 실패"
        }

# 뉴스 기사 분석 함수
def analyze_news(articles: List[Dict[str, str]], company_name: str) -> List[Dict[str, str]]:
    configure_gemini_api()
    analyzed_articles = []

    for article in articles:
        # 각 기사를 분석하여 결과를 추가
        analysis = analyze_article(article['content'], company_name)
        # article['analysis'] = analysis
        analyzed_articles.append(analysis)

    print(analyzed_articles)

    return analyzed_articles
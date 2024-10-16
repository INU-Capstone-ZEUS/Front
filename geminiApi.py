import os
import google.generativeai as genai
from dotenv import load_dotenv
import typing_extensions as typing
import json


with open('005930.json', 'r', encoding='utf-8') as file:
    articles = json.load(file)

company_name = '삼성전자'
# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('MY_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class Analysis(typing.TypedDict):
    evaluation: str
    reason: str
    summary: str

model = genai.GenerativeModel("gemini-1.5-flash")
results = []


def analysis_article(article_content):
    prompt = f"""
    다음의 Article을 바탕으로, 이 기사가 ${company_name} 종목에 대해 긍정적인 평가를 내리고 있는지, 부정적인 평가를 내리고 있는지, 또는 종목과 관련이 없는지 판단해줘. [긍정 / 관련 없음 / 부정] 중 하나의 단어로 평가를 내려주고, 그렇게 판단한 이유는 'reason'에 저장해줘. 또한 이 기사의 종목 관련 중요 내용을 요약해서 'summary'에 저장해줘. 반환 결과는 반드시 JSON 형식이어야 해.

    Article:
    {article_content}

    반환 형식은 아래와 같아:
    Analysis = {{'evaluation': str, reason: str, 'summary': str}}
    Return: Analysis
    """

    result = model.generate_content(prompt)
    result_text = result.candidates[0].content.parts[0].text
    cleaned_response = result_text.replace("```json", "").replace("```", "").strip()
    print(json.loads(cleaned_response))
    results.append(json.loads(cleaned_response))
    

for article in articles:
    analysis_article(article['content'])
    print()
    print()

with open( '005830-분석.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
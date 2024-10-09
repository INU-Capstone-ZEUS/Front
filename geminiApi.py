import os
import google.generativeai as genai
from dotenv import load_dotenv
import typing_extensions as typing
import json

# JSON 파일 읽기
with open('삼성전자기사.json', 'r', encoding='utf-8') as file:
    articles = json.load(file)


# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('MY_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Define the analysis schema
class Analysis(typing.TypedDict):
    evaluation: str
    summary: str

model = genai.GenerativeModel("gemini-1.5-flash")

def analysis_article(article_content):
    # Example article content

    # Define the prompt with the article content
    prompt = f"""
    아래의 Article을 바탕으로, 이 기사가 종목에 대해 어떤 평가를 하고 있는지, [긍정/ 부정] 중 어떤 평가를 내리고 있는지 단어 2개중 하나를 선택해 알려주고, 종목에 대한 중요 내용을 요약해서 요약문 형태로 줘. 전체 결과는 JSON FORMAT으로 줘.

    Article:
    {article_content}

    Use this JSON schema:


    Analysis = {{'evaluation': str, 'summary': str}}
    Return: Analysis
    """

    # Generate content from the model
    result = model.generate_content(prompt)
    result_text = result.candidates[0].content.parts[0].text
    cleaned_response = result_text.replace("```json", "").replace("```", "").strip()
    print(json.loads(cleaned_response))

for article in articles:
    analysis_article(article['content'])
    print()
    print()
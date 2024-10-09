import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('MY_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Configure API settings
API_ENDPOINT = 'https://generativeai.googleapis.com/v1beta2/models/gemini-pro:predict'  # Check this endpoint with the actual API documentation

headers = {
    "Authorization": f"Bearer {GOOGLE_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_news_sentiment_and_summary(articles):
    results = []

    # Iterate through each article
    for article in articles:
        title = article['title']
        content = article['content']
        link = article['link']
        publisher = article['publisher']
        date = article['date']

        response = model.generate_content(["이 기사가 종목에 대해 어떤 평가를 하고 있는지, [긍정/ 부정/ 중립] 중 어떤 평가를 내리고 있는지 알려주고, 종목에 대한 중요 내용을 요약해서 줘. json 형태로 'evaluation'키와 'summary' 키에 벨류값으로 결과를 저장해서 response로 넘겨줘", content])
        for chunk in response:
            results.append(chunk.text)
    
    for result in results:
        print(result)


# Example usage with your articles
articles = [
    # Your article data here
    {
        "title": "삼성전자, '반도체 위기' 현실로?...이례적 사과까지",
        "publisher": "YTN",
        "date": "2024.10.08 18:04",
        "link": "https://n.news.naver.com/mnews/article/052/0002096885",
        "content": "삼성전자 3분기 영업익 9.1조…1년 만에 274.5%↑\n\"10조 원대 하향 조정\"…시장 전망보다도 밑돌아\n'반도체 수장' 전영현, 이례적 사과문 발표[앵커]\n삼성전자가 3분기에 영업이익 9조 원대라는 예상보다 못한 성적을 거뒀습니다.\n\n위기가 현실화하는 것 아니냐는 우려가 나오는 가운데 삼성전자는 전영현 부회장이 이례적인 사과문까지 발표하며 대책을 고심하고 있습니다.\n\n박기완 기자입니다.\n\n[기자]\n지난해 반도체 불황기와 비교한 삼성전자 3분기 실적은 겉보기에는 호조세를 이어갔습니다.\n\n영업이익은 9조천억 원, 1년 전보다 4배 가까이 늘었고,\n\n매출액은 분기 사상 최대 기록을 2년 반 만에 갈아치웠습니다.\n\n하지만 시장의 기대에는 미치지 못했습니다.\n\n10조 원대로 대폭 하향 조정된 증권가의 예상 영업이익마저 크게 밑돌았기 때문입니다.\n\n삼성전자는 스마트폰 재고 조정에 따른 메모리 반도체 수요 감소와,\n\n중국 업체의 추격, 그리고 엔비디아의 HBM 품질 검증 결과 지연 등을 실적 부진의 이유로 꼽았습니다.\n\n그나마 전날 장중 5만 원대까지 떨어졌던 주가는 6만 원을 사수했습니다.\n\n전 거래일 대비 1.15% 줄어든 60,300원으로 마감했습니다.\n\n반도체 부문의 수장인 전영현 부회장은 실적 발표 직후 이례적인 사과문을 발표하며 우려를 불식시키는 데 초점을 맞췄습니다.\n\n기대에 미치지 못하는 성과로 걱정을 끼쳐 송구하다면서,\n\n경영진이 앞장서 세상에 없는 새로운 기술, 품질 경쟁력으로 재도약하겠다고 말했습니다.\n\n앞서 이재용 회장 역시 출장으로 찾은 필리핀에서 파운드리 사업부를 분사하지 않겠다고 밝혔습니다.\n\n이 회장의 발언을 두고 업계 1위 TSMC와의 격차가 좁혀지지 않는 가운데 정면 돌파를 택했다는 분석이 나옵니다.\n\n삼성전자의 위기론이 현실화했다는 우려 속에, 이재용 회장과 경영진이 위기 타파를 위해 어떤 대책을 내놓을지 주목됩니다.\n\nYTN 박기완입니다.\n\n촬영기자 : 홍성노 \n디자인 : 임샛별\n\n※ '당신의 제보가 뉴스가 됩니다'\n[카카오톡] YTN 검색해 채널 추가\n[전화] 02-398-8585\n[메일] social@ytn.co.kr"
    },
    {
        "title": "위기의 삼성, 이재용의 '新프랑크푸르트 선언'은 언제?",
        "publisher": "TV조선",
        "date": "2024.10.08 21:22",
        "link": "https://n.news.naver.com/mnews/article/448/0000481786",
        "content": "[앵커]\n보신 것처럼 삼성전자의 상황이 좋지 않습니다. 원인은 무엇이고 반등의 계기를 마련할 수 있을지 산업부 장혁수 기자와 자세히 얘기 나눠보겠습니다.\n\n장 기자, 오늘 실적 발표 전부터 삼성이 상황이 좋지 않다, 이런 얘기가 많이 나왔어요.\n\n[기자]\n네, 삼성전자가 처한 상황은 주가 흐름으로도 알 수 있습니다. 7월까지만 해도 9만원에 근접했던 주가는 외국인들이 계속 팔면서 이제 '5만 전자'를 눈앞에 뒀습니다. 외국계 증권사들도 삼성전자에 대해 부정적인 목소리를 내고 있습니다. 대표적으로 호주의 글로벌 증권사인 맥쿼리는 삼성전자를 '병약한 반도체 거인'이라고 표현하며 목표주가를 무려 절반으로 낮췄습니다.\n\n[앵커]\n가장 큰 문제는 주력 사업인 반도체 사업이라고 하는데, 그 중에서도 '파운드리' 분야의 부진이 심각한 것 같습니다.\n\n[기자]\n네, 삼성전자는 반도체를 위탁생산하는 파운드리 부문 최강자인 대만 TSMC를 따라잡겠다며 대규모 투자를 감행했습니다. 하지만 기술력이나 수율이 기대에 못미치면서 TSMC를 따라잡기는 커녕 매년 수조원의 적자를 내고 있습니다. 이 때문에 파운드리를 분사해야 하는 것 아니냐는 얘기까지 나오고 있는데 필리핀 생산 법인을 찾아 현장경영 중인 이재용 회장은 로이터통신과의 인터뷰에서 \"파운드리를 분사할 생각은 없다\" \"우리는 사업 성장을 갈망하고 있다\"고 선을 그었습니다.\n\n[앵커]\n사실 \"삼성이 예전같지 않다\"는 얘기가 나온 건 어제 오늘 일이 아니잖아요? 원인은 뭐라고 봐야 합니까?\n\n[기자]\n네, 2년 전 갤럭시 GOS 성능조작 사건과 최근 버즈3 불량품 논란 등이 불거졌을 때도 기술을 최고로 치는 예전의 삼성 같았으면 있을 수 없는 일이라는 말이 많았는데요, 원인은 여러가지가 있겠지만 7년째 이어진 TF 체제에서 원인을 찾는 분석도 있습니다. 국정농단 사태 이후 삼성은 미래전략실을 해체하고 사업지원 TF가 사실상 그룹의 컨트롤 역할을 하고 있는데, 이 TF는 재무통인 정현호 부회장이 이끌고 있습니다. 그러다 보니 기술개발이나 인수합병, 핵심인재 영입 등을 통해 초격차를 유지하기보다 비용 절감에 초점을 맞추는 분위기가 됐다는 겁니다. 실제로 삼성은 지난 2017년 하만 이후 거대 인수합병을 한 건도 해내지 못했습니다.\n\n[앵커]\n삼성도 이런 상황을 잘 알고 있을텐데, 어떤 대책을 내놓고 있습니까?\n\n[기자]\n일단은 비용 절감에 나서고 있습니다. 인도 등 해외 법인에서 최대 30%까지 인력 감축에 나섰고, 국내에서도 임직원들의 출장을 줄이고 소모품을 절약하는 등 비용을 절감하란 공지도 내려왔다고 합니다. 하지만 빡빡한 사내 분위기에 지친 젊은 직원들이 SK하이닉스 경력 채용에 대거 몰리면서 사내 분위기는 좋지 않은 상황입니다.\n\n[앵커]\n삼성의 혁신하면 고 이건희 회장이 \"마누라와 자식 빼고 다 바꾸라\"고 지시한 '프랑크푸르트 선언'이나 불량 핸드폰을 수거해 모두 불태운 '애니콜 화형식'이 떠오르는데, 이재용 회장에게도 선대 회장이 보여준 과감한 결단이 필요해 보입니다. 장 기자 잘 들었습니다."
    }
]

analyze_news_sentiment_and_summary(articles)


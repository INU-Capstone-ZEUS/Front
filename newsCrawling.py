from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

# 크롬 드라이버 실행
driver = webdriver.Chrome()

# Naver 증권 뉴스 페이지 url
company_name = '삼성전자'
company_code = "005930"
page = 1 # 1 ~ 200 페이지까지 확인 가능 

url = 'https://finance.naver.com/item/news.naver?code=' + str(company_code) + '&page=' + str(page) 
driver.get(url)

# 페이지가 완전히 로딩되도록 대기 - 최대 10초 대기
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'news_frame')))
except:
    print("페이지 로딩 실패")
    driver.quit()

# iframe으로 전환 (iframe의 name 또는 id로 전환 가능)
driver.switch_to.frame('news_frame')
sorce_code = driver.page_source

#html = BeautifulSoup(source_code, "lxml")
html = BeautifulSoup(sorce_code,"html.parser")

for tr in html.select('tr.relation_lst '):
    tr.decompose()

# 기사 item의 신문사 / 날짜 / 뉴스 주소 갖고 오기
infos = html.select('.info')
dates = html.select('.date')
aTags = html.select('td.title a')
links = []
articles = []

# a 태그에서 href를 갖고 와야 주소임
for a in aTags:
    href = a.attrs['href']
    links.append(href)




# 추출한 href 링크에 대해 반복
for i in range(len(links)):
    full_url = links[i]

    # Selenium을 사용해 새 페이지로 이동
    driver.get(full_url)

    # 페이지 로딩 대기
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article')))
    except:
        print("페이지 로딩 실패")
        continue

    # 새로운 페이지 소스를 BeautifulSoup으로 파싱
    new_page_source = driver.page_source
    soup = BeautifulSoup(new_page_source, 'html.parser')

    # 영상 제거
    for div in soup.select('div.vod_player_wrap._VIDEO_AREA_WRAP'):
        div.decompose()  # 해당 div를 삭제

    for div in soup.select('div.artical-btm'):
        div.decompose()

    # for script in soup.select('_VOD_IMAGE_REPLACE_TEMPLATE'):
    #     script.decompose()
    #     print('----------스크립트 제거!!!!!!!!----------')

    # br 태그는 줄바꿈으로 변환
    for br in soup.find_all("br"):
        br.replace_with("\n")

    # 기사 추출
    article_content = soup.select_one('article').text.strip()

    # 기사 제목 추출
    article_title = soup.select_one('#title_area span').text.strip()

    # 출력 또는 저장
    print(article_title)
    print(article_content)
    print()

    article = {
        'title' : article_title,
        'publisher' : infos[i].text.strip(),
        'date' : dates[i].text.strip(),
        'link' : full_url,
        'content' : article_content,
    }

    # 리스트에 기사 추가
    articles.append(article)

with open( str(company_code) + '.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)

driver.quit()
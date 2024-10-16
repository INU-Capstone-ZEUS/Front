from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Dict, Any

# 크롤링 요청 데이터 모델
class CrawlRequest(BaseModel):
    company_code: str
    page: int

# 라우터 설정
router = APIRouter()

# Selenium 설정 함수
def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def crawl_news(company_code: str, page: int) -> List[Dict[str, str]]:

    # URL / 요청 헤더 설정
    url = f'https://finance.naver.com/item/news.naver?code={company_code}&page={page}'

    driver = get_browser()
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'news_frame')))
    driver.switch_to.frame('news_frame')

    source_code = driver.page_source
    html = BeautifulSoup(source_code, "html.parser")

    # 중복 뉴스 제거
    for tr in html.select('tr.relation_lst'):
        tr.decompose()

    # 기사 item의 신문사 / 날짜 / 뉴스 주소 갖고 오기
    infos = html.select('.info')
    dates = html.select('.date')
    aTags = html.select('td.title a')
    links = []
    articles = []

    # a 태그에서 href를 추출하여 주소 수집
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

        # br 태그는 줄바꿈으로 변환
        for br in soup.find_all("br"):
            br.replace_with("\n")

        # 기사 추출
        article_content = soup.select_one('article').text.strip()

        # 기사 제목 추출
        article_title = soup.select_one('#title_area span').text.strip()

        article = {
            'title': article_title,
            'publisher': infos[i].text.strip() if i < len(infos) else 'Unknown',
            'date': dates[i].text.strip() if i < len(dates) else 'Unknown',
            'link': full_url,
            'content': article_content,
        }

        # 리스트에 기사 추가
        articles.append(article)

    # 모든 크롤링 작업이 끝난 후 브라우저 종료
    driver.quit()

    return articles

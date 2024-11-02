import React, { useState, useEffect } from 'react';
import './news.css';
import NewsPostItem from './NewsPostItem';
import CardFilter from './CardFilter';

function News() {
    const [news, setNews] = useState([]);
    const [filter, setFilter] = useState('Today');
    const [selectedButton, setSelectedButton] = useState('');

    const handleFilterChange = (filter) => {
        setFilter(filter);
    };

    const handleClick = (buttonName) => {
        setSelectedButton(buttonName);
        console.log(buttonName);
    };

    const fetchData = () => {
        fetch('http://18.117.81.202/crawl-and-analyze', {
            method: 'POST', // POST 메서드 사용
            headers: {
                'Content-Type': 'application/json', // JSON 데이터임을 명시
            },
            body: JSON.stringify({
                company_code: '005180',
                page: 1,
                company_name: '빙그레',
            }), // 전송할 데이터
        })
            .then((res) => res.json())
            .then((data) => {
                setNews(data); // 응답 데이터를 처리
            })
            .catch((e) => console.log(e.message)); // 에러 처리
    };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div className="card">
            <div className="card-header d-flex justify-content-between align-items-center">
                <h5 className="card-title mb-0">
                    뉴스 &amp; 평가 <span>| {filter}</span>
                </h5>
                <div className="btn-group" role="group" aria-label="Basic example">
                    <button type="button" className="btn btn-success" onClick={() => handleClick('긍정')}>
                        긍정
                    </button>
                    <button type="button" className="btn btn-danger" onClick={() => handleClick('부정')}>
                        부정
                    </button>
                </div>
            </div>

            <div className="card-body pb-0">
                <div className="news">
                    {news['analysis'] && news['status'] === 'success' && news['analysis'].length > 0
                        ? news['analysis'].map((item, idx) => <NewsPostItem key={idx} item={item} />)
                        : null}
                </div>
            </div>
        </div>
    );
}

export default News;

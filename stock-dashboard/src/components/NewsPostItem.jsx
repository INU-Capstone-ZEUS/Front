import React from 'react'

function NewsPostItem({item}) {
    console.log(item.link); // 링크 값 확인
    return (
        <div className="post-item clearfix">
            <img src={item.img} alt=""/>
            <h4>
                <a href={item.link}>{item.title}</a>
            </h4>
            <p>{item.subtitle}...</p>
        </div>
    )
}

export default NewsPostItem
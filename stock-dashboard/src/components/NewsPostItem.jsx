import React from 'react'

function NewsPostItem({item}) {
    return (
        <div className="post-item clearfix">
            <img src={item.img} alt=""/>
            <h4>
                <a href={item.link}>{item.evaluation}</a>
            </h4>
            <p>{item.reason}...</p>
        </div>
    )
}

export default NewsPostItem
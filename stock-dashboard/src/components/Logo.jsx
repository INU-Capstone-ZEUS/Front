import React from 'react'
import './logo.css'

export default function Logo() {

    const handleToggleSideBar = () => {
        document.body.classList.toggle('toggle-sidebar');
    };

    return (
        <div className='d-flex align-items-center justify-content-between'>
            <a href="/" className='logo d-flex align-items-center'>
                {/* 로고 이미지 */}
                <img src="logo_light.png"alt="logo"/>
                <span className="d-none d-lg-block">zeus</span>
            </a>
            <i
                // 메뉴 아이콘
                className='bi bi-list toggle-sidebar-btn' 
                onClick={handleToggleSideBar}
            >
            </i>
        </div>
    )
}

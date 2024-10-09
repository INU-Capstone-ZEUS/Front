import { useState} from "react";
import styled from "styled-components";
import { HiBell, HiBookmark, HiChat, HiChartBar } from "react-icons/hi"; // 아이콘 임포트
import { IoMdNotificationsOutline } from "react-icons/io";
import { AiOutlineUser } from "react-icons/ai";
import { MdOutlineBookmarkBorder } from "react-icons/md";
import { IoChatboxSharp } from "react-icons/io5";
import { MdOutlineChatBubbleOutline } from "react-icons/md";
import { BsBarChartFill } from "react-icons/bs";
import { useTheme } from "../../context/themeProvider";

import ThemeToggle from "./ThemeToggle";

// Styled components for the sidebar
const SidebarContainer = styled.div`
  display: flex;  
  flex-direction: column;
  align-items: center;
  background-color: #f8ebf0; // 핑크색 배경
  background-color: ${props => props.theme.sidebarBg}; // 테마에 따른 배경색 적용
  height: 100vh;
  padding: 20px 0;
  width: 80px;
  position: fixed;
  top: 0px;
  left: 0;
  z-index: 90;
  padding-top: 60px;
`;

const IconWrapper = styled.div`
  margin: 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
`;

const IconText = styled.span`
  font-size: 12px;
  margin-top: 5px;
  color: #333;
  text-align: center;
`;

const ModeSwitch = styled.div`
  margin-top: auto;
  padding-bottom: 20px;
  text-align: center;
  font-size: 12px;
  color: #333;
  cursor: pointer;
`;

export default function CustomSidebar() {
  const [ThemeMode, toggleTheme] = useTheme();

  return (
    <SidebarContainer>
      {/* User Icon */}
      <IconWrapper>
        <AiOutlineUser size={30} style={{ background: 'white', color: '#4949F', borderRadius: '50px', paddingTop: '5px'}}/>
      </IconWrapper>

      {/* Bell Icon */}
      <IconWrapper>
        <IoMdNotificationsOutline size={30} style={{color: '#4949F'}}/>
      </IconWrapper>

      {/* Bookmark Icon */}
      <IconWrapper>
        <MdOutlineBookmarkBorder size={30} style={{color: '#4949F'}}/>
      </IconWrapper>

      {/* Chat Icon */}
      <IconWrapper>
        <MdOutlineChatBubbleOutline size={25} style={{color: '#4949F'}}/>
      </IconWrapper>

      {/* Chart Icon */}
      <IconWrapper>
        <BsBarChartFill size={25} style={{color: '#4949F'}}/>
      </IconWrapper>

      <ThemeToggle toggle={toggleTheme} mode={ThemeMode}>
        DarkMode
      </ThemeToggle>
    </SidebarContainer>
  );
}


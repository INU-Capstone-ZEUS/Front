import logo from './logo.svg';
import './App.css';
import Header from './Components/Header/Header';
import CustomSidebar from './Components/Sidebar/CustomSidebar';
import { darkTheme, lightTheme } from './styles/theme';
//import {ThemeContext, ThemeProvider} from 'styled-components'

import { ThemeProvider } from './context/themeProvider';

import React, {useState} from 'react';
import { GlobalStyle } from './styles/globalStyles';
import { Helmet } from "react-helmet"

function App (){

  return (
      <ThemeProvider>
        <GlobalStyle />
        {/* 부모 div로 레이아웃 감싸기 */}
        <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh'}}>
          <Header />

          <div style={{ display: 'flex', flexGrow: 1, paddingTop: '60px'}}>
            {/* 메인 콘텐츠 */}
            <div style={{ flexGrow: 1, padding: '20px', position: 'relative' }}>
              <CustomSidebar />
              {/* 여기에 메인 콘텐츠 삽입 */}
            </div>
          </div>
        </div>
      </ThemeProvider>
  );
}

export default App;

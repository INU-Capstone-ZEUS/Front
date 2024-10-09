import { lightTheme, darkTheme } from '../theme/theme';
import { createContext, useState, useContext, useCallback } from 'react';
import { ThemeProvider as StyledProvider } from 'styled-components';
import { useMemo } from 'react';


const ThemeContext = createContext({});


const ThemeProvider = ({ children }) => {
  const [ThemeMode, setThemeMode] = useState('light'); // 초기 값 'light'
  
  // 현재 테마 모드에 따른 테마 객체 결정
  const themeObject = useMemo(() => {
    return ThemeMode === 'light' ? lightTheme : darkTheme;
  }, [ThemeMode]);

  return (
    // 컨텍스트로 테마 모드와 테마 변경 함수를 전달
    <ThemeContext.Provider value={{ ThemeMode, setThemeMode }}>
      {/* styled-components의 ThemeProvider로 하위 컴포넌트 감싸기 */}
      <StyledProvider theme={themeObject}>
        {children}
      </StyledProvider>
    </ThemeContext.Provider>
  );
};
function useTheme() {
    const context = useContext(ThemeContext);
    
    if (!context) {
      throw new Error('useTheme must be used within a ThemeProvider');
    }
    const { ThemeMode, setThemeMode } = context;
  
    const toggleTheme = useCallback(() => {
      setThemeMode(prevMode => prevMode === 'light' ? 'dark' : 'light');
    }, [setThemeMode]);
  
    return [ThemeMode, toggleTheme];
}

export { ThemeProvider, useTheme };

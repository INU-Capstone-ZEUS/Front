import styled from 'styled-components';
import { useTheme } from '../../context/themeProvider'; // 테마 사용

export default function Header() {
  const [theme] = useTheme(); // 테마 가져오기

  return (
    <HeaderContainer>
      <Logo>
        <img src={theme === 'light' ? 'logo_light.png' : 'logo_dark.png'} alt="Logo" />
      </Logo>
      <Navbar>
        <ul>
          <li><a href="#">News</a></li>
          <li><a href="#">Chart</a></li>
          <li><a href="#">검색기</a></li>
        </ul>
      </Navbar>
      <AuthButtons>
        <button className="sign-in">Sign in</button>
        <button className="register">Register</button>
      </AuthButtons>
    </HeaderContainer>
  );
}

const HeaderContainer = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 30px;
  background-color: ${
    (props) => props.theme.headerBg}; /* 테마에 따른 배경색 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;  
`;

const Logo = styled.div`
  img {
    height: 30px;
  }
`;

const Navbar = styled.nav`
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding-right: 20px;
  flex-grow: 1; /* 남은 공간을 차지하게 만듦 */

  ul {
    display: flex;
    align-items: center;
    list-style-type: none;
    margin: 0;
    padding: 0;
    justify-content: flex-end; /* 아이템들을 오른쪽으로 정렬 */
    
    li {
      margin: 0 15px;
      
      a {
        text-decoration: none;
        color: ${(props) => props.theme.text}; /* 테마에 따른 텍스트 색상 */
        font-weight: 500;
      }
    }
  }
`;

const AuthButtons = styled.div`
  display: flex;
  margin-left: 10px;
  margin-right: 50px;

  button {
    margin-left: 10px;
    padding: 5px 15px;
    border: 1px solid ${(props) => props.theme.text}; /* 테마에 따른 테두리 색상 */
    background-color: ${(props) => props.theme.bg}; /* 테마에 따른 배경색 */
    cursor: pointer;
    font-weight: 600;
    border-radius: 5px;
    color: ${(props) => props.theme.text}; /* 테마에 따른 텍스트 색상 */
  }

  .register {
    background-color: ${(props) => props.theme.primary}; /* 테마에 따른 기본 색상 */
    color: #fff;
  }
`;

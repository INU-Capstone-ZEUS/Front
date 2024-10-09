import './Header.css';
//import { IoIosArrowDown, IoIosArrowUp } from "react-icons/io";

export default function Header() {
  return (
    <header>
      <div className="logo">
        <img src="logo.png" alt="Logo" />
      </div>
      <nav className="navbar">
        <ul>
          <li><a href="#">News</a></li>
          <li><a href="#">Chart</a></li>
          <li><a href="#">검색기</a></li>
        </ul>
      </nav>
      <div className="auth-buttons">
        <button className="sign-in">Sign in</button>
        <button className="register">Register</button>
      </div>
    </header>
  );
}

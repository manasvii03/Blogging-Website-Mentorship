import logo from "../assets/logo.svg";
import penLeft from "../assets/penleft.png";
import penRight from "../assets/penright.png";
import "./AuthBox.css";

function AuthBox({ tab, setTab }) {
  return (
    <div className="card">

      <div className="brand">
        <img src={logo} alt="logo" className="logo" />
        <h1 className="title">
          <span className="simply">SIMPLY</span>
          <span className="said">SAID</span>
        </h1>
      </div>

      <p className="subtitle">WHERE WORDS COME TO LIFE</p>

      <div className="tabs">
        <span
          className={tab === "login" ? "active" : ""}
          onClick={() => setTab("login")}
        >
          Login
        </span>
        <span
          className={tab === "signup" ? "active" : ""}
          onClick={() => setTab("signup")}
        >
          Sign Up
        </span>
      </div>

      <div className="form-area">
        <img src={penLeft} alt="pen" className="pen left" />

        <div className="form">
          <label>
            {tab === "signup" ? "Create a Username:" : "Username:"}
          </label>
          <input type="text" />

          <label>
            {tab === "signup" ? "Create a Password:" : "Password:"}
          </label>
          <input type="password" />

          <button>Let's Get Started</button>
        </div>

        <img src={penRight} alt="pen" className="pen right" />
      </div>

    </div>
  );
}

export default AuthBox;

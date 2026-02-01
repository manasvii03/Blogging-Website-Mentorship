import { useState } from "react";
import logo from "../assets/logo.svg";
import penLeft from "../assets/penleft.png";
import penRight from "../assets/penright.png";
import "./AuthBox.css";
import api from "../api";

function AuthBox({ tab, setTab }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async () => {
    try {
      if (tab === "signup") {
        await api.post("signup/", { username, password });
        setMessage("Signup successful! Now login.");
        setTab("login");
      } else {
        const res = await api.post("login/", { username, password });
        localStorage.setItem("token_"+Date.now(), res.data.token);
        setMessage("Login successful!");
      }
    } catch (err) {
      console.log(err.response?.data);
      setMessage(JSON.stringify(err.response?.data));
    }
  };



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
            {tab === "signup" ? "Create Username:" : "Username:"}
          </label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <label>
            {tab === "signup" ? "Create Password:" : "Password:"}
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button onClick={handleSubmit}>Let's Get Started</button>

          {message && (
            <div style ={{ width:"100%",display:"flex",justifyContent:"center"}}>
            <p style={{ 
              color: "black", 
              fontWeight: "bold",
              fontSize:"48px",
              textAlign:"center",
             }}>{message}
              </p>
             </div>
          )}
        </div>

        <img src={penRight} alt="pen" className="pen right" />
      </div>
    </div>
  );
}

export default AuthBox;
import { useState } from "react";
import logo from "../assets/logo.svg";
import penLeft from "../assets/penleft.png";
import penRight from "../assets/penright.png";
import "./AuthBox.css";
import axios from "axios";

const AuthBox=({ tab, setTab })=> {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    const url =
      tab === "login"
        ? "http://127.0.0.1:8000/api/login/"
        : "http://127.0.0.1:8000/api/signup/";

    axios
      .post(url, {
        username: username,
        password: password,
      })
      .then((response) => {
        if (response.data.message){
          setMessage(response.data.message);
        } else {
        setMessage(
          tab === "login" ? "Login Successful" : "Signup Successful"
        );}

        if (tab === "login") {
          localStorage.setItem("token", response.data.token);
        }
      })
      .catch((error) => {
        setMessage("Something went wrong");
      });
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
            {tab === "signup" ? "Create a Username:" : "Username:"}
          </label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <label>
            {tab === "signup" ? "Create a Password:" : "Password:"}
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button onClick={handleSubmit}>Let's Get Started</button>

          {message && <p style={{ color: "white" }}>{message}</p>}
        </div>

        <img src={penRight} alt="pen" className="pen right" />
      </div>
    </div>
  );
}

export default AuthBox;
import { useState } from "react";
import AuthBox from "./components/Authbox";
import "./App.css";

function App() {
  const [tab, setTab] = useState("signup");

  return (
    <div className="page">
      <AuthBox tab={tab} setTab={setTab} />
    </div>
  );
}

export default App;

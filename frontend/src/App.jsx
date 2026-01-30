import { useState } from "react";
import AuthBox from "./components/Authbox";

function App() {
  const [tab, setTab] = useState("signup");

  return (
      <AuthBox tab={tab} setTab={setTab} />
  );
}

export default App;


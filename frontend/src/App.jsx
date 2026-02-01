// import Homepage from '../homepage/homepage.jsx';
// function App(){
//   return(
//     <Homepage/>
//   );
// }
// export default App;

import { useState } from "react";
import AuthBox from "./components/AuthBox";

function App() {
  const [tab, setTab] = useState("signup");

  return (
      <AuthBox tab={tab} setTab={setTab} />
  );
}

export default App;


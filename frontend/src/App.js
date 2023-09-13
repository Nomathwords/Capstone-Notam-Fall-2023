import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import About from "./components/About";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />}></Route>
      <Route path="about" element={<About />}></Route>
    </Routes>
  );
}

export default App;

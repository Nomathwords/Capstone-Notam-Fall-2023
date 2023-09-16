import { Route, Routes } from "react-router-dom";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./components/Theme";
import Home from "./components/Home";
import About from "./components/About";
import Header from "./components/Header";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Routes>
        <Route path="/" element={<Header />}></Route>
        <Route path="about" element={<About />}></Route>
      </Routes>
    </ThemeProvider>
  );
}

export default App;

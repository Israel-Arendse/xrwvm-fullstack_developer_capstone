import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />,
      <Route path="/registration" element={<RegistrationPanel />} />
    </Routes>
  );
}
export default App;

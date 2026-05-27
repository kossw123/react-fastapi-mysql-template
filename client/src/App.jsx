import { Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import ProductPage from "./pages/ProductPage";
import SignUpPage from "./pages/SignUpPage";
function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route path="/productpage" element={<ProductPage />} />
      <Route path="/SignupPage" element={<SignUpPage />} />
    </Routes>
  );
}

export default App;

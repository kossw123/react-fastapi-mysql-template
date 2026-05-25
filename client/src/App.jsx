import { Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import ProductPage from "./pages/ProductPage";
import NotFoundPage from "./pages/NotFoundPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />

      <Route path="/products" element={<ProductPage />} />

      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}

export default App;

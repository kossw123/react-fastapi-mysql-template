import { Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import ProductManagementPage from "./pages/ProductManagementPage";
import SignUpPage from "./pages/SignUpPage";
import KioskPage from "./pages/KioskPage";
import PaymentPage from "./pages/PaymentPage";

import ProtectedRoute from "./routes/ProtectedRoute";

import PaymentSuccessPage from "./pages/PaymentSuccessPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />

      <Route element={<ProtectedRoute />}>
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route
          path="/productmanagementpage"
          element={<ProductManagementPage />}
        />
        <Route path="/paymentpage" element={<PaymentPage />} />
        <Route path="/signuppage" element={<SignUpPage />} />
        <Route path="/kioskpage" element={<KioskPage />} />
        <Route path="/payment/success" element={<PaymentSuccessPage />} />
      </Route>
    </Routes>
  );
}

export default App;

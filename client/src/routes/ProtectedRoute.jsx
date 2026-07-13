import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import useAuthStore from "../zustand_store/AuthStore";

const ProtectedRoute = () => {
  const isAuthenciated = useAuthStore((state) => state.isAuthenciated);

  if (isAuthenciated == false) {
    alert("Error!!");
    return <Navigate to="/" replace />;
  }

  return <Outlet />;
};

export default ProtectedRoute;

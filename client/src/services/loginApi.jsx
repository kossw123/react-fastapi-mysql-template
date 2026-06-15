// import axios from "axios";
import axiosinstance from "./axiosInstance";

// const API = "http://localhost:8000/auth";

export const login = async (username, password) => {
  const res = await axiosinstance.post("/auth/login", {
    username: username,
    password: password,
  });
  return res.data;
};

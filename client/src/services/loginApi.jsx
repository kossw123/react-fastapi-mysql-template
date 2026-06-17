import axiosinstance from "./axiosInstance";

export const login = async (username, password) => {
  const res = await axiosinstance.post("/auth/login", {
    username: username,
    password: password,
  });
  return res.data;
};

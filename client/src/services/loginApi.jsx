import axiosinstance from "./axiosInstance";

export const login = async (username, password) => {
  console.log("[클라이언트] loginApi.jsx, login() 요청 함수 진입");

  const res = await axiosinstance.post("/auth/login", {
    username: username,
    password: password,
  });
  console.log("[클라이언트] loginApi.jsx, 결과 반환");
  return res.data;
};

export const logout = async (token) => {
  const res = await axiosinstance.post("/auth/logout", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

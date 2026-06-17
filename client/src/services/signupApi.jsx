import axiosinstance from "./axiosInstance";

export const signup = async (username, email, password) => {
  return await axiosinstance
    .post(`/signup`, {
      username: username,
      email: email,
      password: password,
    })
    .then((res) => {
      console.log(
        `[FRONTEND signupAPI.signup]id: ${res.usename}, email: ${res.email}, password: ${res.password}`,
      );
      return res.status;
    });
};

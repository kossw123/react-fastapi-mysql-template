import axios from "axios";

const API = "http://localhost:8000/auth";

export const signup = async (username, email, password) => {
  return await axios
    .post(`${API}/signup`, {
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

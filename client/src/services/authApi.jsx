import axios from "axios";

const API = "http://localhost:8000/auth";

export const login = async (username, password) => {
  const res = await axios.post(`${API}/login`, {
    username: username,
    password: password,
  });
  return res.data;
};

export const get_current_user = async (username) => {
    const res = await axios.post(`${API}/getuser`, { 
      username: username
  });

  return res.data;
};

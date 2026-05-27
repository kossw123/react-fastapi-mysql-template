import axios from "axios";

const API = "http://localhost:8000";

export const login = async () => {
  const res = await axios.post(`${API}/login`);
  return res.data;
};

export const signup = async (id, password) => {
    const res = axios.post(`${API}/signup`, {
        id,
        password
    });

    return res.data
}


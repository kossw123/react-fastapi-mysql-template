import axios from "axios";

const API = "http://localhost:8000/order";

export const ordering = async (items) => {
  const res = await axios.post(`${API}/ordering`, {
    items: items,
  });

  return res.data;
};
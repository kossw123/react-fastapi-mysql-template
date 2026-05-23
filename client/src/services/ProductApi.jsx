import axios from "axios";

const API = "http://localhost:8000";

export const getProducts = async () => {
  const res = await axios.get(`${API}/products`);
  return res.data;
};

export const createProduct = async (name, price, status) => {
  const res = await axios.post(`${API}/products`, {
    name,
    price,
    status,
  });
  return res.data;
};

export const deleteProduct = async (productId) => {
  const res = await axios.delete(`${API}/products/${productId}`);


  return res.data;
};

export const updateProduct = async (productId, updatedData) => {
  const res = await axios.put(`${API}/products/${productId}`, updatedData);
  
  return res.data;
};
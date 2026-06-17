import axiosinstance from "./axiosInstance";


export const getProducts = async () => {
  const res = await axiosinstance.get(`/products`);
  return res.data;
};

export const createProduct = async (name, price, status) => {
  const res = await axiosinstance.post(`/products`, {
    name,
    price,
    status,
  });
  return res.data;
};

export const deleteProduct = async (productId) => {
  const res = await axiosinstance.delete(`/products/${productId}`);
  return res.data;
};

export const updateProduct = async (productId, updatedData) => {
  const res = await axiosinstance.put(`/products/${productId}`, updatedData);
  return res.data;
};

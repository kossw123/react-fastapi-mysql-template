import axiosinstance from "./axiosInstance";

export const ordering = async (items) => {
  const res = await axiosinstance.post(`/ordering`, {
    items: items,
  });

  return res.data;
};

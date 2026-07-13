import axiosinstance from "./axiosInstance";

export const get_current_user = async (username) => {
  const res = await axiosinstance(`/getuser`, {
    username: username,
  });

  return res.data;
};

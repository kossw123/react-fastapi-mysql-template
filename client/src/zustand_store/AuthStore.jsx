import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

const useAuthStore = create(
  persist(
    (set) => ({
      username: "",
      token: null,
      isAuthenticated: false,

      login: (username, token) =>
        set({
          username: username,
          token: token,
          isAuthenticated: true,
        }),

      logout: () =>
        set({
          username: "",
          token: null,
          isAuthenticated: false,
        }),
    }),
    {
      name: "auth-storage",
      storage: createJSONStorage(() => sessionStorage),
    },
  ),
);

export default useAuthStore;

import { create } from "zustand";

const useOrderStore = create((set) => ({
  order_id: null,
  customer_id: null,
  items: [],

  setOrder: (order) =>
    set({
      order_id: order.order_id,
      customer_id: order.customer_id,
      items: order.items,
    }),

  clearOrder: () =>
    set({
      order_id: null,
      customer_id: null,
      items: [],
    }),
}));

export default useOrderStore;

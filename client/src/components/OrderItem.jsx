function OrderItem({ item, onIncrease, onDecrease }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "12px",
      }}
    >
      <div>
        <div>{item.name}</div>

        <div>{(item.price * item.quantity).toLocaleString()}원</div>
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "8px",
        }}
      >
        <button onClick={() => onDecrease(item.id)}>-</button>

        <span>{item.quantity}</span>

        <button onClick={() => onIncrease(item.id)}>+</button>
      </div>
    </div>
  );
}

export default OrderItem;

import OrderItem from "./OrderItem";

import {
  PanelContainer,
  PanelTitle,
  EmptyMessage,
  Divider,
  Summary,
  OrderSubmitButton,
} from "./styles/OrderPanelStyle";

function OrderPanel({ orderItems, onIncrease, onDecrease, onSubmitOrder }) {
  const totalQuantity = orderItems.reduce(
    (sum, item) => sum + item.quantity,
    0,
  );

  const totalPrice = orderItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0,
  );

  return (
    <PanelContainer>
      <PanelTitle>주문 내역</PanelTitle>

      {orderItems.length === 0 ? (
        <EmptyMessage>선택된 상품이 없습니다.</EmptyMessage>
      ) : (
        orderItems.map((item) => (
          <OrderItem
            key={item.id}
            item={item}
            onIncrease={onIncrease}
            onDecrease={onDecrease}
          />
        ))
      )}

      <Divider />

      <Summary>
        <span>총 수량 {totalQuantity}개</span>

        <span>{totalPrice.toLocaleString()}원</span>
      </Summary>

      <OrderSubmitButton onClick={onSubmitOrder}>주문하기</OrderSubmitButton>
    </PanelContainer>
  );
}

export default OrderPanel;

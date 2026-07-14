import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  Page,
  Container,
  Title,
  SectionTitle,
  PaymentGrid,
  PaymentButton,
  PointContainer,
  RadioGroup,
  RadioLabel,
  PhoneInput,
  ButtonContainer,
  BackButton,
  PayButton,
  OrderSummary,
  SummaryTitle,
  OrderItem,
  ItemName,
  ItemInfo,
  ItemQuantity,
  ItemPrice,
  TotalSection,
} from "./styles/PaymentPageStyle";
import useOrderStore from "../zustand_store/OrderStore";
import useAuthStore from "../zustand_store/AuthStore";
import { logout } from "../services/loginApi";

import { loadTossPayments } from "@tosspayments/payment-sdk";

const clientKey = import.meta.env.VITE_TOSS_CLIENT_KEY;

function PaymentPage() {
  const navigate = useNavigate();
  const logoutAction = useAuthStore((state) => state.logout);
  const [paymentMethod, setPaymentMethod] = useState("");
  const [savePoint, setSavePoint] = useState(false);
  const [phoneNumber, setPhoneNumber] = useState("");

  const orderItems = useOrderStore((state) => state.items) ?? [];

  const totalPrice = orderItems.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0,
  );

  const paymentMethods = [
    "신용/체크카드",
    "삼성페이",
    "카카오페이",
    "네이버페이",
    "현금",
  ];

  const handlePayment = async () => {
    if (!paymentMethod) {
      alert("결제 수단을 선택해주세요.");
      return;
    }

    if (savePoint && !phoneNumber) {
      alert("휴대폰 번호를 입력해주세요.");
      return;
    }

    if (orderItems.length === 0) {
      alert("주문 내역이 없습니다.");
      return;
    }

    try {
      const tossPayments = await loadTossPayments(clientKey);
      const orderName =
        orderItems.length === 1
          ? orderItems[0].name
          : `${orderItems[0].name} 외 ${orderItems.length - 1}건`;

      await tossPayments.requestPayment("카드", {
        amount: totalPrice,
        // eslint-disable-next-line react-hooks/purity
        orderId: `ORDER_${Date.now()}`,
        orderName,
        successUrl: `${window.location.origin}/payment/success`,
        failUrl: `${window.location.origin}/payment/fail`,
      });
    } catch (error) {
      console.error(error);
    }

    // alert("결제가 완료되었습니다.");
    // console.log(logoutAction);
    // logout();
    // logoutAction();
    // navigate("/");
  };

  return (
    <Page>
      <Container>
        <Title>결제하기</Title>

        <OrderSummary>
          <SummaryTitle>주문 내역</SummaryTitle>

          {orderItems.map((item) => (
            <OrderItem key={item.id}>
              <ItemName>{item.name}</ItemName>

              <ItemInfo>
                <ItemQuantity>{item.quantity}개</ItemQuantity>

                <ItemPrice>
                  {(item.price * item.quantity).toLocaleString()}원
                </ItemPrice>
              </ItemInfo>
            </OrderItem>
          ))}

          <TotalSection>
            <span>총 결제 금액</span>
            <span>{totalPrice.toLocaleString()}원</span>
          </TotalSection>
        </OrderSummary>

        <SectionTitle>결제 수단 선택</SectionTitle>

        <PaymentGrid>
          {paymentMethods.map((method) => (
            <PaymentButton
              key={method}
              selected={paymentMethod === method}
              onClick={() => setPaymentMethod(method)}
            >
              {method}
            </PaymentButton>
          ))}
        </PaymentGrid>

        <PointContainer>
          <SectionTitle>멤버십 적립</SectionTitle>

          <RadioGroup>
            <RadioLabel>
              <input
                type="radio"
                checked={!savePoint}
                onChange={() => setSavePoint(false)}
              />
              적립 안함
            </RadioLabel>

            <RadioLabel>
              <input
                type="radio"
                checked={savePoint}
                onChange={() => setSavePoint(true)}
              />
              휴대폰 번호로 적립
            </RadioLabel>
          </RadioGroup>

          {savePoint && (
            <PhoneInput
              type="text"
              placeholder="휴대폰 번호 입력 (- 제외)"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
            />
          )}
        </PointContainer>

        <ButtonContainer>
          <BackButton onClick={() => navigate(-1)}>이전으로</BackButton>

          <PayButton onClick={handlePayment}>결제하기</PayButton>
        </ButtonContainer>
      </Container>
    </Page>
  );
}

export default PaymentPage;

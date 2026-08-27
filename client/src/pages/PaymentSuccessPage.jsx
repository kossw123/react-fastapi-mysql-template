import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

import axiosinstance from "../services/axiosInstance";

import {
  Page,
  Container,
  Title,
  SectionTitle,
  ButtonContainer,
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

function PaymentSuccessPage() {
  const [params] = useSearchParams();

  const [loading, setLoading] = useState(true);
  const [paymentStatus, setPaymentStatus] = useState("PENDING");
  const [order, setOrder] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const confirmPayment = async () => {
      const paymentKey = params.get("paymentKey");
      const orderId = params.get("orderId");
      const amount = Number(params.get("amount"));

      try {
        // 1. 결제 승인
        await axiosinstance.post("/payment/confirm", {
          paymentKey,
          orderId,
          amount,
        });

        setPaymentStatus("SUCCESS");

        // 2. 주문 상세 조회
        const orderResponse = await axiosinstance.get(`/order/${orderId}`);

        console.log(orderResponse.data);

        setOrder(orderResponse.data);
      } catch (err) {
        console.error("결제 처리 실패:", err);

        setPaymentStatus("FAILED");
        setError(
          err.response?.data?.message || "결제 처리 중 오류가 발생했습니다.",
        );
      } finally {
        setLoading(false);
      }
    };

    confirmPayment();
  }, [params]);

  // 결제 승인 중
  if (loading) {
    return (
      <Page>
        <Container>
          <Title>결제 처리 중</Title>

          <OrderSummary>
            <SummaryTitle>결제 승인</SummaryTitle>

            <SectionTitle>결제를 승인하고 있습니다.</SectionTitle>

            <p>잠시만 기다려주세요.</p>
          </OrderSummary>
        </Container>
      </Page>
    );
  }

  // 결제 실패
  if (paymentStatus === "FAILED") {
    return (
      <Page>
        <Container>
          <Title>결제 실패</Title>

          <OrderSummary>
            <SummaryTitle>결제 처리에 실패했습니다.</SummaryTitle>

            <SectionTitle>오류 내용</SectionTitle>

            <p>{error}</p>
          </OrderSummary>

          <ButtonContainer>
            <PayButton onClick={() => window.history.back()}>
              결제 페이지로 돌아가기
            </PayButton>
          </ButtonContainer>
        </Container>
      </Page>
    );
  }

  // 결제 성공
  return (
    <Page>
      <Container>
        <Title>결제 완료</Title>

        <OrderSummary>
          <SummaryTitle>주문 내역</SummaryTitle>

          {order?.items?.map((item) => (
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
            <span>{Number(order?.total_price ?? 0).toLocaleString()}원</span>
          </TotalSection>
        </OrderSummary>

        <OrderSummary>
          <SummaryTitle>결제 정보</SummaryTitle>

          <OrderItem>
            <ItemName>주문번호</ItemName>

            <ItemInfo>
              <ItemPrice>{order?.order_id}</ItemPrice>
            </ItemInfo>
          </OrderItem>

          <OrderItem>
            <ItemName>주문상태</ItemName>

            <ItemInfo>
              <ItemPrice>{order?.status}</ItemPrice>
            </ItemInfo>
          </OrderItem>
        </OrderSummary>

        <ButtonContainer>
          <PayButton onClick={() => (window.location.href = "/")}>
            처음으로
          </PayButton>
        </ButtonContainer>
      </Container>
    </Page>
  );
}

export default PaymentSuccessPage;

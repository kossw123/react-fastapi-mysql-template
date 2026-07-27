import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import axiosinstance from "../services/axiosInstance";

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
        const orderResponse = await axiosinstance.get(`/orders/${orderId}`);

        setOrder(orderResponse.data);
      } catch (err) {
        setPaymentStatus("FAILED");
        setError(err.response?.data?.message || "결제 처리 실패");
      } finally {
        setLoading(false);
      }
    };

    confirmPayment();
  }, [params]);

  if (loading) {
    return <h1>결제 승인 중...</h1>;
  }

  if (paymentStatus === "FAILED") {
    return (
      <div>
        <h1>결제 실패</h1>
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div>
      <h1>결제 완료</h1>

      {order && (
        <>
          <p>주문번호: {order.orderId}</p>
          <p>주문상태: {order.status}</p>
          <p>결제금액: {order.totalPrice}원</p>
        </>
      )}
    </div>
  );
}

export default PaymentSuccessPage;

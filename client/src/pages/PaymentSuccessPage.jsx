import { useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import axiosinstance from "../services/axiosInstance";

function PaymentSuccessPage() {
  const [params] = useSearchParams();

  useEffect(() => {
    const confirmPayment = async () => {
      const paymentKey = params.get("paymentKey");
      const orderId = params.get("orderId");
      const amount = Number(params.get("amount"));

      console.log(paymentKey);
      console.log(orderId);
      console.log(amount);

      try {
        const response = await axiosinstance.post("/payment/confirm", {
          paymentKey,
          orderId,
          amount,
        });

        console.log(response.data);
      } catch (error) {
        console.error("전체 에러", error);
        console.error("응답 데이터", error.response?.data);
      }
    };

    confirmPayment();
  }, []);

  return (
    <div>
      <h1>결제 승인 중...</h1>
    </div>
  );
}

export default PaymentSuccessPage;

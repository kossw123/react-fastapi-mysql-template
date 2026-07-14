import { useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import axios from "axios";

function PaymentSuccessPage() {
  const [params] = useSearchParams();

  useEffect(() => {
    const confirmPayment = async () => {
      const paymentKey = params.get("paymentKey");
      const orderId = params.get("orderId");
      const amount = Number(params.get("amount"));

      const response = await axios.post(
        "/payments/confirm",
        {
          paymentKey,
          orderId,
          amount,
        },
      );

      console.log(response.data);
    };

    confirmPayment();
  }, []);

  return <div>결제 승인 중...</div>;
}

export default PaymentSuccessPage;

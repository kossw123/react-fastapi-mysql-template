import requests


class PaymentResultUnknown(Exception):
    pass

class TossPaymentClient():
    def __init__(self, secret_key: str):
        if not secret_key:
            raise ValueError("TOSS_SECRET_KEY가 필요합니다.")
        self.secret_key = secret_key

    def confirm(
            self,
            *,
            payment_key: str,
            order_id: str,
            amount: int,
            idempotency_key: str) -> dict:
        try:
            response = requests.post("https://api.tosspayments.com/v1/payments/confirm",
                                     auth=(self.secret_key, ""), 
                                     headers= {"Idempotency-Key":idempotency_key,},
                                     json={
                                         "paymentKey": payment_key,
                                         "orderId": order_id,
                                         "amount": amount, 
                                     },
                                     timeout=(3, 15),)

            data = response.json()

        except (requests.RequestException, ValueError) as exc:
            raise PaymentResultUnknown("토스 승인 결과를 확인하지 못했습니다.") from exc

        if response.status_code != 200:
            raise PaymentResultUnknown("토스 응답의 추가 확인이 필요합니다.")
        if not isinstance(data, dict):
            raise PaymentResultUnknown("토스 응답 형식이 올바르지 않습니다.")
        if (
            data.get("status") != "DONE" or
            data.get("orderId") != order_id or
            data.get("totalAmount") != amount
            ):
            raise PaymentResultUnknown("승인 결과가 요청과 일치하지 않습니다.")

        return { 
            "status": "COMPLETED",
            "paymentKey": payment_key,
            "orderId": order_id,
            "amount": amount,
            "approvedAt": data.get("approvedAt"),
        }
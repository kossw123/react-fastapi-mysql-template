import requests


class PaymentResultUnknown(Exception):
    pass

class TossPaymentClient():
    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def confirm(
            self,
            payment_key: str,
            order_id: str,
            amount: int,
            idempotency_key: str):
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
            raise PaymentResultUnknown() from exc

        if response.status_code != 200:
            raise PaymentResultUnknown()
        if not isinstance(data, dict):
            raise PaymentResultUnknown()
        if (
            data.get("status") != "DONE" or
            data.get("orderId") != order_id or
            data.get("totalAmount") != amount
            ):
            raise PaymentResultUnknown()

        return { 
            "status": "COMPLETED",
            "paymentKey": payment_key,
            "orderId": order_id,
            "amount": amount,
            "approveAt": data.get("approveAt"),
        }
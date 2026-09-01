from src.Order.domain.Order import Order
from src.Order.domain.OrderItem import OrderItem
from uuid import uuid4

def test_order_total_amount():
    test_order_items = []
    test_order_items.append(
        OrderItem.create(
            product_id=uuid4(),
            name="아메리카노",
            quantity=2,
            price=10000
        )
    )


    order = Order(
        order_id=uuid4(),
        customer_id=uuid4(),
        items=test_order_items
    )

    # Act
    total = order.calculate_total_price()

    # Assert
    assert total == 20000
from src.Order.domain.Order import Order
from src.Order.domain.OrderItem import OrderItem
from uuid import uuid4
from src.Order.domain.OrderStatus import OrderStatus
import pytest

def test_order_amount_must_match():
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



def test_order_must_contain_one():
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

    if order.items:
        assert True
    else:
        assert False



def test_order_must_many_least_one():
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

    if len(order.items) >= 1:
        assert True
    else:
        assert False

def test_order_not_changed_after_completed():
    order = Order(
            order_id=uuid4(),
            customer_id=uuid4(),
            items=[]
        )

    order.add_item(OrderItem.create(
                product_id=uuid4(),
                name="아메리카노",
                quantity=2,
                price=10000
            ))
    order.mark_as_paid()

    with pytest.raises(ValueError, match="결제 완료된 주문은 수정할 수 없습니다"):
        order.add_item(
            OrderItem.create(
                product_id=uuid4(), 
                name="카페라떼", 
                quantity=3, 
                price=10000)
        )

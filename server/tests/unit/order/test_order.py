from src.Order.domain.Order import Order
from src.Order.domain.OrderItem import OrderItem
from uuid import uuid4
from src.Order.domain.commands import (
    OrderCreateHandler,
    OrderCreate
)
import pytest


# 규칙 3. 주문 금액은 상품 가격 × 수량과 일치해야 한다
def test_order_amount_must_match():

    # arrange
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


# 규칙 1. 주문에는 상품이 하나 이상 있어야 한다
def test_order_must_contain_one():
    # arrange
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

    # act
    if order.items:
        # assert
        assert True
    else:
        assert False


# 규칙 2. 주문 상품의 수량은 1개 이상이어야 한다
def test_order_must_many_least_one():
    # arrange
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

    # act
    if len(order.items) >= 1:
        # assert
        assert True
    else:
        assert False

# 규칙 4. 주문이 결제 완료된 이후에는 함부로 상태를 변경할 수 없다
def test_order_not_changed_after_completed():

    # arrange
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


    # act
    with pytest.raises(ValueError, match="결제 완료된 주문은 수정할 수 없습니다"):

        # assert
        order.add_item(
            OrderItem.create(
                product_id=uuid4(), 
                name="카페라떼", 
                quantity=3, 
                price=10000)
        )
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  Container,
  Header,
  HeaderRight,
  Title,
  ProductSection,
  ProductGrid,
  ProductCard,
  ProductName,
  ProductPrice,
  ManagementButton,
} from "./styles/KioskPageStyle";

import { getProducts } from "../services/productApi";
import { ordering } from "../services/orderApi";

import OrderPanel from "../components/OrderPanel";
import useOrderStore from "../zustand_store/OrderStore";
import useAuthStore from "../zustand_store/AuthStore";
import { logout } from "../services/loginApi";

function KioskPage() {
  const navigate = useNavigate();
  const setOrder = useOrderStore((state) => state.setOrder);
  const logoutAction = useAuthStore((state) => state.logout);
  const [orderItems, setOrderItems] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const loadProduct = async () => {
      const data = await getProducts();
      setProducts(data);
    };
    loadProduct();
  }, []);

  const submitHandle = (product) => {
    setOrderItems((prev) => {
      const existingItem = prev.find((item) => item.id === product.id);

      if (existingItem) {
        return prev.map((item) =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item,
        );
      }

      return [
        ...prev,
        {
          id: product.id,
          name: product.name,
          price: product.price,
          quantity: 1,
        },
      ];
    });
  };

  const increaseQuantity = (productId) => {
    setOrderItems((prev) =>
      prev.map((item) =>
        item.id === productId ? { ...item, quantity: item.quantity + 1 } : item,
      ),
    );
  };

  const decreaseQuantity = (productId) => {
    setOrderItems((prev) =>
      prev
        .map((item) =>
          item.id === productId
            ? { ...item, quantity: item.quantity - 1 }
            : item,
        )
        .filter((item) => item.quantity > 0),
    );
  };

  const orderingHandle = async () => {
    try {
      const order = await ordering(orderItems);
      setOrder(order);
      navigate("/paymentpage");
    } catch (error) {
      if (error.response?.status === 400) {
        console.log("상품이 없습니다.");
        return;
      }

      console.log("서버 오류");
    }
  };

  const logoutHandle = () => {
    const { token } = useAuthStore.getState();
    logout(token);
    logoutAction(); // zustand 상태 초기화
    navigate("/"); // 로그인 페이지로 이동
  };

  return (
    <Container>
      <Header>
        <Title>☕ CAFE KIOSK</Title>

        <HeaderRight>
          <ManagementButton onClick={() => navigate("/productmanagementpage")}>
            상품 관리
          </ManagementButton>

          <ManagementButton onClick={logoutHandle}>로그아웃</ManagementButton>
        </HeaderRight>
      </Header>

      <ProductSection>
        <ProductGrid>
          {products.map((product) => (
            <ProductCard key={product.id} onClick={() => submitHandle(product)}>
              <ProductName>{product.name}</ProductName>
              <ProductPrice>{product.price.toLocaleString()}원</ProductPrice>
            </ProductCard>
          ))}
        </ProductGrid>
      </ProductSection>

      <OrderPanel
        orderItems={orderItems}
        onIncrease={increaseQuantity}
        onDecrease={decreaseQuantity}
        onSubmitOrder={orderingHandle}
      />
    </Container>
  );
}

export default KioskPage;

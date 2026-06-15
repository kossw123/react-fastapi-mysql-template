import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ProductCreateForm from "../components/ProductCreateForm";
import ProductList from "../components/ProductList";
import {
  getProducts,
  deleteProduct,
  updateProduct,
} from "../services/productApi";

import {
  PageWrapper,
  TopBar,
  Logo,
  Brand,
  ContentWrapper,
  HeroSection,
  Title,
  Divider,
  Subtitle,
  Section,
  SectionTitle,
  Card,
  LogoutButton,
} from "./styles/ProductPageStyle";

function ProductPage() {
  const navigate = useNavigate();

  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    const data = await getProducts();
    setProducts(data);
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("access_token");

    navigate("/");
  };

  const handleDelete = async (productId) => {
    await deleteProduct(productId);

    fetchProducts();
  };

  const handleUpdate = async (productId, updatedData) => {
    await updateProduct(productId, updatedData);

    fetchProducts();
  };

  return (
    <PageWrapper>
      <TopBar>
        <Logo>☕</Logo>

        <Brand>TEST KIOSK</Brand>

        <LogoutButton onClick={handleLogout}>로그아웃</LogoutButton>
      </TopBar>

      <HeroSection>
        <Title>메뉴 관리 시스템</Title>

        <Divider />

        <Subtitle>상품 등록 및 관리</Subtitle>
      </HeroSection>

      <SectionTitle>상품 등록</SectionTitle>

      <ContentWrapper>
        <Section>
          <Card>
            <ProductCreateForm refresh={fetchProducts} />
          </Card>
        </Section>
      </ContentWrapper>

      <SectionTitle>상품 목록</SectionTitle>

      <ContentWrapper>
        <Section>
          <ProductList
            products={products}
            onDelete={handleDelete}
            onUpdate={handleUpdate}
          />
        </Section>
      </ContentWrapper>
    </PageWrapper>
  );
}

export default ProductPage;

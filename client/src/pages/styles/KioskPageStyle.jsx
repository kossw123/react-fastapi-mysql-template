import styled from "styled-components";

export const Container = styled.div`
  min-height: 100vh;
  background: #f8f6f2;
`;

export const Header = styled.header`
  position: relative;

  height: 80px;

  display: flex;
  align-items: center;
  justify-content: center;

  background: #ffffff;

  border-bottom: 1px solid #ececec;
`;

export const Title = styled.h1`
  font-size: 28px;
  font-weight: 700;
`;

export const ProductSection = styled.div`
  padding: 32px;
`;

export const ProductGrid = styled.div`
  display: grid;

  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));

  gap: 24px;
`;

export const ProductCard = styled.button`
  height: 180px;

  border: none;

  border-radius: 20px;

  background: white;

  cursor: pointer;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);

  transition: 0.2s;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  &:hover {
    transform: translateY(-4px);
  }

  &:active {
    transform: scale(0.98);
  }
`;

export const ProductName = styled.h2`
  margin-bottom: 12px;

  font-size: 22px;
`;

export const ProductPrice = styled.p`
  font-size: 18px;
  font-weight: bold;

  color: #7b5e57;
`;

export const OrderBar = styled.div`
  position: fixed;

  bottom: 0;
  left: 0;
  right: 0;

  height: 90px;

  background: white;

  border-top: 1px solid #ececec;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 0 32px;
`;

export const OrderInfo = styled.div`
  font-size: 18px;
  font-weight: 600;
`;

export const OrderButton = styled.button`
  width: 180px;
  height: 50px;

  border: none;

  border-radius: 12px;

  background: #2f2f2f;

  color: white;

  font-size: 16px;
  font-weight: 600;

  cursor: pointer;
`;

export const ManagementButton = styled.button`
  position: absolute;

  right: 24px;

  height: 42px;

  padding: 0 16px;

  border: none;

  border-radius: 10px;

  background: #2f2f2f;

  color: white;

  font-size: 14px;

  font-weight: 600;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    opacity: 0.9;
  }
`;

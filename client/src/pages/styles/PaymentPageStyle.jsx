import styled from "styled-components";

export const Page = styled.div`
  min-height: 100vh;
  background: #f7f3ef;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const Container = styled.div`
  width: 900px;
  background: white;
  border-radius: 24px;
  padding: 40px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
`;

export const Title = styled.h1`
  text-align: center;
  color: #f4a100;
  margin-bottom: 40px;
`;

export const SectionTitle = styled.h2`
  font-size: 24px;
  margin-bottom: 20px;
`;

export const TotalPrice = styled.div`
  font-size: 42px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 40px;
`;

export const PaymentGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
`;

export const PaymentButton = styled.button`
  padding: 25px;
  font-size: 18px;
  border: ${(props) =>
    props.selected ? "3px solid #f4a100" : "2px solid #ddd"};
  background: ${(props) => (props.selected ? "#fff4d6" : "white")};
  border-radius: 16px;
  cursor: pointer;
  transition: 0.2s;

  &:hover {
    transform: translateY(-3px);
  }
`;

export const PointContainer = styled.div`
  margin-top: 40px;
`;

export const RadioGroup = styled.div`
  display: flex;
  gap: 30px;
  margin-top: 15px;
`;

export const RadioLabel = styled.label`
  font-size: 18px;
  display: flex;
  align-items: center;
  gap: 8px;
`;

export const PhoneInput = styled.input`
  margin-top: 20px;
  width: 100%;
  padding: 15px;
  font-size: 18px;
  border-radius: 12px;
  border: 1px solid #ccc;
`;

export const ButtonContainer = styled.div`
  display: flex;
  gap: 20px;
  margin-top: 50px;
`;

export const BackButton = styled.button`
  flex: 1;
  padding: 20px;
  border: none;
  border-radius: 16px;
  background: #ddd;
  font-size: 20px;
  cursor: pointer;
`;

export const PayButton = styled.button`
  flex: 2;
  padding: 20px;
  border: none;
  border-radius: 16px;
  background: #f4a100;
  color: white;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;

  &:hover {
    background: #df9200;
  }
`;

export const OrderSummary = styled.div`
  background: #fafafa;
  border: 2px solid #eee;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 40px;
`;

export const SummaryTitle = styled.h2`
  margin-bottom: 20px;
  color: #333;
`;

export const OrderItem = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #eee;
`;

export const ItemName = styled.span`
  font-size: 18px;
  font-weight: 500;
`;

export const ItemInfo = styled.div`
  display: flex;
  gap: 20px;
`;

export const ItemQuantity = styled.span`
  color: #666;
`;

export const ItemPrice = styled.span`
  font-weight: bold;
`;

export const TotalSection = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;

  margin-top: 20px;
  padding-top: 20px;

  border-top: 3px solid #f4a100;

  font-size: 24px;
  font-weight: bold;
  color: #f4a100;
`;

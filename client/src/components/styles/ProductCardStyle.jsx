import styled from "styled-components";

export const Card = styled.div`
  position: relative;

  width: 100%;

  max-width: 560px;

  padding: 28px;

  border-radius: 20px;

  background: white;

  border: 2px solid #eeeeee;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);

  transition: 0.2s;

  overflow: hidden;

  &:hover {
    transform: translateY(-2px);

    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.08);
  }

  &::after {
    content: "";

    position: absolute;

    bottom: 0;
    left: 0;

    width: 100%;

    height: 6px;

    background: #ffe000;
  }
`;

export const TopSection = styled.div`
  display: flex;

  justify-content: space-between;

  align-items: flex-start;

  gap: 20px;
`;

export const ProductInfo = styled.div`
  flex: 1;
`;

export const ProductName = styled.h3`
  font-size: 28px;

  font-weight: 800;

  color: #111;

  margin-bottom: 12px;
`;

export const ProductPrice = styled.p`
  font-size: 18px;

  color: #555;

  margin-bottom: 12px;
`;

export const StatusBadge = styled.span`
  display: inline-block;

  padding: 6px 12px;

  border-radius: 999px;

  font-size: 13px;

  font-weight: 700;

  background: ${({ status }) => (status === "ACTIVE" ? "#FFE000" : "#DDDDDD")};

  color: ${({ status }) => (status === "ACTIVE" ? "#111111" : "#555555")};
`;

export const ButtonGroup = styled.div`
  display: flex;

  gap: 10px;
`;

export const UpdateButton = styled.button`
  border: 2px solid #111;

  background: white;

  color: #111;

  border-radius: 10px;

  padding: 10px 18px;

  font-size: 15px;

  font-weight: 700;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    background: #111;

    color: #ffe000;
  }
`;

export const DeleteButton = styled.button`
  width: 42px;

  height: 42px;

  border-radius: 10px;

  border: none;

  background: #111;

  color: white;

  font-size: 18px;

  font-weight: bold;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    opacity: 0.85;
  }
`;

export const EditInput = styled.input`
  width: 100%;

  padding: 14px 16px;

  margin-bottom: 14px;

  border-radius: 12px;

  border: 2px solid #eeeeee;

  background: white;

  font-size: 16px;

  color: #111;

  outline: none;

  transition: 0.2s;

  &:focus {
    border-color: #ffe000;

    box-shadow: 0 0 0 4px rgba(255, 224, 0, 0.25);
  }
`;

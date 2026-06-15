import styled from "styled-components";

export const PanelContainer = styled.div`
  position: fixed;

  bottom: 0;
  left: 0;
  right: 0;

  background: white;

  border-top: 1px solid #ddd;

  padding: 20px;

  box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.1);
`;

export const PanelTitle = styled.h3`
  margin-bottom: 16px;

  font-size: 20px;
  font-weight: 600;
`;

export const EmptyMessage = styled.p`
  color: #777;

  margin-bottom: 16px;
`;

export const Divider = styled.hr`
  margin: 16px 0;

  border: none;

  border-top: 1px solid #eee;
`;

export const Summary = styled.div`
  display: flex;

  justify-content: space-between;

  align-items: center;

  font-weight: bold;

  font-size: 18px;
`;

export const OrderSubmitButton = styled.button`
  width: 100%;

  height: 50px;

  margin-top: 16px;

  border: none;

  border-radius: 12px;

  background: #2f2f2f;

  color: white;

  font-size: 16px;

  font-weight: 600;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    opacity: 0.9;
  }

  &:active {
    transform: scale(0.98);
  }
`;

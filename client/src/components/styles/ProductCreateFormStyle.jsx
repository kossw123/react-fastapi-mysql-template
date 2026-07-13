import styled from "styled-components";

export const FormContainer = styled.form`
  display: flex;

  align-items: center;

  gap: 16px;

  width: 100%;
`;

export const Input = styled.input`
  height: 64px;

  padding: 0 20px;

  border-radius: 14px;

  border: 2px solid #eeeeee;

  background: white;

  font-size: 18px;

  color: #111;

  outline: none;

  transition: 0.2s;

  box-sizing: border-box;

  &::placeholder {
    color: #999;
  }

  &:focus {
    border-color: #ffe000;

    box-shadow: 0 0 0 4px rgba(255, 224, 0, 0.25);
  }
`;

export const NameInput = styled(Input)`
  flex: 1;

  min-width: 260px;
`;

export const PriceInput = styled(Input)`
  width: 160px;
`;

export const SubmitButton = styled.button`
  height: 64px;

  padding: 0 28px;

  border: none;

  border-radius: 14px;

  background: #111;

  color: #ffe000;

  font-size: 18px;

  font-weight: 800;

  cursor: pointer;

  white-space: nowrap;

  transition: 0.2s;

  &:hover {
    background: #222;

    transform: translateY(-2px);
  }

  &:active {
    transform: scale(0.98);
  }
`;

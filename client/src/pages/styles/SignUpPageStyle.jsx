import styled from "styled-components";

export const Container = styled.div`
  width: 100%;

  height: 100vh;

  display: flex;

  justify-content: center;

  align-items: center;
`;

export const SignupBox = styled.form`
  width: 350px;

  background: white;

  padding: 40px;

  border-radius: 12px;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);

  display: flex;

  flex-direction: column;

  gap: 15px;
`;

export const Title = styled.h1`
  text-align: center;

  margin-bottom: 10px;
`;

export const Input = styled.input`
  padding: 12px;

  border: 1px solid #ccc;

  border-radius: 8px;

  font-size: 16px;
`;

export const Button = styled.button`
  padding: 12px;

  border: none;

  border-radius: 8px;

  background-color: #4f46e5;

  color: white;

  font-size: 16px;

  font-weight: bold;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    background-color: #4338ca;
  }
`;

export const ErrorMessage = styled.p`
  color: red;

  font-size: 14px;

  text-align: center;

  margin: 0;
`;

export const SuccessMessage = styled.p`
  color: green;

  font-size: 14px;

  text-align: center;

  margin: 0;
`;

export const Footer = styled.div`
  text-align: center;

  font-size: 14px;

  color: #666;
`;

export const FooterLink = styled.span`
  color: #4f46e5;

  font-weight: bold;

  cursor: pointer;

  &:hover {
    text-decoration: underline;
  }
`;

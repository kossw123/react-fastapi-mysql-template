import { useState } from "react";
import styled from "styled-components";

import { createProduct } from "../services/productApi";

const FormContainer = styled.form`
  width: 350px;

  background: white;

  padding: 40px;

  border-radius: 12px;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);

  display: flex;
  flex-direction: column;

  gap: 15px;
`;

const Title = styled.h2`
  text-align: center;

  margin: 0 0 10px 0;
`;

const Input = styled.input`
  padding: 12px;

  border: 1px solid #ccc;

  border-radius: 8px;

  font-size: 16px;
`;

const Button = styled.button`
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

function ProductCreateForm({ refresh }) {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    await createProduct(name, price, "ACTIVE");

    setName("");
    setPrice("");

    refresh();
  };

  return (
    <FormContainer onSubmit={handleSubmit}>
      <Title>상품 등록</Title>

      <Input
        placeholder="상품 이름"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <Input
        placeholder="가격"
        type="number"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <Button type="submit">상품 추가</Button>
    </FormContainer>
  );
}

export default ProductCreateForm;

import { useState } from "react";

import { createProduct } from "../services/productApi";

import {
  FormContainer,
  NameInput,
  PriceInput,
  SubmitButton,
} from "./styles/ProductCreateFormStyle";

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
      <NameInput
        placeholder="상품 이름"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <PriceInput
        type="number"
        placeholder="가격"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <SubmitButton type="submit">상품 추가</SubmitButton>
    </FormContainer>
  );
}

export default ProductCreateForm;

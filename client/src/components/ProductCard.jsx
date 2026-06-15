import { useState } from "react";

import {
  Card,
  TopSection,
  ProductInfo,
  ProductName,
  ProductPrice,
  StatusBadge,
  ButtonGroup,
  UpdateButton,
  DeleteButton,
  EditInput,
} from "./styles/ProductCardStyle";

function ProductCard({ product, onDelete, onUpdate }) {
  const [isEditing, setIsEditing] = useState(false);

  const [editName, setEditName] = useState(product.name);

  const [editPrice, setEditPrice] = useState(product.price);

  const handleUpdate = async () => {
    await onUpdate(product.id, {
      name: editName,
      price: editPrice,
      status: product.status,
    });

    setIsEditing(false);
  };

  return (
    <Card>
      <TopSection>
        <ProductInfo>
          {isEditing ? (
            <>
              <EditInput
                value={editName}
                onChange={(e) => setEditName(e.target.value)}
                placeholder="상품 이름"
              />

              <EditInput
                type="number"
                value={editPrice}
                onChange={(e) => setEditPrice(e.target.value)}
                placeholder="가격"
              />
            </>
          ) : (
            <>
              <ProductName>☕ {product.name}</ProductName>

              <ProductPrice>가격 : {product.price}원</ProductPrice>
            </>
          )}

          <StatusBadge status={product.status}>{product.status}</StatusBadge>
        </ProductInfo>

        <ButtonGroup>
          <UpdateButton
            onClick={() => {
              if (isEditing) {
                handleUpdate();
              } else {
                setIsEditing(true);
              }
            }}
          >
            {isEditing ? "저장" : "수정"}
          </UpdateButton>

          <DeleteButton onClick={() => onDelete(product.id)}>✕</DeleteButton>
        </ButtonGroup>
      </TopSection>
    </Card>
  );
}

export default ProductCard;

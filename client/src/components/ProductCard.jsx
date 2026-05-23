import { useState } from "react";

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
    <div
      style={{
        position: "relative",

        border: "2px solid #dcdcdc",

        borderRadius: "16px",

        padding: "20px",

        paddingBottom: isEditing ? "70px" : "20px",

        margin: "15px",

        width: "300px",

        backgroundColor: "#ffffff",

        boxShadow: "0 4px 12px rgba(0,0,0,0.12)",

        transition: "0.2s",
      }}
    >
      {/* Delete 버튼 */}
      <button
        onClick={() => onDelete(product.id)}
        style={{
          position: "absolute",

          top: isEditing ? "auto" : "12px",

          bottom: isEditing ? "12px" : "auto",

          right: "12px",

          width: "32px",

          height: "32px",

          border: "none",

          borderRadius: "50%",

          backgroundColor: "#ff4d4f",

          color: "white",

          fontWeight: "bold",

          cursor: "pointer",

          fontSize: "14px",
          
          display: "flex",
          
          alignItems: "center",
          
          justifyContent: "center",
        }}
      >
        X
      </button>

      {/* Update / Save 버튼 */}
      <button
        onClick={() => {
          if (isEditing) {
            handleUpdate();
          } else {
            setIsEditing(true);
          }
        }}
        style={{
          position: "absolute",

          top: isEditing ? "auto" : "12px",

          bottom: isEditing ? "12px" : "auto",

          right: "56px",

          width: isEditing ? "60px" : "72px",

          height: "32px",

          border: "none",

          borderRadius: "8px",

          backgroundColor: "#1677ff",

          color: "white",

          fontWeight: "bold",

          cursor: "pointer",

          fontSize: "12px",
        }}
      >
        {isEditing ? "Save" : "Update"}
      </button>

      {/* 수정 모드 */}
      {isEditing ? (
        <>
          <input
            value={editName}
            onChange={(e) => setEditName(e.target.value)}
            style={{
              width: "100%",

              marginBottom: "12px",

              padding: "8px",

              boxSizing: "border-box",

              border: "1px solid #d9d9d9",

              borderRadius: "8px",
            }}
          />

          <input
            type="number"
            value={editPrice}
            onChange={(e) => setEditPrice(e.target.value)}
            style={{
              width: "100%",

              marginBottom: "12px",

              padding: "8px",

              boxSizing: "border-box",

              border: "1px solid #d9d9d9",

              borderRadius: "8px",
            }}
          />
        </>
      ) : (
        <>
          <h3
            style={{
              marginBottom: "16px",

              fontSize: "22px",

              paddingRight: "120px",
            }}
          >
            {product.name}
          </h3>

          <p
            style={{
              fontSize: "16px",
            }}
          >
            가격 : {product.price}
          </p>
        </>
      )}

      {/* 상태 */}
      <p
        style={{
          color: product.status === "ACTIVE" ? "green" : "gray",

          fontWeight: "bold",

          marginTop: "12px",
        }}
      >
        상태 : {product.status}
      </p>
    </div>
  );
}

export default ProductCard;

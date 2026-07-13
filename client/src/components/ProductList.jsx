import ProductCard from "./ProductCard";

function ProductList({ products, onDelete, onUpdate }) {
  return (
    <div>
      <h2>상품 목록</h2>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
        }}
      >
        {products.map((p) => (
          <ProductCard
            key={p.id}
            product={p}
            onDelete={onDelete}
            onUpdate={onUpdate}
          />
        ))}
      </div>
    </div>
  );
}

export default ProductList;

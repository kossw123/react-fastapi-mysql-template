import ProductCard from "./ProductCard";

function ProductList({ products, onDelete }) {
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
          <ProductCard key={p.id} product={p} onDelete={onDelete} />
        ))}
      </div>
    </div>
  );
}

export default ProductList;

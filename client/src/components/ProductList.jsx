import ProductCard from "./ProductCard"

function ProductList({ products }) {

    return (
        <div>
            <h2>상품 목록</h2>

            <div style={{ display: "flex", flexWrap: "wrap" }}>
                {products.map((p) => (
                    <ProductCard key={p.id} product={p} />
                ))}
            </div>

        </div>
    )
}

export default ProductList
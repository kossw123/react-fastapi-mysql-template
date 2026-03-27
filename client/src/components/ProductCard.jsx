function ProductCard({ product }) {

    return (
        <div style={{
            border: "1px solid gray",
            padding: "10px",
            margin: "10px",
            width: "200px"
        }}>

            <h3>{product.name}</h3>

            <p>가격 : {product.price}</p>

            <p>상태 : {product.status}</p>

        </div>
    )
}

export default ProductCard
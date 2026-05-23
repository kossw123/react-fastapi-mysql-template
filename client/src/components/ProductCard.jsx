

function ProductCard({ product, onDelete }) {
    return (
        <div
            style={{
                position: "relative",

                border: "2px solid #dcdcdc",

                borderRadius: "16px",

                padding: "20px",

                margin: "15px",

                width: "260px",

                // backgroundColor: "#ffffff",
                backgroundColor: "#ffffff",

                boxShadow: "0 4px 12px rgba(0,0,0,0.12)",

                transition: "0.2s"
            }}
        >

            <button
                onClick={() => onDelete(product.id)}

                style={{
                    position: "absolute",

                    top: "12px",
                    right: "12px",

                    width: "32px",
                    height: "32px",

                    border: "none",

                    borderRadius: "50%",

                    backgroundColor: "#ff4d4f",

                    color: "white",

                    fontWeight: "bold",

                    cursor: "pointer",

                    fontSize: "14px"
                }}
            >
                X
            </button>

            <h3
                style={{
                    marginBottom: "16px",
                    fontSize: "22px"
                }}
            >
                {product.name}
            </h3>

            <p
                style={{
                    fontSize: "16px"
                }}
            >
                가격 : {product.price}
            </p>

            <p
                style={{
                    color:
                        product.status === "ACTIVE"
                            ? "green"
                            : "gray",

                    fontWeight: "bold"
                }}
            >
                상태 : {product.status}
            </p>

        </div>
    )
}

export default ProductCard
import { useState } from "react"
// import { createProduct } from "./services/ProductApi"
import { createProduct } from "../services/productApi"


function ProductCreateForm({ refresh }) {

    const [name, setName] = useState("")
    const [price, setPrice] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()

        await createProduct(name, price)

        setName("")
        setPrice("")

        refresh()
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>상품 등록</h2>

            <input
                placeholder="상품 이름"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />

            <input
                placeholder="가격"
                type="number"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
            />

            <button type="submit">상품 추가</button>
        </form>
    )
}

export default ProductCreateForm
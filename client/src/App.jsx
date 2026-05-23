import { useEffect, useState } from "react"

import {
    getProducts,
    deleteProduct
} from "./services/productApi"

import ProductCreateForm from "./components/ProductCreateForm"

import ProductList from "./components/ProductList"

function App() {

    const [products, setProducts] = useState([])

    const fetchProducts = async () => {
        const data = await getProducts()
        setProducts(data)
    }

    useEffect(() => {
        fetchProducts()
    }, [])

    /* 추가 */

    const handleDelete = async (productId) => {
        await deleteProduct(productId)
        fetchProducts()
    }

    return (
        <div>

            <h1>키오스크 상품 관리</h1>

            <ProductCreateForm refresh={fetchProducts} />

            <ProductList
                products={products}
                onDelete={handleDelete}
            />

        </div>
    )
}

export default App
import { useEffect, useState } from "react";

import {
  getProducts,
  deleteProduct,
  updateProduct,
} from "./services/productApi";

import ProductCreateForm from "./components/ProductCreateForm";

import ProductList from "./components/ProductList";

function App() {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    const data = await getProducts();
    setProducts(data);
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleDelete = async (productId) => {
    await deleteProduct(productId);

    fetchProducts();
  };

  const handleUpdate = async (productId, updatedData) => {
    await updateProduct(productId, updatedData);

    fetchProducts();
  };

  return (
    <div>
      <h1>키오스크 상품 관리</h1>

      <ProductCreateForm refresh={fetchProducts} />

      <ProductList
        products={products}
        onDelete={handleDelete}
        onUpdate={handleUpdate}
      />
    </div>
  );
}

export default App;

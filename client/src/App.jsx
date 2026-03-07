import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [products, setProducts] = useState([]);

  const API = "https://upgraded-space-adventure-967j956r9ggc7qqv-8000.app.github.dev";

  // 처음 렌더링될 때 상품 목록 가져오기
  useEffect(() => {
    axios
      .get(`${API}/products`)
      .then((res) => {
        setProducts(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  // 상품 추가
  const create_product = () => {
    axios
      .post(`${API}/products`, {
        name: "Americano",
        price: 3000,
      })
      .then((res) => {
        setProducts((prev) => [...prev, res.data]);
      })
      .catch((err) => {
        console.error(err.response?.data || err);
      });
  };

  return (
    <div>
      <h1>Product list</h1>

      <button onClick={create_product}>add</button>

      {products.map((p) => (
        <div key={p.id}>
          {p.name} - {p.price}
        </div>
      ))}
    </div>
  );
}

export default App;
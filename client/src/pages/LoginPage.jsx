import { useNavigate } from "react-router-dom";

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = () => {
    // 나중에 실제 로그인 로직 추가
    navigate("/products");
  };

  return (
    <div>
      <h1>Login Page</h1>

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default LoginPage;

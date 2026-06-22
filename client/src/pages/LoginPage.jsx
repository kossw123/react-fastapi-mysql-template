import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/loginApi";
import useAuthStore from "../zustand_store/AuthStore";
import { jwtDecode } from "jwt-decode";
import {
  Container,
  LoginBox,
  Title,
  Input,
  ErrorMessage,
  ButtonGroup,
  Button,
} from "./styles/LoginPageStyle";

function LoginPage() {
  const loginAction = useAuthStore((state) => state.login);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLoading, isSetLoading] = useState(false);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      isSetLoading(true);

      if (isLoading == false) {
        setError("로그인 중 입니다.");
      }

      if (!username.trim() || !password.trim()) {
        setError("필요한 정보를 입력 해주세요.");
        return;
      }

      const response = await login(username, password);

      const payload = jwtDecode(response.token).username;
      const token = response.token;

      if (!payload || !token) {
        throw new Error("페이로드나 토큰이 없습니다.");
      }

      loginAction(payload, token);

      setError("");
      navigate("/kioskpage");
    } catch (err) {
      console.log(err);
      console.log(err.response);

      if (err.response?.status === 401) {
        setError("아이디 또는 비밀번호가 틀렸습니다.");
      } else {
        setError("서버와 통신할 수 없습니다.");
      }
    } finally {
      isSetLoading(false);
    }
  };

  const handleSignup = (e) => {
    e.preventDefault();
    navigate("/signuppage");
  };

  return (
    <Container>
      <LoginBox onSubmit={handleLogin}>
        <Title>Login</Title>

        <Input
          type="text"
          placeholder="ID"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        {error && <ErrorMessage>{error}</ErrorMessage>}

        <ButtonGroup>
          <Button type="submit">로그인</Button>

          <Button type="button" onClick={handleSignup} disabled={isLoading}>
            회원가입
          </Button>
        </ButtonGroup>
      </LoginBox>
    </Container>
  );
}

export default LoginPage;

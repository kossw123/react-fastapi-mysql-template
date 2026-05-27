import { useState } from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";

const Container = styled.div`
  width: 100%;
  height: 100vh;

  display: flex;
  justify-content: center;
  align-items: center;
`;

const LoginBox = styled.form`
  width: 350px;

  background: white;

  padding: 40px;

  border-radius: 12px;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);

  display: flex;
  flex-direction: column;

  gap: 15px;
`;

const Title = styled.h1`
  text-align: center;

  margin-bottom: 10px;
`;

const Input = styled.input`
  padding: 12px;

  border: 1px solid #ccc;

  border-radius: 8px;

  font-size: 16px;
`;

const ErrorMessage = styled.p`
  color: red;

  font-size: 14px;

  text-align: center;

  margin: 0;
`;

const ButtonGroup = styled.div`
  display: flex;

  gap: 10px;
`;

const Button = styled.button`
  flex: 1;

  padding: 12px;

  border: none;

  border-radius: 8px;

  background-color: #4f46e5;

  color: white;

  font-size: 16px;
  font-weight: bold;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    background-color: #4338ca;
  }
`;

function LoginPage() {
  const navigate = useNavigate();

  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();

    // 테스트용 계정
    const correctId = "admin";
    const correctPassword = "1234";

    if (id === correctId && password === correctPassword) {
      navigate("/productpage");
    } else {
      setError("아이디 또는 비밀번호가 틀렸습니다.");
    }
  };

  const handleSignup = (e) => {
    e.preventDefault();

    navigate("/SignupPage");
  };

  return (
    <Container>
      <LoginBox onSubmit={handleLogin}>
        <Title>Login</Title>

        <Input
          type="text"
          placeholder="ID"
          value={id}
          onChange={(e) => setId(e.target.value)}
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

          <Button type="button" onClick={handleSignup}>
            회원가입
          </Button>
        </ButtonGroup>
      </LoginBox>
    </Container>
  );
}

export default LoginPage;

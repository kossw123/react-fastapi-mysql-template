import { useState } from "react";

import { useNavigate } from "react-router-dom";

import {
  Container,
  SignupBox,
  Title,
  Input,
  Button,
  ErrorMessage,
  SuccessMessage,
  Footer,
  FooterLink,
} from "./styles/SignUpPageStyle";

import { signup } from "../services/signupApi";

function SignUpPage() {
  const navigate = useNavigate();

  const API = "http://localhost:8000";

  const [username, setUsername] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [error, setError] = useState("");

  const [success, setSuccess] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      if (!username.trim() || !email.trim() || !password.trim()) {
        setError("필요한 정보를 모두 입력해주세요.");
        return;
      }

      setError("");
      setSuccess("");

      await signup(username, email, password);

      setSuccess("회원가입 성공!");

      setTimeout(() => {
        handleLoginMove();
      }, 1000);
    } catch (error) {
      console.log(error);

      if (error.response?.status === 409) {
        setError("이미 가입된 회원입니다.");
        return;
      }

      setError("회원가입 중 오류 발생");
    }
  };
  const handleLoginMove = () => {
    navigate("/");
  };

  return (
    <Container>
      <SignupBox onSubmit={handleSignup}>
        <Title>Sign Up</Title>

        <Input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        {error && <ErrorMessage>{error}</ErrorMessage>}

        {success && <SuccessMessage>{success}</SuccessMessage>}

        <Button type="submit">회원가입</Button>

        <Footer>
          이미 계정이 있나요?{" "}
          <FooterLink onClick={handleLoginMove}>로그인</FooterLink>
        </Footer>
      </SignupBox>
    </Container>
  );
}

export default SignUpPage;

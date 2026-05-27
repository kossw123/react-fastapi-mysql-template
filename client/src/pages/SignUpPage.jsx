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

const SignupBox = styled.form`
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

const Button = styled.button`
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

const ErrorMessage = styled.p`
  color: red;

  font-size: 14px;

  text-align: center;

  margin: 0;
`;

const SuccessMessage = styled.p`
  color: green;

  font-size: 14px;

  text-align: center;

  margin: 0;
`;

const Footer = styled.div`
  text-align: center;

  font-size: 14px;

  color: #666;
`;

const FooterLink = styled.span`
  color: #4f46e5;

  font-weight: bold;

  cursor: pointer;

  &:hover {
    text-decoration: underline;
  }
`;

function SignUpPage() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();

    setError("");
    setSuccess("");

    try {
      const response = await fetch("http://localhost:8000/signup", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username,
          email,
          password,
        }),
      });

      if (!response.ok) {
        throw new Error("회원가입 실패");
      }

      setSuccess("회원가입 성공!");

      setTimeout(() => {
        navigate("/");
      }, 1000);
    } catch (error) {
      console.error(error);

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

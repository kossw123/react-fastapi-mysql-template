import styled from "styled-components";

export const PageWrapper = styled.div`
  min-height: 100vh;

  background: #f5f5f5;

  color: #111;

  font-family: "Pretendard", sans-serif;
`;

export const TopBar = styled.div`
  height: 90px;

  background: #ffe000;

  display: flex;

  align-items: center;

  padding: 0 40px;

  gap: 16px;

  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
`;

export const Logo = styled.div`
  width: 56px;

  height: 56px;

  border-radius: 50%;

  background: #111;

  color: #ffe000;

  display: flex;

  align-items: center;

  justify-content: center;

  font-size: 28px;
`;

export const Brand = styled.h1`
  font-size: 36px;

  font-weight: 900;

  margin: 0;

  color: #111;

  letter-spacing: -1px;
`;

export const ContentWrapper = styled.div`
  width: 100%;

  max-width: 1200px;

  margin: 0 auto;

  padding: 0 40px;
`;

export const HeroSection = styled.div`
  text-align: center;

  padding: 60px 0;
`;

export const Title = styled.h1`
  margin: 0;

  font-size: 56px;

  font-weight: 900;

  color: #111;
`;

export const Divider = styled.div`
  width: 100px;

  height: 6px;

  background: #ffe000;

  margin: 24px auto;
`;

export const Subtitle = styled.p`
  margin: 0;

  font-size: 22px;

  color: #555;

  font-weight: 500;
`;

export const Section = styled.div`
  margin-bottom: 48px;
`;

export const SectionTitle = styled.h2`
  width: 100%;

  max-width: 1200px;

  margin: 0 auto 24px;

  padding: 0 40px;

  font-size: 30px;

  font-weight: 800;

  color: #111;
`;

export const Card = styled.div`
  background: white;

  border-radius: 20px;

  padding: 28px;

  border: 2px solid #eee;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
`;

export const LogoutButton = styled.button`
  margin-left: auto;

  padding: 12px 20px;

  border: none;

  border-radius: 10px;

  background: #111;

  color: #ffe000;

  font-weight: 700;

  cursor: pointer;

  transition: 0.2s;

  &:hover {
    transform: translateY(-2px);
  }
`;

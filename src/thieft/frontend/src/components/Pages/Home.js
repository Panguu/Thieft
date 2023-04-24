import React, {useEffect} from 'react';
import axios from "axios";
import styled from 'styled-components';
import { motion } from 'framer-motion';
import { Button } from '@material-ui/core';

export const Home = () => {
  useEffect(() => {
    if (localStorage.getItem('token') !== undefined) {
      axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {
        if (res.data !== "Token is valid") {
          window.location.pathname = '/signin';
        }
      })
    }
  }, []);

  const Section = styled.section`
  margin-top: -10%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const Container = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: 100vh;
  padding: 3rem calc((100vw - 1300px) / 2);
  
  @media screen and (max-width: 768px) {
    grid-grid-template-columns: 1fr;
  }
`;

  const fadeLeft = {
    hidden: { opacity: 0, x: -100 },
    visible: { opacity: 1, x: 0 }
  };
  return (
  

    <Section id="home-bg">
      <Container>
        <div className="hero">
          <motion.h1
            variants={fadeLeft}
            initial='hidden'
            animate='visible'
            transition={{ duration: 1 }}
          >
            Welcome to Thieft: A Bluetooth-Enabled Theft and Collision Detection Device for Vehicles
          </motion.h1>

          <div className="hero-buttons">
          <Button className="bt" type="submit" variant="contained" color="primary" fullWidth onClick={() => window.location.href="/help"}>Get Started</Button>
          <Button className="bt" type="submit" variant="contained" color="primary" fullWidth onClick={() => window.location.href="https://gitlab.computing.dcu.ie/oreilj46/2022-ca400-oreilj46-berminn4/-/tree/master/docs"}>Find Out More</Button>
          </div>

        </div>
      </Container>
    </Section>
  );
};
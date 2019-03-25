import React, { Component } from 'react';
import { Container, Card } from 'react-bootstrap';
import axios from 'axios';

import LoginForm from '../Components/login/loginForm'

// this can be called whatever
function onSubmit(values) {
    console.log(values)
    getLogInToken(values);
}

function getLogInToken(values) {
    let username = values.username
    let pwd = values.pwd

    axios({
        method: 'post',
        url: `http://100.1.253.16:8000/o/token/?grant_type=password&username=${username}&password=${pwd}&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M`,
    })
        .then(res => {
            let accessToken = res.data.access_token;
            // store accessToken in state
            
        })
}

const LoginPage = () => {
    return (
        <Container>
            <Card>
                <Card.Body>
                    <Card.Title>Login</Card.Title>
                    <LoginForm onSubmit={onSubmit} />
                </Card.Body>
            </Card>
        </Container>
    )
}

export default LoginPage;


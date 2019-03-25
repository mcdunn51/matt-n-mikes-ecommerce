import React from 'react';
import { Container, Card } from 'react-bootstrap';
import axios from 'axios';
import { connect } from 'react-redux';

import LoginForm from './loginForm'


function getLogInToken(values, storeAccessToken) {
    let username = values.username
    let pwd = values.pwd

    axios({
        method: 'post',
        url: `http://100.1.253.16:8000/o/token/?grant_type=password&username=${username}&password=${pwd}&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M`,
    })
        .then(res => {
            let accessToken = res.data.access_token;
            if (accessToken) {
                storeAccessToken(accessToken);
            }
        })
}

const Index = (props) => {
    const {storeAccessToken} = props
    return (
        <Container>
            <Card>
                <Card.Body>
                    <Card.Title>Login</Card.Title>
                    <LoginForm onSubmit={(values) => getLogInToken(values, storeAccessToken)} />
                </Card.Body>
            </Card>
        </Container>
    )
}

function mapDispatchToProps(dispatch) {
    return {
        storeAccessToken: (accessToken) => {
            // console.log(accessToken) this is working
            dispatch({ type: 'STORE_ACCESS_TOKEN', payload: accessToken })
        }
    }
}


export default connect(null, mapDispatchToProps)(Index);


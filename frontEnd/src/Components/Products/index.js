import React, { Component } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import CardImage from '../../images/cardImage.jpg';


class ProductsIndex extends Component {

    state = {
        products: []
    }

    componentDidMount() {
        axios({
            method: 'post',
            url: 'http://192.168.20.100:8000/Address/?access_token=n9mPEVc0HBCH2Y3S3nxxgDQ8PR2FVQ',
            data: {
                customerID: 1,
                address1: "Sutton House",
                address2: "Berry Hill Road",
                town: "Staffordshire",
                county: "Staffordshire",
                postcode: "ST4 2NL",
                phoneNumber: "01782 838822",
                email: "rkw@rkwltd.com",
                country: "UK"
            }
        })
            .then(res => {
                console.log(res.data);
                // this.setState({ products: res.data });
            })
    }


    // componentDidMount() {
    //     axios.get(`http://192.168.20.89:8000/Productlist/?access_token=RzazVFDkRrWvJzpUCUyBsoabf5cQQS&format=json`)
    //         .then(res => {
    //             console.log(res.data);
    //             this.setState({ products: res.data });
    //         })
    // }

    render() {
        return (
            // <ul>
            //     {this.state.persons.map(person => 
            //     <li>{person.description}</li>)}
            // </ul>
            <Container>
                <Row>
                    <Col md={3}>
                        <Card style={{ width: '18rem' }}>
                            <Card.Img variant="top" src={CardImage} />
                            <Card.Body>
                                <Card.Title>Card Title</Card.Title>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default ProductsIndex;
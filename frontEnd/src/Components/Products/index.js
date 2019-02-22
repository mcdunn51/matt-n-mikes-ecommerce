import React, { Component } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import CardImage from '../../images/cardImage.jpg';


class ProductsIndex extends Component {
    // state = {
    //     persons: []
    // }

    state = {
        products: []
    }

    componentDidMount() {
        // axios.get(`http://192.168.20.118:8000/Productlist/?access_token=sFAXJvmPcog2aGQyrK0aK3KRi8mERm&format=json`)
        //     .then(res => {
        //         console.log(res.data);
        //         this.setState({ persons: res.data });
        //     })


    }

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
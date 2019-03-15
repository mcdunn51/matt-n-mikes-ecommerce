import React, { Component } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import CardImage from '../../images/cardImage.jpg';
import Filters from './filters';


class ProductsIndex extends Component {

    state = {
        products: []
    }

    componentDidMount() {
        axios.get(`http://100.1.253.16:8000/Productlist/?access_token=KtSyKysXXRXDItz8AEkTUUZOMqEM5E&manufacturerCode=${this.props.id}`)
            .then(res => {
                console.log(res.data);
                this.setState({ products: res.data });
            })
    }

    render() {
        return (
            // <ul>
            //     {this.state.persons.map(person => 
            //     <li>{person.description}</li>)}
            // </ul>
            <Container fluid={true}>
                <Row>
                    <Col md={1} />
                    <Filters />
                    {this.state.products.map(product => 
                    <Col md={2}>
                        <Card>
                            <Card.Img variant="top" src={CardImage} />
                            <Card.Body>
                                <Card.Title>{product.id}</Card.Title>
                                <Card.Text>
                                    {product.description}
                                </Card.Text>
                                {product.price}
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>,
                    {/* <Col md={2}>
                        <Card>
                            <Card.Img variant="top" src={CardImage} />
                            <Card.Body>
                                <Card.Title>{this.props.id}</Card.Title>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={2}>
                        <Card>
                            <Card.Img variant="top" src={CardImage} />
                            <Card.Body>
                                <Card.Title>{this.props.id}</Card.Title>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col md={2}>
                        <Card>
                            <Card.Img variant="top" src={CardImage} />
                            <Card.Body>
                                <Card.Title>{this.props.id}</Card.Title>
                                <Card.Text>
                                    Some quick example text to build on the card title and make up the bulk of
                                    the card's content.
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Col> */},
                    {/* <Col md={1} /> */}
                    )}
                </Row>
            </Container>
        )
    }
}

export default ProductsIndex;
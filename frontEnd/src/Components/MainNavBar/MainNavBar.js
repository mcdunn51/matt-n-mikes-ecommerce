import React from 'react';
import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap';
import {IndexLinkContainer} from 'react-router-bootstrap';



const mainNavbar = () => {

    return (
        <Navbar id="MainNavBar" bg="light" expand="lg">
            <Navbar.Brand href="#home">Matt and Mike's Eccomerce Site</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <IndexLinkContainer to="/">
                        <Nav.Link>Home</Nav.Link>
                    </IndexLinkContainer>
                    <IndexLinkContainer to="/products">
                        <Nav.Link>Products</Nav.Link>
                    </IndexLinkContainer>
                    <IndexLinkContainer to="/checkout">
                        <Nav.Link>Checkout</Nav.Link>
                    </IndexLinkContainer>
                </Nav>
                <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-success">Search</Button>
                </Form>
            </Navbar.Collapse>
        </Navbar>
    )
};

export default mainNavbar;



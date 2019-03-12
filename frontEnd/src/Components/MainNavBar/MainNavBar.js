import React, { Component } from 'react';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button } from 'react-bootstrap';
import { IndexLinkContainer } from 'react-router-bootstrap';
import axios from 'axios';

class MainNavbar extends Component {

    state = {
        brands: []
    }



    // get all brand names
    componentDidMount() {
        axios.get(`http://192.168.20.100:8000/Manufacturer/?access_token=n9mPEVc0HBCH2Y3S3nxxgDQ8PR2FVQ`)
            .then(res => {

                const manufacturerCodes = [];

                res.data.forEach(element => {
                    if (element.manufacturerCode.startsWith('s') || element.manufacturerCode.startsWith('S')) {
                        manufacturerCodes.push(element.manufacturerCode);
                    }
                });

                this.setState({ brands: manufacturerCodes });
            })
    };


    render() {
        return (
            <Navbar id="MainNavBar" bg="light" expand="lg">
                <Navbar.Brand href="#home">Matt and Mike's Eccomerce Site</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <IndexLinkContainer to="/">
                            <Nav.Link>Home</Nav.Link>
                        </IndexLinkContainer>

                        <NavDropdown title="brands" id="basic-nav-dropdown">
                            {
                                this.state.brands.map(brand => 
                                    <IndexLinkContainer to="{/products">
                                        <NavDropdown.Item>{brand}</NavDropdown.Item>
                                    </IndexLinkContainer>
                                )
                            }
                        </NavDropdown>

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
    }
}

export default MainNavbar;



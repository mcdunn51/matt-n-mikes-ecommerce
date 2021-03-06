import React from 'react';
import { Route } from 'react-router-dom';

import HomePage from './pages/Home';
import Products from './pages/Products';
import Checkout from './pages/Checkout';
import Cart from './pages/Cart';
import LoginForm from './pages/login';
// import Error from './pages/Error';



const Router = () => {
    return (
        <div>
            <Route exact path="/" component={HomePage} />
            <Route path="/products/:id" component={Products} />
            <Route exact path="/checkout" component={Checkout} />
            <Route exact path="/cart" component={Cart} />
            <Route exact path="/login" component={LoginForm} />
            {/* <Route component={Error} /> */}
        </div>
    )
}

export default Router; 

import React from 'react';
import { Route } from 'react-router-dom';
import Products from './pages/Products'


import HomePage from './pages/Home';

const Router = () => {
    return (
    <div>
        <Route exact path="/" component={HomePage} />
        <Route exact path="/products" component={Products} />
    </div>
    )
}

export default Router; 

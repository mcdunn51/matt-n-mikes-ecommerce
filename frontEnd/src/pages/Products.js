import React from 'react';
import ProductsIndex from '../Components/Products/index'

const Products = (props) => {
    return (
        <div>
            <h2>{props.match.params.id}</h2>
            <ProductsIndex id={props.match.params.id}/>
        </div>
    )
}

export default Products;
import { createStore, combineReducers} from 'redux';
import { reducer as formReducer } from 'redux-form';

import brandsReducer from './Components/MainNavBar/reducer';
import productsReducer from './Components/Products/reducer';
import cartReducer from './Components/Cart/reducer';

const rootReducer = combineReducers({
    brands: brandsReducer,
    products: productsReducer,
    cart: cartReducer,
    form: formReducer
})

const store = createStore(
    rootReducer, 
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)

export default store;
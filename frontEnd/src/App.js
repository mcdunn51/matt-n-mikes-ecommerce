import React, { Component } from 'react';
import MainNavBar from './Components/MainNavBar/MainNavBar';
import ThreeBrands from './Components/ThreeBrands/ThreeBrands';
import Footer from './Components/Footer/Footer';



class App extends Component {
  render() {
    return (
      <div className="App">
        <MainNavBar/>
        <ThreeBrands/>
        <Footer/>
      </div>
    );
  }
}

export default App;

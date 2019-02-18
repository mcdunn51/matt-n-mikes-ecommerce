import React, { Component } from 'react';
import MainNavBar from './Components/MainNavBar/MainNavBar';
import ThreeBrands from './Components/ThreeBrands/ThreeBrands';



class App extends Component {
  render() {
    return (
      <div className="App">
        <MainNavBar/>
        <ThreeBrands/>
      </div>
    );
  }
}

export default App;

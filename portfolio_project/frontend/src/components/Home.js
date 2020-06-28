import React from 'react';
import { render } from "react-dom";

class Home extends React.Component {
  render() {
      return (
        <div className="container">
          <p id="home_name"> Kamile Demir </p>
          <p id="home_majorminor"> Computer Science | Digital Art </p>
          <p id="home_slogan"> Inspiring technology with art</p>
        </div>
      );
  }
}

export default Home;

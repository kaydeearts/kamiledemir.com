import React from 'react';
import ReactDOM from 'react-dom';
import Menu from './components/Menu'
import Home from './components/Home'
import App from './components/App';
import './css/menu.css';
import * as serviceWorker from './serviceWorker';


ReactDOM.render(
  <React.StrictMode>
    <Menu/>
    <Home/>
    <App/>
  </React.StrictMode>,
  document.getElementById('app')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

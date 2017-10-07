// @flow

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

import NavbarComponent from '../Navbar';

class App extends React.Component<any, any> {
  render() {
    return (
      <Router>
        <div>
          <NavbarComponent />
        </div>
      </Router>
    );
  }
}

export default App;

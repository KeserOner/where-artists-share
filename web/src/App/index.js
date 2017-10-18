// @flow

import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

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

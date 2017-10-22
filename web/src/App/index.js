// @flow

import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

import Header from '../Header';

const App = () => (
  <Router>
    <div>
      <Header />
    </div>
  </Router>
);

export default App;

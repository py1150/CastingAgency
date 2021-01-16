import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom';

//import logo from './logo.svg';
import './App.css';

import IndexView from './components/IndexView';
import UserView from './components/UserView';


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <Router>
            <Switch>
              <Route path="/" exact component={IndexView} />
              <Route path="/user" component={UserView} />
              {/*<Route component={IndexView} />*/}
            </Switch>
          </Router>
        </header>
      </div>
    );
 }
}

export default App;

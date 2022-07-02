import React from 'react'
import ReactDOM from 'react-dom'
import { Route, Link, BrowserRouter as Router, Switch } from 'react-router-dom'
import App from './components/App'
import {GetDataGeneration} from './components/charts/generation_side/fetchDataGeneration'
import {GetDataLoad} from './components/charts/load_side/fetchDataLoad'
import logo from './img/logo.svg';
import Nav from 'react-bootstrap/Nav'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';


const routing = (
  <Router>
    <div>
      <div>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Micro Grid Analytics</h1>
        </header>
      </div>
        <nav className="navbar navbar-inverse">
          <div className="container-fluid">
            <ul className="nav navbar-nav">
              <li><a href="/">Home</a></li>
              <li><a href="/generaton">Generation</a></li>
              <li><a href="/load">Load</a></li>
            </ul>
          </div>
        </nav>
      </div>
      <div>
        <Switch>
          <Route exact path="/" component={App} />
          <Route path="/generaton" component={GetDataGeneration} />
          <Route path="/load" component={GetDataLoad} />
        </Switch>
      </div>
    </div>
  </Router>
)
ReactDOM.render(routing, document.getElementById('root'))
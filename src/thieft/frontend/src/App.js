// imports
import "./App.css";
import React from "react";
import NavBar from "./components/NavBar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Home } from "./components/Pages/Home";
import { Profile } from "./components/Pages/Profile";
import { Settings } from "./components/Pages/Settings";
import { Vehicle } from "./components/Pages/Vehicle";
import { Devices } from "./components/Pages/Devices";
import { Help } from "./components/Pages/Help";
import { Security } from "./components/Pages/Security";
import { Incidents } from "./components/Pages/Incidents"
import Login from "./components/Pages/Login";
import ChangePassword from "./components/Pages/changePassword";
import Location from "./components/Pages/Location";
import {  List } from '@material-ui/core';
import Username from "./components/Pages/changeUsername";


const App = () => {


  return (


  
  // router enables navigation to viewing components
      <Router>
        <NavBar />

        <div className="pages">
          <Switch>

            <Route exact path="/" component={Home} />
            <Route path="/profile" component={Profile} />
            <Route path="/settings" component={Settings} />
            <Route path="/help" component={Help} />
            <Route path="/signin" component={Login} />
            <Route path="/changepassword" component={ChangePassword} />
            <Route path="/location" component={Location} />
            <Route path="/devices" component={Devices} />
            <Route path="/vehicle" component={Vehicle} />
            <Route path="/security" component={Security} />
            <Route path="/incidents" component={Incidents} />
            <Route path="/changeusername" component={Username} />
            

          </Switch>
        </div>
        <List>
        <ul id="nav-sidebar">
          <li>
            <a class="fa fa-home" href="/"><span>Home</span></a>
          </li>
          <li>
            <a class="fa fa-user" href="/profile"><span>Profile</span></a>
          </li>
          <li>
            <a class="fa fa-gear" href="/settings"><span>Settings</span></a>
          </li>
          <li>
            <a class="fa fa-car" href="/vehicle"><span>Vehicle Data</span></a>
          </li>
          <li>
            <a class="fa fa-location-arrow" href="/location"><span> Last Location</span></a>
          </li>
        </ul>
        </List>
      </Router>

      
  );
}

export default App;

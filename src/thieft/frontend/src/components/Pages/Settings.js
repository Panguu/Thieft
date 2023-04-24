import React, {useEffect} from 'react';
import axios from "axios";
import "../../App.css";
import {List} from '@material-ui/core';



export const Settings = () => {
  useEffect(() => {
    if (localStorage.getItem('token') !== undefined) {
      axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {
        if (res.data !== "Token is valid") {
          window.location.pathname = '/signin';
        }
      })
    }
  }, []);
  return ( 
        <List>
          <div class="container">
  <div class="items">
    
    <div class="items-body">
      <div class="items-body-content">
        <a href="/security"><span><a class="fa fa-lock"></a>Sign In & Security</span></a>
        <i class="fa fa-angle-right"></i>
      </div>
      <div class="items-body-content">
      <a href="/devices"><span><a class="fa fa-bluetooth"></a>Manage Devices</span></a>
        <i class="fa fa-angle-right"></i>
      </div>
    </div>
  </div>
</div>
        </List>
  );
}
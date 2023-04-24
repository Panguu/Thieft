import React, {useEffect} from 'react';
import axios from "axios";
import {List} from '@material-ui/core';

export const Security = () => {
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
                    <a href="/changeusername"><span><a class="fa fa-user"></a>Change Username</span></a>
                    <i class="fa fa-angle-right"></i>
                </div>
                <div class="items-body-content">
                    <a href="/changepassword"><span><a class="fa fa-lock"></a>Change Password</span></a>
                    <i class="fa fa-angle-right"></i>
                </div>
      
            </div>
        </div>
    </div>
    </List>
  );
};
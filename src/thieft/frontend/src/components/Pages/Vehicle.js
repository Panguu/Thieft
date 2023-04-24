import React, {useEffect} from 'react';
import axios from "axios";
import "../../App.css";
import {List} from '@material-ui/core';



export const Vehicle = () => {
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
                    <a href="/incidents"><span><a class="fa fa-car"></a>Journey Data</span></a>
                    <i class="fa fa-angle-right"></i>
                </div>
                <div class="items-body-content">
                <a href="/location"><span><a class="fa fa-location-arrow"></a>Last Location</span></a>
                    <i class="fa fa-angle-right"></i>
                </div>
      
            </div>
        </div>
    </div>
    </List>
  );
}
import React, {useEffect} from 'react';
import axios from "axios";
import "../../App.css";
import { Button, MenuItem, Card, CardContent, Grid, List, ListItem, ListItemText, Menu } from '@material-ui/core';



export const Help = () => {
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
    <Grid>
    <Card id="card">
      <CardContent id="card-content">
      <form>
        <div id="card-form-title">Getting Started</div>
      <Grid item xs={12}>
      <List
  sx={{ width: '100%', height: '100%', bgcolor: 'background.paper' }}>
    <ListItem>
    <ListItemText><p><h6>Step 1:</h6> Fill out the required information (phone number *) on the <a href="/profile">Profile</a> page.</p></ListItemText>
  </ListItem>
  <ListItem>
  <ListItemText><p><h6>Step 2:</h6> Add a bluetooth device to your authenticated devices list on the <a href="/devices">Devices</a> page.</p></ListItemText>
  </ListItem>
  <ListItem>
  <ListItemText><p><h6>Step 3:</h6> That's it! You are now ready to receive alerts!</p></ListItemText>
  </ListItem>
</List>
</Grid>
        </form>
      </CardContent>
    </Card>
  </Grid>
  );
}

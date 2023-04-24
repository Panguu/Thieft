import React, { useState, useEffect } from 'react';
import axios from "axios";
import {Button, TextField, Grid, Typography,Container} from '@material-ui/core';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';




const Login = () => {

  const handleClose = (event, reason) => {
    if (reason ==="clickaway") {
      return
      }
      setOpen(false)
  }

  
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [open, setOpen] = useState(false)


    useEffect(() => {
      if (localStorage.getItem('token') !== undefined) {
        axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {
          if (res.data === "Token is valid") {

            window.location.pathname = '';
          }
        })
      }
    }, []);
    
  
    const onSubmit = e => {
      e.preventDefault();
  
      const user = {
        username: username,
        password: password
      };
      // create login request
      axios.post('auth/login/', user)
        .then(res => {
          console.log(res.data);
          if (res.data.token !== undefined) {
            localStorage.setItem('token', res.data.token);

            window.location.pathname = '';
          }
        })
      };
    return (
      <Container maxWidth="xs">
      <div className="signin">
      <Typography className="type-h5" gutterBottom variant="h5" align="center">
              Sign In
          </Typography>
          <form onSubmit={onSubmit}>
          <TextField className="txt"
            onChange={e => setUsername(e.target.value)}
            value={username}
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
            autoFocus
          />
          <TextField className="txt"
            onChange = {e => setPassword(e.target.value)}
            value={password}
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <Button className="bt"
            type="submit"
            fullWidth
            variant="contained"
          >
            Sign In
          </Button>

          <Grid container>
            <Grid item xs>


            </Grid>
            <Grid item>
            </Grid>
            <Grid item>
            </Grid>
          </Grid>
        </form>

      </div>
    </Container>
  );
}

export default (Login);

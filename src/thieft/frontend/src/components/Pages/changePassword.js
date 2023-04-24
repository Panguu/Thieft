import React, {  useState, useEffect } from 'react';
import axios from "axios";
import {Button, TextField, Grid, Typography,Container} from '@material-ui/core';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';

const ChangePassword = () => {

    const [username, setUsername] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const [setErrors] = useState(false);
    const [open, setOpen] = useState(false);
    const [incorrect, setIncorrect] = useState(false);

    const handleClose = (reason) => {

      if(reason === "clickaway") {
          return
        }
        setOpen(false)
        setIncorrect(false)
    }
  
    useEffect(() => {
      if (localStorage.getItem('token') !== undefined) {
        axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {
          if (res.data !== "Token is valid") {
            window.location.pathname = '/signin';
          }
        })
      }
    }, []);
    
      const onSubmit = e => {
        e.preventDefault();
        if (password1 !== password2) {
          setIncorrect(true);
        } else {
          const user = {
            username: username,
            new_password: password2,
            token: localStorage.getItem('token')
          };
          setOpen(true);
          axios.post('auth/changePassword/', user).then(res => {
            if (res.data === "Password changed") {
              window.location.pathname = '/';
            } else {
              alert(res.data);
            }
          });
        }
    };
  

    return (
      <Container maxWidth="xs">
      <div className="signin">
      <Typography className="type-h5" gutterBottom variant="h5" align="center">
              Change Password
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
            onChange = {e => setPassword1(e.target.value)}
            value={password1}
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="New Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <TextField className="txt"
            onChange = {e => setPassword2(e.target.value)}
            value={password2}
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Confirm Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <Button className="bt"
            type="submit"
            fullWidth
            variant="contained"
          >
            Change Password
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

        <Snackbar id="snack"
                    anchorOrigin={{
                    vertical: 'center',
                    horizontal: 'center',
                    }}
                    open={open} autoHideDuration={3000} onClose={handleClose}>
                    <MuiAlert id="alert" elevation={6}  variant="filled" onClose={handleClose} severity="success">Password Updated!
                    </MuiAlert>
      </Snackbar>
      <Snackbar id="snack"
                    anchorOrigin={{
                    vertical: 'center',
                    horizontal: 'center',
                    }}
                    open={incorrect} autoHideDuration={3000} onClose={handleClose}>
                    <MuiAlert id="alert" elevation={6}  variant="filled" onClose={handleClose} severity="error">Error: Username or Password Incorrect!
                    </MuiAlert>
      </Snackbar>

      </div>
    </Container>
  );
};

export default (ChangePassword);
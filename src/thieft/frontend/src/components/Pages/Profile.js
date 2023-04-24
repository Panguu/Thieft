import React, {useState, useEffect} from 'react';
import axios from "axios";
import "../../App.css";
import TextField from '@material-ui/core/TextField';
import { Button, Card, CardContent, Grid, Avatar } from '@material-ui/core';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';




export const Profile = () => {
  const [firstname, setFirstname] = useState('');
  const [lastname, setLastname] = useState('');
  const [phonenumber, setPhonenumber] = useState('');
  const [address , setAddress] = useState('');
  const [city, setCity] = useState('');
  const [country, setCountry] = useState('');
  const [open, setOpen] = useState(false);

  const handleClose = (reason) => {

    if(reason === "clickaway") {
        return
      }
      setOpen(false)
  }


  useEffect(() => {
    if (localStorage.getItem('token') !== undefined) {
      axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {
        if (res.data !== "Token is valid") {
          window.location.pathname = '/signin';
        }
      })
    }
    axios.post('auth/profileDetails/', {"token": localStorage.getItem('token')}).then(res => res.data).then(data => {
      setFirstname(data.firstName);
      setLastname(data.lastName);
      setPhonenumber(data.phoneNumber);
      setAddress(data.address);
      setCity(data.city);
      setCountry(data.country);
      console.log(data.firstname);
    })
  }, []);

  const onSubmit = e => {
    e.preventDefault();
    setOpen(true);
    axios.post('auth/updateProfileDetails/', 
    {"token": localStorage.getItem('token'),
    "firstName": firstname,
    "lastName": lastname,
    "phoneNumber": phonenumber,
    "address": address,
    "city": city,
    "country": country
    }).then(res => res.data).then(data => {
      console.log("updated user profile");
      
    })
  }
  return (
    <div className="profile"> 
      <Grid>
        <Card className="card">
          <CardContent className="card-content">
            <form>
              
              <Grid container spacing={2}>
                <Grid xs={12} item>
                  <TextField className="txt" placeholder={"Enter first name"} label="First Name" value={firstname} onChange={e => setFirstname(e.target.value)} variant="outlined" fullWidth />
                </Grid>
                <Grid xs={12} item>
                  <TextField className="txt" placeholder={"Enter last name"} label="Last Name" value={lastname} onChange={e => setLastname(e.target.value)} variant="outlined" fullWidth />
                </Grid>

                <Grid item xs={12}>
                  <TextField className="txt" placeholder={"Enter phone number"} label="Phone" value={phonenumber} onChange={e => setPhonenumber(e.target.value)} variant="outlined" fullWidth required/>
                </Grid>

                <Grid item xs={12}>
                  <TextField className="txt" placeholder={"Enter Address"} label="Address" value={address} onChange={e => setAddress(e.target.value)} variant="outlined" fullWidth />
                </Grid>

                <Grid item xs={12}>
                  <TextField className="txt" placeholder={"Enter City"} label="City" value={city} onChange={e => setCity(e.target.value)} variant="outlined" fullWidth />
                </Grid>

                <Grid item xs={12}>
                  <TextField className="txt" placeholder={"Enter Country"} label="Country" value={country} onChange={e => setCountry(e.target.value)} variant="outlined" fullWidth />
                </Grid>
                
                <Grid item xs={12}>
                  <Button className="bt" type="submit" variant="contained" color="primary" fullWidth onClick={onSubmit}>UPDATE PROFILE</Button>
                </Grid>
                </Grid>
                </form>

                
              
          </CardContent>
        </Card>
      </Grid>
      <Snackbar id="snack"
                    anchorOrigin={{
                    vertical: 'center',
                    horizontal: 'center',
                    }}
                    open={open} autoHideDuration={3000} onClose={handleClose}>
                    <MuiAlert elevation={6}  variant="filled" onClose={handleClose} severity="success">Profile Updated!
                    </MuiAlert>
      </Snackbar>
      
    </div>
    
  );
}
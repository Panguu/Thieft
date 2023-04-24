import React, {useEffect, useState} from 'react';
import axios from "axios";
import "../../App.css";
import TextField from '@material-ui/core/TextField';
import { Button, MenuItem, Card, CardContent, Grid, List, ListItem, ListItemText, Menu } from '@material-ui/core';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';


export const Devices = () => {

  const [bluetoothDevices, setBluetoothDevices] = useState(["test1", "test2"]);
  const [approvedBleDevices, setApprovedBleDevices] = useState([]);
  const [device, setDevice] = useState("");
  const [trackerDevices, setTrackerDevices] = useState([]);
  const [setSelectBleDevices, setSelectBleDevicesState] = useState(false);
  const [correct, setCorrect] = useState(false);
  const [incorrect, setIncorrect] = useState(false);

  const handleCollapse = (reason) => {

    if(reason === "clickaway") {
        return
      }
      setCorrect(false)
      setIncorrect(false)
  }

  function getBleDevicesInRange() {
    axios.post('device/getBluetoothDevicesInRange/', {"token": localStorage.getItem('token')}).then(res => {
      if (res.data === null){
        setTrackerDevices(["No devices in range"]);
      }
      else {
        let devices = []
        for (var device in res.data) {
          devices.push(res.data[device]);
        }
        setBluetoothDevices(devices);
      }

    })
  }
  function getBleDevices() {
    axios.post('device/getregisteredBluetoothDevices/', {"token": localStorage.getItem('token')}).then(res => {
      if (res.data === null){
        setTrackerDevices(["No devices in range"]);
      }
      else {
        let devices = []
        for (var device in res.data) {
          devices.push(res.data[device]);
        }
        setApprovedBleDevices(devices);
      }

    })
  }
  function getTrackerDevices() {
    axios.post('device/getDevices/', {"token": localStorage.getItem('token')}).then(res => {
      if (res.data === null){
        setTrackerDevices(["No devices in range"]);
      }
      else {
        let devices = []
        for (var device in res.data) {
          devices.push(res.data[device][1]);
        }
        setTrackerDevices(devices);
      }

    })
  }
  function setBleDevices() {
    let devices = {
      "token": localStorage.getItem('token'),
      "registeredBluetoothDevices": setSelectBleDevices
    }
    axios.post('device/registerBluetooth/', devices).then(res => {
      if (res.data === 'added bluetooth device'){
        alert("Added bluetooth device")
      }
      else {
        alert("unable to add bluetooth device")
      }

    })
  }
  function handleDeleteDevice(ble_device) {
    axios.post('device/removeBluetooth/', {"token": localStorage.getItem('token'), "bluetooth_id": ble_device[2], "device_id": 1}).then(res => {
      if (res.data === null){
        setTrackerDevices(["No devices in range"]);
      }
      else {
        let devices = []
        for (var device in res.data) {
          devices.push(res.data[device][1]);
        }
        setTrackerDevices(devices);
      }
    })
  }
  function addnewDevice() {
    axios.post('device/registerDevice/', {"token":localStorage.getItem('token'), "device_id": device}).then(res => {
      if (res.data === "OK"){
        alert("device has been added");
      }
      else {
        alert("device has not been added");
      }
    }).catch(err => {
      alert(`Error has occured: ${err}`);
    })
  }

  useEffect(() => {
    if (localStorage.getItem('token') !== undefined) {
      axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {
        if (res.data !== "Token is valid") {
          window.location.pathname = '/signin';
        }
      })
    }
    getBleDevicesInRange();
    getTrackerDevices();
    getBleDevices();
  }, []);

  return (
    <div className="profile"> 
      <Grid>
        <Card className="card">
          <CardContent className="card-content">
          <form>
            <div id="form-title">Bluetooth Devices</div>
          <Grid item xs={12}>
          <List
      sx={{ width: '100%', bgcolor: 'background.paper' }}
    >
    {approvedBleDevices.map((device, index) => {
      return (
        <ListItem>
        <ListItemText id="switch-list-label-device" primary={device[1]} />
      <a href='' id='remove' onClick={() => handleDeleteDevice(device)}>Remove</a>
      </ListItem>
      )
    })}
    </List>
    </Grid>
            <Grid container spacing ={2}>
              <Grid item xs={12} id="help-text">
              <TextField
          id="outlined-select"
          variant="outlined"
          select
          label="Add Device"
          placeholder="Add Bluetooth Device"
          fullWidth required
        >
        {bluetoothDevices.map((option, index) => {
          return (
            <MenuItem key={option[1]} value={option[1]} onClick={() => {setSelectBleDevicesState([option[1], option[2]])}}>
              {option}
            </MenuItem>
          )
        })}
        </TextField>
        <p>*Adds device to authenticated bluetooth devices list*</p>
              </Grid>
              <Grid item xs={12}>
                  <Button className="bt" type="submit" variant="contained" color="primary" onClick={setBleDevices} fullWidth>UPDATE BLUETOOTH DEVICES</Button>
                </Grid>
              </Grid>
            </form>
          </CardContent>
        </Card>
      </Grid>
      <Grid>
        <Card className="card" id="second-card">
          <CardContent className="card-content">
          <form>
            <div id="form-title">Thieft Devices</div>
          <Grid item xs={12}>
          <List
      sx={{ width: '100%', bgcolor: 'background.paper' }}
    >
    {trackerDevices.map((index, value) => (
      <ListItem>
        <ListItemText id="switch-list-label-device" primary={value} />
      <a href='' id='remove' onClick={() => delete trackerDevices[index]}>Remove</a>
      </ListItem>
    ))}
    </List>
    </Grid>
    <Grid container spacing ={2}>
      <Grid item xs={12} id="help-text">
        <TextField
              id="outlined"
              variant="outlined"
              value={device}
              onChange={(e) => setDevice(e.target.value)}
              label="Add Device ID"
              placeholder="Add Device"
              fullWidth required
        >
        </TextField>
        <p>*Adds device to authenticated devices list*</p>
              </Grid>
              <Grid item xs={12}>
                  <Button className="bt" type="submit" variant="contained" color="primary" onClick={addnewDevice} fullWidth>UPDATE DEVICES</Button>
                </Grid>
              </Grid>
            </form>
          </CardContent>
        </Card>
      </Grid>
    </div>
    
  );
}
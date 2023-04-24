import React, { useState, useEffect } from "react";
import "../../App.css";
import {TableContainer, Table, TableCell, TableRow, Paper, TableBody, TableHead, Button} from '@material-ui/core';
import axios from 'axios';



export const Incidents = () => {

  const [rows , setRows] = useState([]);

  function createData(deviceId, journeyId, type, time, gcd, location) {
    return { deviceId, journeyId, type, time, gcd, location};
  }

  function loadLocation(device_id, journey_id){
    localStorage.setItem('device_id', device_id);
    localStorage.setItem('journey_id', journey_id);
    window.location.pathname = '/location';
  }
  useEffect(() =>{
    const loadResults = async() => {
      await axios.post('tracking/data/getAllJourneys/', {"token" : localStorage.getItem('token')}).then(
        res=>res.data).then(
          data=>{
            let jsonRows = []
            for (let [deviceKey, deviceValue] of Object.entries(data)) {
              for (let [journeyKey, journeyValue] of Object.entries(deviceValue)) {
                journeyValue.forEach((x, i) => {
                  jsonRows.push(createData(deviceKey, journeyKey, x.trackerType, x.timestamp, x.gcd, `${x.latitude}, ${x.longitude}`));
                });
              }
            }
            setRows(jsonRows);
        }
      )}
    loadResults();
  }, []);
  
  return ( 

    <TableContainer id="incident-table" component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>DeviceID</TableCell>
            <TableCell>JourneyID</TableCell>
            <TableCell align="center">Type</TableCell>
            <TableCell align="center">Time</TableCell>
            <TableCell align="center">GCD</TableCell>
            <TableCell align="center">Location</TableCell>
            <TableCell align="center">Data</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {rows.map((row) => (
            <TableRow
              key={row.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.deviceId}
              </TableCell>
              <TableCell component="th" scope="row">
                {row.journeyId}
              </TableCell>
              <TableCell align="right">{row.type}</TableCell>
              <TableCell align="right">{row.time}</TableCell>
              <TableCell align="right">{row.gcd}</TableCell>
              <TableCell align="right">{row.location}</TableCell>
              <TableCell align="right" onClick={() => loadLocation(row.deviceId, row.journeyId)}>
              <Button className="bt" id="data-bt" 
              type="submit" variant="contained" color="primary" fullWidth
              >View</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    )
}
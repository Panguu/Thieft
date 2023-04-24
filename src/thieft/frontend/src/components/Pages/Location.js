import React, {useEffect, useState} from 'react';
import axios from "axios";
import { Map, Marker, ZoomControl} from "pigeon-maps";
import { osm } from 'pigeon-maps/providers';


export const Location = () => {

  const [markerInformation, setMarkerInformation] = useState([{lat: 0.0, lng: 0.0, timestamp: ""}]);
  const primaryMarkerSize = 80;
  const secondaryMarkerSize = 30;
  const [center, setCenter] = useState([53, -6]);
  const [loading, setLoading] = useState(true);
  const primaryColour = 'black';
  const secondaryColour = '#0000eb';

  // sort marker information by latitude, longitude and timestamp
  function sortMarkerInformation(lat, lng, timestamp){
    return {lat, lng, timestamp}
  }

  // wait to receive journey information
  async function getJourneyInfoLocation(journeyId, deviceId) {

    await axios.post('/tracking/getJourneyInfo/', {"token": localStorage.getItem('token'), "journey_id": journeyId, "device_id": deviceId}).then(res => {
      let locationData = []

      // for each variable in result data
      for (var i in res.data) {

        let data = res.data[i];
        locationData.push(sortMarkerInformation((data.latitude).toFixed(4), (data.longitude).toFixed(4), data.timestamp));
        setCenter([parseFloat((data.latitude).toFixed(4)), parseFloat((data.longitude).toFixed(4))]);
      }
      // add location data to marker
      setMarkerInformation(locationData);
      setLoading(false);
      
    })
  };



  useEffect(() => {
    if (localStorage.getItem('token') !== undefined) {

      axios.post('auth/checkToken/', {"token": localStorage.getItem('token')}).then(res => {

        if (res.data !== "Token is valid") {
          window.location.pathname = '/signin';
        }
      })
    }
    // get journey and device ID from local storage
    let journey_id = localStorage.getItem('journey_id');
    let device_id = localStorage.getItem('device_id');

    // if journey data is not equal to null
    if (typeof journey_id !== undefined && journey_id !== null && typeof  device_id !== undefined && device_id !== null) {
      getJourneyInfoLocation(journey_id, device_id);
      localStorage.removeItem('journey_id');
      localStorage.removeItem('device_id');
    }
    else {
      // assign default value
      getJourneyInfoLocation(1, 1);
    }
  }, []);

    if (loading) { 
      return (<div id="loading">Loading...</div>)
    } else {
      return (
    <div id="map" className="map">
    <Map
    // pigeon maps provider
    provider={osm}
    height={800}
    center={center}
    defaultZoom={16}
  >
  <ZoomControl/>

  {markerInformation.map((marker, index) => {
    if (index + 1 === markerInformation.length) {
      return (<Marker
      anchor={[parseFloat(marker.lat), parseFloat(marker.lng)]}
      width={primaryMarkerSize}
      color={primaryColour}
    />)
    }else{
      return (<Marker
      anchor={[parseFloat(marker.lat), parseFloat(marker.lng)]}
      width={secondaryMarkerSize}
      color={secondaryColour}
    />)
      }
  })}
  </Map>
  </div>
    )}
};

export default (Location);
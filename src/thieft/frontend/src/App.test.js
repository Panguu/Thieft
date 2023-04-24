import { render, screen } from '@testing-library/react';
import App from './App';
import Login from "./components/Pages/Login";
import Signup from "./components/Pages/Signup";
import Location from "./components/Pages/Location";
import { Profile } from "./components/Pages/Profile";
import { Settings } from "./components/Pages/Settings";
import { Vehicle } from "./components/Pages/Vehicle";
import { Devices } from "./components/Pages/Devices";
import { Help } from "./components/Pages/Help";
import { Security } from "./components/Pages/Security";
import { Alerts } from "./components/Pages/Alerts";
import { Incidents } from "./components/Pages/Incidents";

test('renders app', () => {
  render(<App />);
});

test('renders login', () => {
  render(<Login />);
});

test('renders sign up', () => {
  render(<Signup />);
});

test('renders sign up', () => {
  render(<Location />);
});

test('renders profile', () => {
  render(<Profile />);
});

test('renders settings', () => {
  render(<Settings />);
});

test('renders vehicle', () => {
  render(<Vehicle />);
});

test('renders vehicle', () => {
  render(<Devices />);
});

test('renders vehicle', () => {
  render(<Help />);
});

test('renders security', () => {
  render(<Security />);
});

test('renders alerts', () => {
  render(<Alerts />);
});

test('renders incidents', () => {
  render(<Incidents />);
});



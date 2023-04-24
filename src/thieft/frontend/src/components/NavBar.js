import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

function NavBar() {
  const [click, setClick] = useState(false);

  const handleClick = () => setClick(!click);
  const handleSignout = () => {localStorage.clear(); window.location.pathname = '/signin';};
  return (
    <>
      <nav className="navbar">
        <div className="nav-container">
          <NavLink exact to="/" className="nav-logo">
            <h3>THIEFT</h3>
          </NavLink>
          { localStorage.getItem('token') !== null &&
          <ul className={click ? "nav-menu active" : "nav-menu"}>
            <li className="nav-item">
              <NavLink
                exact
                to="/"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/profile"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                Profile
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/settings"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                Settings
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to="/vehicle"
                activeClassName="active"
                className="nav-links"
                onClick={handleClick}
              >
                Vehicle Data
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                exact
                to='/signin'
                activeClassName="active"
                className="nav-links"
                onClick={handleSignout}
              >
                Sign Out
              </NavLink>
            </li>
          </ul>
          }
          <div className="nav-icon" onClick={handleClick}>
            <i className={click ? "fas fa-times" : "fas fa-bars"}></i>
          </div>
        </div>
      </nav>
    </>
  );
}

export default NavBar;

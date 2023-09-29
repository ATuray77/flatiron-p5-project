import React from 'react'
import { NavLink } from 'react-router-dom'
//import "./App.css";


const linkStyles = {
  display: "inline-block",
  width: "50px",
  padding: "12px",
  margin: "0px 6px 6px",
  background: "green",
  textDecoration: "none",
  color: "white",
};

function NavBar() {
  return (
    <div>
      <NavLink to="/" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
        Home
      </NavLink>
      <NavLink to="/songs" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
        Songs
      </NavLink>
      <NavLink to="/form" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
        Form
      </NavLink>
    </div>
  );
}

export default NavBar
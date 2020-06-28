import React from 'react';
import { render } from "react-dom";
import { Navbar, NavItem, NavDropdown, MenuItem, Nav } from 'react-bootstrap';

class Menu extends React.Component {
  render() {
      return (
        <Navbar bg="dark" variant="dark" expand="lg">
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="nav_links">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#about_me">About Me</Nav.Link>
              <Nav.Link href="#technical_work">Technical Work</Nav.Link>
              <Nav.Link href="#design_work">Design Work</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      );
  }
}

export default Menu;

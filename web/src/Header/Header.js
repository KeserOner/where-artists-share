// @flow

import React from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';
import { Link } from 'react-router-dom';

import banner from '../../assets/banner.jpg';

type State = {
  isOpen: boolean,
  title: string,
};

class Header extends React.Component<any, State> {
  toggle: Function;

  constructor() {
    super();

    this.toggle = this.toggle.bind(this);

    this.state = {
      isOpen: false,
      title: '',
    };
  }

  toggle() {
    this.setState({
      isOpen: !this.state.isOpen,
    });
  }

  render() {
    const bannerStyle = {
      height: '200px',
      backgroundImage: `url(${banner})`,
      backgroundPosition: 'center',
      backgroundSize: 'cover',
    };

    return (
      <div>
        <div style={bannerStyle} />
        <Navbar color="success" dark expand="md">
          <NavbarBrand href="/">WAS</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              <NavItem>
                <NavLink tag={Link} to="/">
                  Home
                </NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Navbar>
      </div>
    );
  }
}

export default Header;

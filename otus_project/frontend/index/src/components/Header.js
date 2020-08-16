import React from 'react';
import { NavLink }  from 'react-router-dom'
import { connect } from "react-redux";
import axios from "axios";
import { bindActionCreators } from "redux";
import { logOut } from '../actions/auth'
import { Cookies, withCookies } from 'react-cookie';
import { instanceOf } from 'prop-types';

class Header extends React.Component {
    constructor(props) {
      super(props)
    }

    logout = async () => {
      event.preventDefault();
      const url = 'http://127.0.0.1:8000/api-token/logout/';
      const data = {}
      let headers = {
        headers: {
          Authorization: `Token ${this.props.token}`
        }
      }
      const { cookies } = this.props;
      const logOut = this.props.logOut;

      let res = await axios.post(url, data, headers)

      logOut(null)
      cookies.remove('token', { path: '/' });
      this.setState({
        appLoaded: true,
        isAuthenticated: false,
        token: null
      })
    }
  render(){
    if (this.props.isAuthenticated){
      return (
        <header>
          <nav>
            <ul>
              <li><NavLink activeClassName="selected" to='/'>Home</NavLink></li>
              <li><NavLink activeClassName="selected" to='/token'>Token</NavLink></li>
              <li><NavLink activeClassName="selected" to='/my_courses'>My courses</NavLink></li>
              <li><NavLink activeClassName="selected" to='/login'>Login</NavLink></li>
            </ul>
          </nav>
          <button className="btn btn-primary" onClick={this.logout}>Log out</button>
        </header>
      )
    } else {
      return (
        <header>
          <nav>
            <ul>
              <li><NavLink activeClassName="selected" to='/'>Home</NavLink></li>
              <li><NavLink activeClassName="selected" to='/login'>Login</NavLink></li>
            </ul>
          </nav>
        </header>
      )
    }
  }
}

const mapStateToProps = (state) => {
  return {
    isAuthenticated: state.auth.isAuthenticated,
    token: state.auth.token
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    logOut: bindActionCreators(logOut, dispatch),
  };
};

  Header.propTypes = {
    cookies: instanceOf(Cookies)
  }

export default withCookies(connect(mapStateToProps, mapDispatchToProps)(Header));

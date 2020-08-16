import React from "react";
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import { Redirect } from 'react-router-dom';
import axios from 'axios';
import { axiosPost } from '../utils/API'
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
import { logIn, logOut } from '../actions/auth'


class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    const { cookies, isAuthenticated, token } = props;
    this.state = {
                  login: '',
                  password: '',
                  appLoaded: false,
                  isAuthenticated: isAuthenticated,
                  token: token,
                }
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
    this.login = this.login.bind(this);
  }

  handleUsernameChange(event){
    this.setState({login: event.target.value});
  }
  handlePasswordChange(event){
    this.setState({password: event.target.value});
  }

  checkAuth = async () => {
    const url = 'http://127.0.0.1:8000/api-token/check_auth_token/';
    const data = {}
    const logOut = this.props.logOut;
    const headers = {
      headers: {
        'Authorization': `Token ${this.state.token}`
      }
    }
    try {
      let result = await axios.post(url, data, headers)
      this.setState({
        appLoaded: true
      })
    } catch (err) {
      if (err.response.status == 401) {
        logOut(null)
        this.setState({
          appLoaded: true,
          isAuthenticated: false,
          token: null
        })
      }
    }
  }

  login = async () => {
    event.preventDefault();
    const url = 'http://127.0.0.1:8000/api-token/token/';
    const data = {
      username: this.state.login,
      password: this.state.password
    }
    const logIn = this.props.logIn;

    let res = await axios.post(url, data)

    logIn(res.data.token)
    const { cookies } = this.props;
    cookies.set('token', res.data.token, { path: '/' });
    this.setState({
      appLoaded: true,
      isAuthenticated: true,
      token: res.data.token
    })
  }

  render() {
    const loginForm = (
        <form>
          <div className="form-group">
            <label>Username</label>
            <input type="text" className="form-control" value={this.state.login} onChange={this.handleUsernameChange}/>
          </div>
          <div className="form-group">
            <label>Password</label>
            <input type="password" className="form-control" value={this.state.password} onChange={this.handlePasswordChange}/>
          </div>
          <button className="btn btn-primary" onClick={this.login}>Login</button>
        </form>
        )

    if (this.state.appLoaded) {
    return (
          <div className="mx-auto mt-4 text-center p-5">
            {this.state.token && <Redirect to="/my_courses"/>}
            {loginForm}
          </div>
        );
    }
    else {
      this.checkAuth()
      return (<div>Loading...</div>)
    }
  }
}

LoginForm.propTypes = {
    cookies: instanceOf(Cookies)
};

const mapStateToProps = (state) => {
  return {
    isAuthenticated: state.auth.isAuthenticated,
    token: state.auth.token
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    logIn: bindActionCreators(logIn, dispatch),
    logOut: bindActionCreators(logOut, dispatch)
  };
};

export default withCookies(connect(mapStateToProps, mapDispatchToProps)(LoginForm));

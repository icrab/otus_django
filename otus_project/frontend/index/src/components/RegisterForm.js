import React from "react";
import { Redirect } from 'react-router-dom';
import axios from 'axios';
import { axiosPost } from '../utils/API'
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
import { logIn } from '../actions/auth'


class RegisterForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
                  login: '',
                  password: '',
                  confirmPassword: '',
                  email: '',
                }
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
    this.handleConfirmPasswordChange = this.handleConfirmPasswordChange.bind(this);
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.register = this.register.bind(this);
  }

  handleUsernameChange(event){
    this.setState({login: event.target.value});
  }
  handlePasswordChange(event){
    this.setState({password: event.target.value});
  }
  handleConfirmPasswordChange(event){
    this.setState({confirmPassword: event.target.value});
  }
  handleEmailChange(event){
    this.setState({email: event.target.value});
  }

  register = () => {
    event.preventDefault();
    const url = 'http://127.0.0.1:8000/api-token/register/';
    const data = {
      username: this.state.login,
      email: this.state.email,
      password: this.state.password,
      confirm_password: this.state.confirmPassword,
    }
    const logIn = this.props.logIn;

    axios.post(url, data)
      .then(result =>{
        alert('register success')
        logIn(result.data.token)
      })
      .catch(err => {
        console.log(err.response.data)
        alert('register failed')
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
            <label>Email</label>
            <input type="text" className="form-control" value={this.state.email} onChange={this.handleEmailChange}/>
          </div>
          <div className="form-group">
            <label>Password</label>
            <input type="password" className="form-control" value={this.state.password} onChange={this.handlePasswordChange}/>
          </div>
          <div className="form-group">
            <label>Confim password</label>
            <input type="password" className="form-control" value={this.state.confirmPassword} onChange={this.handleConfirmPasswordChange}/>
          </div>
          <button className="btn btn-primary" onClick={this.register}>Register</button>
        </form>
        )

    return (
          <div className="mx-auto mt-4 text-center p-5">
            {this.props.isAuthenticated && <Redirect to="/my_courses"/>}
            {loginForm}
          </div>
        );
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
    logIn: bindActionCreators(logIn, dispatch),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(RegisterForm);

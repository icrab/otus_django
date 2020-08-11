import React from "react";
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import axios from 'axios';


class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    const { cookies } = props;
    this.state = {
                  login: '',
                  password: '',
                  token :'',
                  students:'',
                  token: cookies.get('token')
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

  login() {
    event.preventDefault();
    const redirect_url = window.location.origin + '/all_courses/';
    const url = 'http://127.0.0.1:8000/api-token/token/';
    const data = {
        username: this.state.login,
        password: this.state.password
      }

    axios.post(url, data)
      .then(res => {
        const { cookies } = this.props;
        cookies.set('token', res.data.token, { path: '/' });
        this.setState({token: res.data.token, login:'', password: ''});
        window.location.href = redirect_url;
      })
      .catch(err => {
          alert('Login failed')
        }
      );
  }

  render() {
    const courseDetails = (
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

        let courses = this.state.courses

    return (
          <div className="mx-auto mt-4 text-center p-5">
            {courseDetails}
          </div>
        );
      }
}

  LoginForm.propTypes = {
    cookies: instanceOf(Cookies)
  };

export default withCookies(LoginForm);

import React from "react";
import PropTypes from "prop-types";
import axios from 'axios';
import Students from './Students'

class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
                  login: '',
                  password: '',
                  token :'',
                  students:''
                }
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
    this.showWithToken = this.showWithToken.bind(this);
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
    let url = 'http://127.0.0.1:8000/api-token/token/';
    let data = {
        username: this.state.login,
        password: this.state.password
      }

    axios.post(url, data)
      .then(res => {
        this.setState({token: res.data.token, login:'', password: ''})
        this.showWithToken()
      })
      .catch(err => {
          alert('Login failed')
        }
      );
  }

  showWithToken(){
    event.preventDefault();
    let url = 'http://127.0.0.1:8000/api-token/user_student/';
    let data = {
          headers: { Authorization: `Token ${this.state.token}` }
      }

    axios.get(url, data)
      .then(res => {
        this.setState({students: res.data})
      })
      .catch(err => {
          console.log(err)
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

        let students = this.state.students

    return (
          <div className="mx-auto mt-4 text-center p-5">
            {!students && courseDetails}
            {students ? students.map(stud => <Students name={stud.first_name} email={stud.email} key={stud.id}/>) : <div>Please log in</div>}
          </div>
        );
      }
}

export default LoginForm;

import React from "react";
import { Redirect } from 'react-router-dom';
import {axiosGet, axiosPost} from "../utils/API.js";
import { bindActionCreators } from "redux";
import { connect } from "react-redux";
import { logIn } from '../actions/auth'


class Token extends React.Component {
  constructor(props) {
    super(props);
  }
  updateToken = () => {
     const logIn = this.props.logIn;
     const url = 'http://127.0.0.1:8000/api-token/refresh_auth_token/';
     const data = {}
     const headers = { headers: { 'Authorization': `Token ${this.props.token}` } }
     const then_handler = ( response => {
          logIn(response.data.token)
       })
     const catch_handler = ( err => {
         console.log(err)
         alert('Something went wrong')
       })
    axiosPost(url, data, headers, then_handler, catch_handler)

  }

  render() {
    const updateToken = (
      <div>
        <div>
          <h4>Current Token:</h4>
          <span>{this.props.token}</span>
          </div>
        <button className="btn btn-primary" onClick={this.updateToken}>Update Token</button>
      </div>
    )

    return (
          <div className="mx-auto mt-4 text-center p-5">
            {!this.props.isAuthenticated && <Redirect to="/login"/>}
            {updateToken}
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

export default connect(mapStateToProps, mapDispatchToProps)(Token);

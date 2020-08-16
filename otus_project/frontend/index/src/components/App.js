import React from 'react';
import { instanceOf } from 'prop-types';
import AllCourses from "./AllCourses"
import Header from "./Header"
import Token from "./Token"
import LoginForm from "./LoginForm"
import DetailCourse from "./DetailCourse"
import StudentCourses from "./StudentCourses"

import axios from "axios";
import { Switch, Route, Redirect } from 'react-router-dom'
import { Cookies, withCookies } from 'react-cookie';
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import { logIn } from '../actions/auth'

class App extends React.Component {
  constructor(props){
    super(props)
    const { cookies } = props;
    this.state = {appLoaded: false}
  }

  componentDidMount(){
    const token = this.props.cookies.get('token')
    const logIn = this.props.logIn;
    if (token){
      logIn(token)
      this.setState({appLoaded: true, isAuthenticated:true})
    } else {
      this.setState({appLoaded: true, isAuthenticated:false})
    }
}

  render(){
    if (this.state.appLoaded && this.state.isAuthenticated){
      return (
            <div>
              <Header/>
              <Switch>
                <Route path='/login' component={() => <LoginForm token={this.props.token}/>}/>
                <Route path='/courses/:id' component={(props) => <DetailCourse {...props} isAuthenticated={this.props.isAuthenticated} token={this.props.token}/>}/>
                <Route path='/token' component={() => <Token isAuthenticated={this.props.isAuthenticated} token={this.props.token}/>}/>
                <Route path ="/my_courses" component={() => <StudentCourses isAuthenticated={this.props.isAuthenticated} token={this.props.token}/>}/>
                <Route path ="/" component={() => <AllCourses isAuthenticated={this.props.isAuthenticated} token={this.props.token}/>}/>
              </Switch>
            </div>
      )
    } else if (this.state.appLoaded) {
            return (
              <div>
                <Header/>
                <Switch>
                  <Route path='/courses/:id' component={(props) => <DetailCourse {...props} isAuthenticated={this.props.isAuthenticated} token={this.props.token}/>}/>
                  <Route path='/login' component={() => <LoginForm token={this.props.token}/>}/>
                  <Route path ="/" component={() => <AllCourses isAuthenticated={this.props.isAuthenticated} token={this.props.token}/>}/>
                </Switch>
              </div>
          )
      } else {
      return (<div>Loading...</div>)
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
    logIn: bindActionCreators(logIn, dispatch),
  };
};

  App.propTypes = {
    cookies: instanceOf(Cookies)
  }

export default withCookies(connect(mapStateToProps, mapDispatchToProps)(App));

import React from 'react';
import AllCourses from "./AllCourses"
import Header from "./Header"
import Token from "./Token"
import LoginForm from "./LoginForm"
import DetailCourse from "./DetailCourse"
import StudentCourses from "./StudentCourses"
import RegisterForm from "./RegisterForm"

import axios from "axios";
import { Switch, Route, Redirect } from 'react-router-dom'
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import { logIn } from '../actions/auth'

class App extends React.Component {
  constructor(props){
    super(props)
  }

  render(){
    if (this.props.isAuthenticated){
      return (
            <div>
              <Header/>
              <Switch>
                <Route path='/courses/:id' component={(props) => <DetailCourse {...props}/>}/>
                <Route path='/token' component={() => <Token/>}/>
                <Route path ="/my_courses" component={() => <StudentCourses/>}/>
                <Route path ="/" component={() => <AllCourses/>}/>
              </Switch>
            </div>
      )
    } else {
            return (
              <div>
                <Header/>
                <Switch>
                  <Route path='/courses/:id' component={(props) => <DetailCourse {...props} />}/>
                  <Route path='/login' component={() => <LoginForm/>}/>
                  <Route path='/register' component={() => <RegisterForm/>}/>
                  <Route path ="/" component={() => <AllCourses/>}/>
                </Switch>
              </div>
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
    logIn: bindActionCreators(logIn, dispatch),
  };
};


export default connect(mapStateToProps, mapDispatchToProps)(App);

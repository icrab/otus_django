import React from "react";
import axios from 'axios';
import Course from "./Course"
import { Redirect } from 'react-router-dom';

class StudentCourses extends React.Component {
  constructor(props) {
    super(props);
    this.state = {results:false}
  }

  componentDidMount() {
    if (this.props.token) {
      let url = 'http://127.0.0.1:8000/api-token/user_courses/';
      let headers = {
        headers: {
          Authorization: `Token ${this.props.token}`
        }
      }
      axios.get(url, headers)
        .then(courses => {
          this.setState({
            results: courses.data
          });
        })
        .catch(err => {
          console.log(err)
          alert('Something went wrong')
        })
    }
  }

  render() {
    return (
      <div>
          {!this.props.isAuthenticated && <Redirect to="/login"/>}
          {this.state.results && this.state.results.map(course =>
            <Course userSingUp={true} isAuthenticated={this.props.isAuthenticated}  key={course.id} id={course.id} name={course.title} cost={course.cost}/>)}
      </div>
    )
  }
}

export default StudentCourses;

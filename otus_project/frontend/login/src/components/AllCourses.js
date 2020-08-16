import React from "react";
import axios from 'axios';
import Course from "./Course"
import { Redirect } from 'react-router-dom';

class AllCourses extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        results: false
      }
    }

    componentDidMount() {
      let url = 'http://127.0.0.1:8000/api-token/courses/';
      axios.get(url)
        .then(courses => {
          this.setState({
            results: courses.data
          });
        })
        .catch(err => {
          console.log(err)
          alert('Something went wrong')
        })
    }  render() {
    return (
      <div>
          {this.state.results && this.state.results.map(course =>
            <Course userSingUp={false} isAuthenticated={this.props.isAuthenticated} token={this.props.token} key={course.id} id={course.id} name={course.title} cost={course.cost}/>)
          }
      </div>
    )
  }
}

export default AllCourses;

import React from "react";
import axios from 'axios';
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import Courses from "./Courses.js";

class App extends React.Component {
  constructor(props) {
    super(props);
    const { cookies } = props;
    this.state = {
      token: cookies.get('token'),
      results: ''
  }
}

  componentDidMount() {
    let url = 'http://127.0.0.1:8000/api-token/course/';
    let data = {
          headers: { Authorization: `Token ${this.state.token}` }
      }
    axios.get(url, data)
      .then(courses => {
        this.setState({results:courses.data});
      })
      .catch(err => {
        alert(err)
      })
  }

  render() {
    return (
      <div>
        {this.state.results && this.state.results.map(course => <Courses key={course.id} id={course.id} name={course.title} cost={course.cost}/>)}
      </div>
    )
  }
}

export default withCookies(App);

import React from "react";
import axios from 'axios';
import Course from "./Course";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      results: {}
  }
}

  componentDidMount() {
    let url = 'http://127.0.0.1:8000/api-token/course/';
    axios.get(url)
      .then(courses => {
        this.setState({results:courses});
      })
  }

  render() {
    return (
      <div>
        {this.state.results.data && this.state.results.data.map((course, index) => <Course key={index} name={course.title} cost={course.cost}/>)}
      </div>
    )
  }
}

export default App;

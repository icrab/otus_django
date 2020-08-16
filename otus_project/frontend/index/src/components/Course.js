import React from "react";
import axios from "axios";
import { axiosGet } from "../utils/API.js"
import { NavLink }  from 'react-router-dom'

class Course extends React.Component {
  constructor(props) {
    super (props);
    this.state = {
      courseDetail: false,
    }
    this.SignUpOnCourse = this.SignUpOnCourse.bind(this);
  }

  SignUpOnCourse(){
    const url = 'http://127.0.0.1:8000/api-token/sign_up_on_course/';
    const data = {
                  course: this.props.id,
                }
    const headers = { headers: { 'Authorization': `Token ${this.props.token}` } }

    axios.post(url, data, headers)
      .then(result =>{
        alert('all right')
      })
      .catch(err => {
        alert('failed')
      })

  }
  render() {
    const { id, name, cost, userSingUp, isAuthenticated } = this.props;
    const url = '/courses/' + id;
    const allCourse = (
          <div>
            <div>
            <h4 className="mb-0"><NavLink activeClassName="selected" to={url}>{name}</NavLink></h4>
            <span className="text-muted">{cost}</span>
            </div>
            {!userSingUp && isAuthenticated && <button type="button" className="btn subscribe" onClick={this.SignUpOnCourse}>Записаться</button>}
          </div>
        );
    return (
        <div>
          <div className="mx-auto mt-4 text-center p-5">
            {allCourse}
          </div>
        </div>
        );
  }
}

export default Course;

import React from "react";
import axios from "axios";
import { instanceOf } from 'prop-types';
import { Cookies, withCookies } from 'react-cookie';
import {axiosGet} from "../utils/API.js"

class Courses extends React.Component {
  constructor(props) {
    super (props);
    const {cookies} = props;
    this.state = {
      courseDetail: false,
      token: cookies.get('token')
    }
    this.SignUpOnCourse = this.SignUpOnCourse.bind(this);
  }

  SignUpOnCourse(){
    const url = 'http://127.0.0.1:8000/api-token/sign_up_on_course/';
    const data = {
                  course: this.props.id,
                }
    const headers = { headers: { 'Authorization': `Token ${this.state.token}` } }

    axios.post(url, data, headers)
      .then(result =>{
        alert('all right')
      })
      .catch(err => {
        alert('failed')
      })

  }
  render() {
    const { id, name, cost } = this.props;
    let url = window.location.origin + '/print_course/' + id + '/'
    const allCourse = (
          <div>
            <div>
            <h4 className="mb-0"><a href={url}>{name}</a></h4>
            <span className="text-muted">{cost}</span>
            </div>
            <button type="button" className="btn subscribe" onClick={this.SignUpOnCourse}>Записаться</button>
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

  Courses.propTypes = {
    cookies: instanceOf(Cookies)
  }

export default withCookies(Courses);

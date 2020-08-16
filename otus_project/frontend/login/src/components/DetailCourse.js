import React from "react";
import { NavLink }  from 'react-router-dom'
import {axiosGet, axiosPost} from "../utils/API.js";
import { Redirect } from 'react-router-dom';
import Lesson from './Lesson.js';

class DetailCourse extends React.Component {
    constructor(props) {
      super(props)
      this.state = ({
        course: false,
      })
      console.log(this.props)
      this.SignUpOnCourse = this.SignUpOnCourse.bind(this);
    }

    componentDidMount() {
      const courseUrl = 'http://127.0.0.1:8000/api-token/courses/'
      const id = this.props.match.params.id
      const url = courseUrl + id
      const data = {}
      let headers = {}
      if (this.props.token) {
        headers = {
          headers: {
            'Authorization': `Token ${this.props.token}`
          }
        }
      }
      const then_handler = (course => {
        this.setState({
          course: course.data
        })
      })
      const catch_handler = (err => {
        console.log(err)
        alert('Something went wrong')
      })
      axiosGet(url, headers, then_handler, catch_handler)
    }

    SignUpOnCourse() {
      const url = 'http://127.0.0.1:8000/api-token/sign_up_on_course/';
      const data = {
        course: this.state.course.id
      }
      const headers = {
        headers: {
          'Authorization': `Token ${this.props.token}`
        }
      }

      let then_handler = (result => {
        alert('all right')
        console.log(result)
      })
      let catch_handler = (err => {
        alert('failed')
        console.log(err)
      })
      axiosPost(url, data, headers, then_handler, catch_handler)
    }
 render(){
    if (this.state.course) {
      const courseDetails = (
        <div className="modal" id="detailCourse" style={{display: 'block'}}>
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">{this.state.course.title}</h5>
                <NavLink className="close" aria-label="Close" to="/courses">
                  <span aria-hidden="true">&times;</span>
                </NavLink>
              </div>
              <div className="modal-body">
                <span> Цена за курс: {this.state.course.cost}</span>
                <h6>Список тем:</h6>
                <ul>
                {this.state.course.lessons.map((lesson) => (<Lesson key={lesson.id} title={lesson.title}/>))}
                </ul>
              </div>
              <div className="modal-footer">
                {this.props.isAuthenticated && <button type="button" className="btn btn-secondary" id="signUp" onClick={this.SignUpOnCourse} data-dismiss="modal">Записаться на курс</button>}
              </div>
            </div>
          </div>
        </div>
      )
      return (<div>{courseDetails}</div>)
    }
    return (<div></div>)

   }
}

export default DetailCourse;

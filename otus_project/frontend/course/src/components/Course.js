import React from "react";
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import {axiosGet, axiosPost} from "../utils/API.js";
import Lesson from './Lesson.js';

class Course extends React.Component {
  constructor(props) {
    super (props)
    const { cookies } = props;
    this.state = ({
          course: false,
          token: cookies.get('token')
        })
    this.close = this.close.bind(this);
    this.SignUpOnCourse = this.SignUpOnCourse.bind(this);
  }

  componentDidMount() {
     const courseUrl = 'http://127.0.0.1:8000/api-token/user_course/'
     const id = window.location.pathname.split('/')[2]
     const url = courseUrl + id
     const data = {}
     const headers = { headers: { 'Authorization': `Token ${this.state.token}` } }
     const then_handler = ( course => {
        this.setState({course:course.data})
       })
     const catch_handler = ( err => {
         alert('error')
         console.log(err)
       })
    axiosGet(url, headers, then_handler, catch_handler)
  }

  close(){
    const redirect_url = window.location.origin + '/all_courses/';
    window.location.href = redirect_url;
  }

  SignUpOnCourse(){
    const url = 'http://127.0.0.1:8000/api-token/sign_up_on_course/';
    const data = { course: this.state.course.id }
    const headers = { headers: { 'Authorization': `Token ${this.state.token}` } }

    let then_handler = ( result => {
        alert('all right')
        console.log(result)
      } )
    let catch_handler = ( err => {
        alert('failed')
        console.log(err)
      })
    axiosPost(url, data, headers, then_handler, catch_handler)
  }

 render(){
    if (this.state.course) {
      let courseDetails = (
        <div className="modal" id="detailCourse" style={{display: 'block'}}>
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">{this.state.course.title}</h5>
                <button type="button" className="close" onClick={this.close} data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div className="modal-body">
                <span> Цена за курс: {this.state.course.cost}</span>
                <h6>Список тем:</h6>
                <ul>
                {this.state.course.lessons.map((lesson) => (<Lesson key={lesson.id} title={lesson.title}/>))}
                </ul>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" id="signUp" onClick={this.SignUpOnCourse} data-dismiss="modal">Записаться на курс</button>
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

export default withCookies(Course)

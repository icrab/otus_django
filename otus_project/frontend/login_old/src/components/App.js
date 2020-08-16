import React from "react";
import axios from 'axios';
import LoginForm from "./LoginForm";
import Courses from "./Courses"
import { instanceOf } from 'prop-types';
import { CookiesProvider, Cookies, withCookies} from 'react-cookie';

class App extends React.Component {
  constructor(props) {
    super(props);
    const { cookies } = props;
    this.state = { token: cookies.get('token'), results: false }
    this.handler = this.handler.bind(this)
  }

  handler(val) {
    this.setState({ token: val })
    console.log('token update')
    this.componentDidMount()
  }

  componentDidMount() {
    if (this.state.token){
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
  }

  render() {
    return (
      <CookiesProvider>
        {!this.state.token && <LoginForm handler = {this.handler}/>}
        {this.state.results && this.state.results.map(course => <Courses key={course.id} id={course.id} name={course.title} cost={course.cost}/>)}
      </CookiesProvider>
    )
  }
}

  App.propTypes = {
    cookies: instanceOf(Cookies)
  };

export default withCookies(App);

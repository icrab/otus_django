import React from "react";
import PropTypes from "prop-types";


class Students extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    console.log(this.props.students)
    const username = this.props.name
    const email = this.props.email

    return (
      <li>
      {username}, {email}
      </li>
    )
  }
}

export default Students;

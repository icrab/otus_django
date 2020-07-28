import React from "react";
import PropTypes from "prop-types";

class Course extends React.Component {
  render() {
    const { name, cost } = this.props;
    const courseDetails = (
          <div>
            <h4 className="mb-0">{name}</h4>
            <span className="text-muted">{cost}</span>
          </div>
        );
    return (
          <div className="mx-auto mt-4 text-center p-5">
            {courseDetails}
          </div>
        );
  }
}

export default Course;

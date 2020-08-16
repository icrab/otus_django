import React from "react";

class Lesson extends React.Component {
  constructor(props) {
    super (props)

  }
 render(){
    const { title } = this.props;
    let lesson = (<li>{title}</li>)
    return (<div>{lesson}</div>)
   }
}

export default Lesson;

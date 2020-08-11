import React from "react";
import { CookiesProvider } from 'react-cookie';
import axios from 'axios';
import Course from "./Course.js";

class App extends React.Component {
  constructor(props) {
    super(props);
}

  render() {
    return (
      <CookiesProvider>
        <Course/>
      </CookiesProvider>
    )
  }
}

export default App;

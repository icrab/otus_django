import React from "react";
import LoginForm from "./LoginForm";
import { CookiesProvider } from 'react-cookie';

class App extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <CookiesProvider>
        <LoginForm />
      </CookiesProvider>
    )
  }
}

export default App;

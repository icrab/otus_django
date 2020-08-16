import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App'
import Header from './components/Header'
import { createStore } from "redux";
import { Provider } from "react-redux";
import { rootReducer } from './reducers/root'
import { HashRouter } from 'react-router-dom'

const store = createStore(rootReducer)

ReactDOM.render(
  <Provider store={store}>
    <HashRouter>
      <App />
    </HashRouter>
  </Provider>,
  document.getElementById('root')
);

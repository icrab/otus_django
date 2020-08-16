import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App'
import Header from './components/Header'
import { applyMiddleware, createStore } from "redux";
import { Provider } from "react-redux";
import { rootReducer } from './reducers/root'
import { HashRouter } from 'react-router-dom'
import { save, load } from "redux-localstorage-simple"


const createStoreWithMiddleware
    = applyMiddleware(
        save()
    )(createStore)

const store = createStoreWithMiddleware(
    rootReducer,
    load()
)

ReactDOM.render(
  <Provider store={store}>
    <HashRouter>
      <App />
    </HashRouter>
  </Provider>,
  document.getElementById('root')
);

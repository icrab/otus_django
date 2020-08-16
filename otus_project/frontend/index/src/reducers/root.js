import { authReducer } from './auth'
import { combineReducers } from 'redux'

export const rootReducer = combineReducers({
  auth: authReducer,
})
//export const rootReducer = authReducer

import axios from 'axios'

export function axiosGet(url, headers, then_handler, catch_handler){
     axios.get(url, headers)
      .then(then_handler)
      .catch(catch_handler)
}

export function axiosPost(url, data, headers, then_handler, catch_handler){
     axios.post(url, data, headers)
      .then(then_handler)
      .catch(catch_handler)
}

import axios from 'axios'

export function axiosGet(url, handler){
     axios.get(url)
      .then(handler)
}

export function axiosPost(url, handler){
     axios.post(url)
      .then(handler)
}

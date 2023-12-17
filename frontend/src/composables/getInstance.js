// Composable function to get a single instance from the backend
//author: xfratr01

import axios from 'axios'

const getInstance = (id) => {
  const url = 'http://localhost:5000/instance/' + id

  return axios.get(url)
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
      return null
    })
}


export default getInstance
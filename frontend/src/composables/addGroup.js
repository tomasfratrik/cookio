// author: xfratr01
import axios from 'axios'

const addGroup = (name) => {
    const group = {
      name: name
    }

    const url = `http://localhost:5000/groups`
    return axios.post(url, group)
      .then((response) => {
          return response.data
      })
}


export default addGroup
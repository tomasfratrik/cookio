// author: xfratr01
import axios from 'axios'

const deleteGroup = (name) => {

    const url = `http://localhost:5000/groups/${name}`
    return axios.delete(url)
      .then((response) => {
          return response.data
      })
}


export default deleteGroup
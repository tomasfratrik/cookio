import axios from 'axios'

const updateInstance = (instance) => {
  const url = `http://localhost:5000/instance/${instance.id}`
  return axios.put(url, instance)
      .then(response => {
          return response.data
      })
}


export default updateInstance
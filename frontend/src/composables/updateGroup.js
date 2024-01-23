// Composable function to update a recipe class
//author: xfratr01

import axios from 'axios'

const updateGroup = (old_gp, new_gp) => {
  const url = `http://localhost:5000/groups`
  const group = {
    old_name: old_gp.name,
    new_name: new_gp.rename_name,
  }
  return axios.put(url, group)
      .then(response => {
        return response.data
      })
      .catch(error => {
          return null
      })
}


export default updateGroup
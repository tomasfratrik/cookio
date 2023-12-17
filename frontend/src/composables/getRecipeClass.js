// Purpose: Gets a recipe class from the backend by id.
//author: xfratr01

import axios from 'axios'

const getRecipeClass = (id) => {
  const url = `http://localhost:5000/recipes/${id}`

  return axios.get(url)
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
      return null
    })
}


export default getRecipeClass
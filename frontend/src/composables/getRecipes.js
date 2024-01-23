// Composable function to get recipes from the backend
//author: xfratr01

import axios from 'axios'

const getRecipes = () => {
  const url = 'http://localhost:5000/recipes'
  return axios.get(url)
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
      return null
    })
}


export default getRecipes
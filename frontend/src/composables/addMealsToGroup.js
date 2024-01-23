// Composable function to update a recipe class
//author: xfratr01

import axios from 'axios'

const addMealsToGroup = (name, meal_id_list) => {
  const url = `http://localhost:5000/groups/${name}/meals`
  const list = {
    meals: meal_id_list,
  }
  return axios.put(url, list)
      .then(response => {
        return response.data
      })
      .catch(error => {
          return null
      })
}


export default addMealsToGroup
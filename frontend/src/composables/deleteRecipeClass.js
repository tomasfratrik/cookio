// Purpose: composable for deleting a recipe class from the database
// author: xfratr01
import axios from 'axios'

const deleteRecipeClass = (id) => {
      const url = `http://localhost:5000/recipes/${id}`
      return axios.delete(url)
        .then((response) => {
            return response.data
        })
}


export default deleteRecipeClass
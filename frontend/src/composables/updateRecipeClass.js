import axios from 'axios'

const updateRecipeClass = (recipe) => {
  const id = recipe.id
  const url = `http://localhost:5000/recipe_classes/${id}`
  const recipeClass = {
      class_name: recipe.class_name,
      class_desc: recipe.class_desc,
  }
  return axios.put(url, recipeClass)
      .then(response => {
        return response.data
      })
      .catch(error => {
          return null
      })
}


export default updateRecipeClass
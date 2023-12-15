import axios from 'axios'

const deleteRecipeClass = (id) => {
      const url = `http://localhost:5000/recipes/${id}`
      return axios.delete(url)
        .then((response) => {
            return response.data
        })
}


export default deleteRecipeClass
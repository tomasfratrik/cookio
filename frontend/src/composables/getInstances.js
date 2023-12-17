// Composable function to retrieve instances of a recipe class from the backend
//author: xfratr01

import axios from 'axios'

const getInstances = (id) => {
    const url = `http://localhost:5000/recipe_classes/${id}/instances`
    return axios.get(url)
        .then(response => {
            return response.data
        })
}


export default getInstances
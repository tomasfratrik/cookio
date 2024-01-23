//author: xfratr01

import axios from 'axios'

const getGroups = (id) => {
    const url = `http://localhost:5000/groups`
    return axios.get(url)
        .then(response => {
            return response.data
        })
}

export default getGroups
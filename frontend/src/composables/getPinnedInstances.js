// Composable function to retrieve all pinned instances from the backend
//author: xfratr01

import axios from 'axios'

const getPinnedInstances = () => {
    const url = `http://localhost:5000/instance/pinned`
    return axios.get(url)
        .then(response => {
            return response.data
        })
}


export default getPinnedInstances
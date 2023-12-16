import axios from 'axios'

const getPinnedInstances = () => {
    const url = `http://localhost:5000/instance/pinned`
    return axios.get(url)
        .then(response => {
            return response.data
        })
}


export default getPinnedInstances
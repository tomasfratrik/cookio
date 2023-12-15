
import axios from 'axios'

const deleteInstance = (id) => {
    const url = `http://localhost:5000/instance/${id}`
    return axios.delete(url)
        .then(response => {
            return response.data
        })
}


export default deleteInstance
// author: xfratr01
import axios from 'axios'

const deleteInstanceFromGroup = (group_name, instance_id) => {
    const url = `http://localhost:5000/groups/${group_name}/meals/${instance_id}`
    return axios.delete(url)
        .then(response => {
            return response.data
        })
}


export default deleteInstanceFromGroup
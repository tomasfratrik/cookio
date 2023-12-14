<template>
    <div class="AssignRecipeClass">
        <div class="left">
            left
        </div>
        <div class="right">
            <form @submit.prevent="handleSubmit">
                <label>Class recipe name:</label>
                <input type="text" v-model="className" required>
                <label>Class description:</label>
                <textarea v-model="classDesc" required></textarea>
                <button class="btn-create">Create</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            className: '',
            classDesc: '',
        }
    },
    methods: {
        handleSubmit() {
            const recipeClass = {
                class_name: this.className,
                class_desc: this.classDesc,
            }
            const url = 'http://localhost:5000/recipe_classes'
            axios.post(url, recipeClass)
                .then(response => {
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.className = ''
            this.classDesc = ''
             
        }
    },
    mounted() {
        // get all recipes
        const url = 'http://localhost:5000/recipe_classes'
        axios.get(url)
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
        

    }

}
</script>

<style>
.AssignRecipeClass {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

.btn-create {
    padding: 10px;
    background-color: white;
    text-decoration: none;
    color: var(--primary-color);
    cursor: pointer;
    font-size: 20px;
    border-radius: 5px;
    border: 1px solid var(--primary-color);
    transition: all 0.2s ease-in-out;
}

.btn-create:hover {
    background-color: var(--primary-color);
    color: white;
}

.right form {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}

</style>

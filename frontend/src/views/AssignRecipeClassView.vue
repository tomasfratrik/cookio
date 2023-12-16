<template>
    <div class="AssignRecipeClass">
        <div class="left">
            <div class="box">
                <div class="recipe" v-for="recipe in recipes" :key="recipe.id" @click="select(recipe)">
                    <h2>{{ recipe.class_name }}</h2>
                    <p>{{ recipe.class_desc }}</p>
                </div>
            </div>
        </div>
        <div class="right">
            <form @submit.prevent="handleSubmit">
                <label>Class recipe name:</label>
                <input type="text" v-model="className" required>
                <div v-if="classNameError" class="error-one-liner">
                    Class name must be at least 3 characters long
                </div>
                <label>Class description:</label>
                <textarea v-model="classDesc" ></textarea>
                <button class="btn-create">Create</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import getRecipes from '@/composables/getRecipes'

export default {
    data() {
        return {
            className: '',
            classDesc: '',
            recipes: [],
            classNameError: false,
            classDescError: false,
        }
    },
    methods: {
        handleSubmit() {
            if (this.className.length < 3) {
                this.classNameError = true
                return
            } else {
                this.classNameError = false
            }


            const recipeClass = {
                class_name: this.className,
                class_desc: this.classDesc,
            }
            const url = 'http://localhost:5000/recipe_classes'
            axios.post(url, recipeClass)
                .then(response => {
                    const insntance = response.data
                    const intanceId = insntance.id
                    console.log(intanceId)
                    this.updateRecipes()
                    this.$router.push({ name: 'InstanceDetail', params: { id: intanceId } })
                })
                .catch(error => {
                    console.log(error)
                })

            // reset form
            this.className = ''
            this.classDesc = ''


        },
        updateRecipes() {
            getRecipes()
                .then((data) => {
                    this.recipes = data
                })
        },
        select(recipe_class) {
            console.log(recipe_class)
            console.log(recipe_class.class_name)
            this.className = recipe_class.class_name
            this.classDesc = recipe_class.class_desc
        }

    },
    mounted() {
        getRecipes()
            .then((data) => {
                this.recipes = data
            })
    }
}
</script>

<style scoped>
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
.box {
    border: 1px solid black;
    width: 300px;
    border-radius: 5px;
    padding: 10px;
    height: 300px;
    overflow: scroll;
}
</style>

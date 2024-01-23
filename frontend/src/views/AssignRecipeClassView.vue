<!-- ITU project 
  -- AUTHOR: xkvasn16
-->
<template>
    <div class="AssignRecipeClass">
        <div class="header">
            <h1>Where should be meal created?</h1>
            <p>Crete own by typing name of different recipe that doesn't yet exist</p>
            <p>Or crete meal under already existing recipe by clicking at it, in left panel</p>
            <input type="text" v-model="search" placeholder="Search">
        </div>
        <div class="row">
            <div class="left">
                <div class="box">
                    <div class="recipe" v-for="recipe in filteredRecipes" :key="recipe.id" @click="select(recipe)">
                        <h2>{{ recipe.class_name }}</h2>
                    </div>
                </div>
            </div>
            <div class="right">
                <form @submit.prevent="handleSubmit">
                    <div class="Class_name">
                        <label>Recipe name:</label>
                        <br>
                        <input type="text" v-model="className" required>
                    </div>
                    <div v-if="classNameError" class="error-one-liner">
                        Class name must be at least 3 characters long
                    </div>
                    <div class="Class_desc">
                        <label>Recipe description:</label>
                        <br>
                        <textarea v-model="classDesc" ></textarea>
                        <br>
                        <button class="btn-create">Create</button>
                    </div>
                </form>
            </div>
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
            search: '',
        }
    },
    methods: {
        // after we press submit, assign class
        handleSubmit() {

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
        // fetch all recipes
        updateRecipes() {
            getRecipes()
                .then((data) => {
                    this.recipes = data
                })
        },
        // select recipe
        select(recipe_class) {
            console.log(recipe_class)
            console.log(recipe_class.class_name)
            this.className = recipe_class.class_name
            this.classDesc = recipe_class.class_desc
        }

    },
    mounted() {
        // fetch all recipes
        getRecipes()
            .then((data) => {
                this.recipes = data
            })
    },
    // filter recipes based on search
    computed: {
        filteredRecipes() {
            return this.recipes.filter(item => item.class_name.includes(this.search));
        }
    }
}
</script>

<style scoped>

.recipe:hover {
    background-color: var(--secondary-color);
    color: white;
    cursor: pointer;
}
.row {
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
    width: 100px;
    height: 50px;
    font-weight: bold;
    font-family: sans-serif;

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
    width: 400px;
    border-radius: 5px;
    padding: 10px;
    height: 300px;
    overflow: scroll;
}
.right{
    width: 50%;
}
.Class_name{ 
    text-align: center;
}
.Class_desc{ 
    text-align: center;
}
label{
    font-size: 25px;
    color: var(--primary-color);
    font-weight: bold;
    font-family: sans-serif;
}
textarea {
    font-size: 20px;
    padding: 5px;
    width: 300px; /* Šířka inputu a textarea */
    height: 150px; /* Šířka inputu a textarea */
    margin-bottom: 10px;
    }   
input{
    font-size: 20px;
    padding: 5px;
    margin-bottom: 10px;
}
h2{
    font-size: 20px;
    font-weight: bold;
    font-family: sans-serif;
}
p{
    font-size: 15px;
    font-weight: bold;
    font-family: sans-serif;
}

.header {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.recipe h2 {
    max-width: 100%;
}
</style>

<template>
    <div class="InstanceDetailView">       
        <div v-if="toggleModal">
            <Modal @close="toggleModal_">
                <form @submit.prevent="addIngredient">
                    <label style="margin-right: 10px;">Ingredient name</label>           
                    <input v-model="ingredientName" placeholder="Search ..." @click="activate_searching" class="search-input"/>
                    <ul v-if="searching_allowed" class="result-list">
                        <li v-for="item in filteredList" @click="set_searching(item)" class="result-list li">
                            {{ item }}
                        </li>
                    </ul>
                        

                    <label>Select Unit</label>
                    <select v-model="unit">
                        <option>Grams</option>
                        <option>Kilograms</option>
                        <option>Handfuls</option>
                        <option>Liters</option>
                        <option>Mililiters</option>
                        <option>Centiliters</option>
                        <option>Cups</option>
                        <option>Ounces</option>
                        <option>Teaspoons</option>
                        <option>Tablespoons</option>
                        <option>Pounds</option>
                    </select>
                    <label>Quantity</label>
                    <input type="range" v-model="quantity" min="0" max="100000" step="1">
                        <span>
                            <input type="number" v-model="quantity" required placeholder="Choose quantity">
                        </span>
                    <div style="display: flex; align-items: center;">
                        <button class="btn-create">Add</button>
                        <button @click="toggleModal_" class="btn-create">Close</button>
                    </div>
                </form>
            </Modal>
        </div>
        <label>Edit </label>
        <label class="switch">
            <input type="checkbox" v-model="edit">
            <span class="round slider"></span>
        </label>
        <div v-if="edit">
            <form @submit.prevent="handleSubmit">
                <label>Name</label>
                <input type="text" v-model="instance.name">
                <label>Description</label>
                <input type="text" v-model="instance.desc">
                <label>Rating</label>
                <input type="number" v-model="instance.rating">
                <label>Pinned</label>
                <input type="checkbox" v-model="instance.pinned">
                <button class="btn-create">Save</button>
            </form>
        </div>
        <div v-else>
            <h1>{{ instance.name }}</h1>
            <p>{{ instance.desc }}</p>
            <p v-if="instance.rating >= 0"> Rating: {{ instance.rating }}</p>
            <p v-else> Rating: not rated yet!</p>
            <p>Pinned:</p>
            <input disabled="true" type="checkbox" v-model="instance.pinned">
            <h2>Ingredients: </h2>
            <button @click="toggleModal_">Add Ingredients</button>
            <div v-if="ingredients.length === 0">
                <p>No ingredients</p>
            </div>
            <div v-else>
                <ul>
                    <li v-for="ingredient in ingredients" :key="ingredient.name">
                        {{ ingredient.name }} - {{ ingredient.quantity }} -  {{ ingredient.unit }} 
                        <button class="btn-delete" @click="deleteIngredient(ingredient)">Delete</button>
                    </li>
                </ul>
            </div>
        </div>

    </div>
</template>

<script>
import getInstance from '@/composables/getInstance'
import updateInstance from '@/composables/updateInstance'
import Modal from '@/components/Modal.vue'
import axios, { all } from 'axios'
export default {
    components: {
        Modal,
    },
    data() {
        return {
            recipes: [],
            instance: {},
            ingredients: [],
            unique_ingredients: [],
            searching_allowed: false,
            toggleModal: false,
            ingredientName: '',
            unit: '',
            quantity: '',
            edit:  false,
        }
    },
    methods: {
        handleSubmit() {
            updateInstance(this.instance)
                .then(() => {
                    console.log('updated instance')
                    this.edit = false
                })
        },
        toggleModal_() {
            this.toggleModal = !this.toggleModal
        },
        addIngredient() {
            const ingredient = {
                name: this.ingredientName,
                unit: this.unit,
                quantity: this.quantity,
            }
            const url = `http://localhost:5000/instance/${this.instance.id}/ingredients`
            axios.post(url, ingredient)
                .then(response => {
                    const ingredients = response.data
                    this.ingredients = ingredients
                    // const ingredient = response.data
                    // this.instance.ingredients.push(ingredient)
                    // this.ingredients.push(ingredient)
                })
        },
        deleteIngredient(ingredient) {
            const url = `http://localhost:5000/instance/${this.instance.id}/ingredients`
            axios.delete(url, { data: ingredient })
                .then(response => {
                    this.ingredients = response.data
                })
        },
        get_unique_ingredients(){
            const url = `http://127.0.0.1:5000/ingredients`
            axios.get(url)
                .then(response =>{
                    this.unique_ingredients = response.data
                })
            return this.unique_ingredients
        },
        set_searching(item){
            this.ingredientName = item
            this.searching_allowed = false
        },
        activate_searching(){
            this.unique_ingredients = this.get_unique_ingredients()
            this.searching_allowed = true
        },

    },
    mounted() {
        getInstance(this.$route.params.id)
            .then((data) => {
                this.instance = data
                this.ingredients = this.instance.ingredients
            })
    },
    computed: {
        filteredList() {
            if (this.ingredientName !== '')
                return this.unique_ingredients.filter(item => item.toLowerCase().includes(this.ingredientName.toLowerCase()))
        },
  },
}

</script>

<style>
.btn-create {
    margin: 10px;
}

.btn-new {
    margin: 10px;
}

form {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}

.search-input {
  padding: 10px;
  font-size: 16px;
  margin-bottom: 10px;
}

.result-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.result-list li {
  padding: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.result-list li:hover {
  background-color: #f0f0f0;
}

</style>

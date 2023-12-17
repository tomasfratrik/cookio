<template>
    <div class="InstanceDetailView"> 
        <div v-if="toggleModal">
            <Modal @close="toggleModal_">
                <form @submit.prevent="addIngredient">
                    <label>Ingredient name</label>
                    <input type="text" v-model="ingredientName" required>
                    <label>Select Unit</label>
                    <select v-model="unit">
                        <option>Gram</option>
                        <option>Miligram</option>
                        <option>Liter</option>
                        <option>Mililiter</option>
                    </select>
                    <label>Quantity</label>
                    <input type="number" v-model="quantity" required>
                    <button class="btn-create">Add</button>
                </form>
            </Modal>
        </div>
        <div v-if="toggleModalUp">
            <Modal @close="toggleModal_">
                <form @submit.prevent="addIngredient">
                    <label>Ingredient name</label>
                    <input type="text" v-model="ingredientName" required>
                    <label>Select Unit</label>
                    <select v-model="unit">
                        <option>Gram</option>
                        <option>Miligram</option>
                        <option>Liter</option>
                        <option>Mililiter</option>
                    </select>
                    <label>Quantity</label>
                    <input type="number" v-model="quantity" required>
                    <button class="btn-create">Add</button>
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
            <button @click="toggleModal_">Add Ingrediets</button>
            <div v-if="ingredients.length === 0">
                <p>No ingredients</p>
            </div>
            <div v-els>
                <ul>
                    <li v-for="ingredient in ingredients" :key="ingredient.name">
                        <div  class="ingredient-info">
                            <span class="ingredient-name">{{ ingredient.name }}</span>
                            <span class="ingredient-quantity">{{ ingredient.quantity }}-</span> 
                            <span class="ingredient-unit">{{ ingredient.unit }}</span>
                            <div>
                                <button class="btn-delete" @click="deleteIngredient(ingredient)">Delete</button>
                                <button class="btn-delete" @click="toggleModal_Update()">Update</button>
                            </div>
                        </div> 
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
import axios from 'axios'
export default {
    components: {
        Modal,
    },
    data() {
        return {
            recipes: [],
            instance: {},
            pinned_instances: [],
            ingredients: [],
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
        },toggleModal_Update() {
            this.toggleModalUp = !this.toggleModalUp
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
        updateIngredient(ingredient) {
            const url = `http://localhost:5000/instance/${this.instance.id}/ingredients`
            axios.updateInstance(url, { data: ingredient })
                .then(response => {
                    this.ingredients = response.data
                })
        },
    },
    mounted() {
        getInstance(this.$route.params.id)
            .then((data) => {
                this.instance = data
                this.ingredients = this.instance.ingredients
            })
    },
}

</script>

<style scoped>
.btn-delete {
    background-color: white;
    text-decoration: none;
    color: var(--primary-color);
    cursor: pointer;
    font-size: 15px;
    border-radius: 5px;
    border: 1px solid var(--primary-color);
    transition: all 0.2s ease-in-out;
    width: 75px;
    height: 33px;
    font-weight: bold;
    font-family: sans-serif;
    text-align: center;
    margin-top: -12px;
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

.ingredient-info{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-bottom: 2px solid #ccc;
    margin-bottom: 20px;
}

.ingredient-name, .ingredient-quantity, .ingredient-unit{
    font-size: 20px;
    font-weight: bold;
    font-family: sans-serif;
    color: black;

}

.ingredient-quantity, .ingredient-unit{ 
    color: var(--primary-color);
    text-align: right;
}

.ingredient-unit{
    text-align: left;
}

li{
    list-style: none;
}



</style>

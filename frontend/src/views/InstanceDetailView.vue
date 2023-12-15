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
        <router-link class="btn-create" :to="{ name: 'home' }">
            Save
        </router-link>
        <h1>{{ instance.name }}</h1>
        <p>{{ instance.desc }}</p>
        <h2>Ingredients: </h2>
        <button @click="toggleModal_">Add Ingrediets</button>
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
</template>

<script>
import getInstance from '@/composables/getInstance'
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
            ingredients: [],
            toggleModal: false,
            ingredientName: '',
            unit: '',
            quantity: '',
        }
    },
    methods: {
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
        }
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

<style>

</style>

<!-- ITU project 
  -- AUTHOR: xsynek04
-->
<template>
    <div class="InstanceDetailView">       
        <Alert ref="alertDetail" theme="success"></Alert>
        <Alert ref="alertBox"></Alert>
        <div v-if="toggleModal">
            <Modal @close="toggleModal_">
                <Alert ref="alertModal" theme="success"></Alert>
                <form @submit.prevent="addIngredient">
                    <label style="margin-right: 10px;">Select ingredient</label>           
                    <input v-model="ingredientName" placeholder="Search ..." @click="activate_searching" class="search-input"/>
                    <ul v-if="searching_allowed" class="result-list">
                        <li v-for="item in filteredList" :key="item" @click="set_searching(item)" class="result-list li">
                            {{ item }}
                        </li>
                    </ul>
                        
                    <div class="select_unit" >
                    <label>Select unit</label>
                    <select v-model="unit" required>
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
                    </div>
                    <label>Select quantity</label>
                    <input type="range" v-model="quantity" :min="range_low" :max="range_high" step="1">
                    <div class="slider_info" >
                        <span>
                            <input class="range" type="number" v-model="range_low" required >
                        </span>
                        <span>
                            <input class="num_show" type="number" v-model="quantity" required placeholder="Value">
                        </span>
                        <span>
                            <input class="range" type="number" v-model="range_high" required >
                        </span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; width: 70%;">
                        <button class="btn-create">Add</button>
                        <button @click="toggleModal_" class="btn-create">Close</button>
                    </div>
                </form>
            </Modal>
            
        </div>

        <div v-if="toggleModal_Up">
            <Modal @close="toggleModal_Update">
                <Alert ref="alertModal" theme="success"></Alert>
                <form @submit.prevent="updateIngredient">
                    <label style="margin-right: 10px;">Select ingredient</label>           
                    <input v-model="ingredientName" placeholder="Search ..." @click="activate_searching" class="search-input"/>
                    <ul v-if="searching_allowed" class="result-list">
                        <li v-for="item in filteredList" :key="item" @click="set_searching(item)" class="result-list li">
                            {{ item }}
                        </li>
                    </ul>
                        
                    <div class="select_unit" >
                    <label>Select unit</label>
                    <select v-model="unit" required>
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
                    </div>
                    <label>Select quantity</label>
                    <input type="range" v-model="quantity" :min="range_low" :max="range_high" step="1">
                    <div class="slider_info" >
                        <span>
                            <input class="range" type="number" v-model="range_low" required >
                        </span>
                        <span>
                            <input class="num_show" type="number" v-model="quantity" required placeholder="Value">
                        </span>
                        <span>
                            <input class="range" type="number" v-model="range_high" required >
                        </span>
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between; width: 70%;">
                        <button class="btn-create">Save</button>
                        <button @click="toggleModal_Update" class="btn-create">Close</button>
                    </div>
                </form>
            </Modal>
            
        </div>

        <div class="headr">
            <div v-if="showGroupModal">
                <SmallModal ref="modal" @close="handleGroupModalToggle">
                    <h2>Groups</h2>
                    <div class="groups box">
                        <div v-for="group in groups" :key="group.id">
                            <div class="group">
                                <p>{{ group.name }}</p>
                                <button @click="addInstaceToGroup(group)" class="btn-add-group">Add</button>
                            </div>
                        </div>
                    </div>
                    <div class="buttons">
                        <button @click="handleGroupModalToggle" class="btn-close">Close</button>
                    </div>
                </SmallModal>
            </div>
            <div class="edit">
                <h1>Meal detail</h1>

                <div class="settings">
                    <label>Edit </label>
                    <label v-if="showEdit" class="switch">
                        <input type="checkbox" v-model="edit">
                        <span class="round slider"></span>
                    </label>
                    <button class="add-to-group" @click="showGroupModal = true">Add to group</button>
                </div>
            </div>
            <div v-if="edit">
                <form @submit.prevent="handleSubmit">
                    <div class="left">
                        <label>Meal name</label>
                        <input class="instance-name" type="text" v-model="instance.name"><br>
                        <label>Meal description</label>
                        <textarea class="instance-desc" v-model="instance.desc"></textarea>
                    </div>
                    <div class="right">
                        <label>Rating</label>
                        <p>Set to -1, if not rated</p>
                        <input type="number" v-model="instance.rating" min="-1" max="10"><br>
                        <label class="pinned">Pinned</label>
                        <input type="checkbox" v-model="instance.pinned">
                        <button class="btn-create">Save</button>
                    </div>
                </form>
            </div>
            <div v-else class="form2">
                <div class="left">
                    <label>Meal name</label>
                    <h1 class="instance-name">{{ instance.name }}</h1>
                    <label>Meal description</label>
                    <textarea class="instance-desc no-border" v-model="instance.desc" disabled></textarea>
                </div>
                <div class="right">
                    <label>Rating</label>
                    <p v-if="instance.rating >= 0"> Rating: {{ instance.rating }}</p>
                    <p v-else> Rating: not rated yet!</p>
                    <label class="pinned">Pinned</label>
                    <input disabled="true" type="checkbox" v-model="instance.pinned">
                </div>
            </div>
        </div>

            <div class="ingredients">
                <button @click="toggleModal_" class="btn-add">Add Ingredients</button>
                <div v-if="ingredients.length === 0">
                    <p>No ingredients</p>
                </div>
                <ul class="box">
                    <li v-for="ingredient in ingredients" :key="ingredient.name">
                        <div  class="ingredient-info">
                            <span class="ingredient-name">{{ ingredient.name }}</span>
                            <span class="ingredient-quantity">{{ ingredient.quantity }}-</span> 
                            <span class="ingredient-unit">{{ ingredient.unit }}</span>
                            <div>
                                <button class="btn-delete" @click="deleteIngredient(ingredient)">Delete</button>
                                <button class="btn-update" @click="open_modal_update(ingredient)">Update</button>
                            </div>
                        </div> 
                    </li>
                </ul>
            </div>

    </div>
</template>

<script>
import getInstance from '@/composables/getInstance'
import updateInstance from '@/composables/updateInstance'
import Modal from '@/components/Modal.vue'
import axios, { all } from 'axios'
import Alert from '@/components/Alert.vue'
import SmallModal from '@/components/SmallModal.vue'
import getGroups from '@/composables/getGroups'
import addMealsToGroup from '@/composables/addMealsToGroup'

export default {
    components: {
        Modal, Alert, SmallModal
    },
    data() {
        return {
            recipes: [],
            instance: {},
            pinned_instances: [],
            ingredients: [],
            ingredient: {},
            unique_ingredients: [],
            searching_allowed: false,
            toggleModal: false,
            toggleModal_Up: false,
            ingredientName: '',
            unit: '',
            quantity: '',
            edit:  false,
            range_low: 0,
            range_high: 1000,
            showEdit: true,
            showGroupModal: false,
            groups: [],
        }
    },
    methods: {

        alert(type, msg) {
            this.$refs.alertBox.showAlert(type, msg);
        },

        addInstaceToGroup(group) {
            // make ist of instance ids, in this instance only 1 id in list
            const instance_ids = [this.instance.id]
            addMealsToGroup(group.name, instance_ids)
                .then(() => {
                    this.$emit('updateGroups')
                    this.alert('success', "Meal successfully added to group.");
                })
        },

        handleGroupModalToggle() {
            // update groups
            getGroups()
                .then((data) => {
                    this.groups = data
                    this.showGroupModal = !this.showGroupModal
                })
        },

        // handle submit button, update instance
        handleSubmit() {
            updateInstance(this.instance)
                .then(() => {
                    console.log('updated instance')
                    this.edit = false
                })
        },
        // toggle modal, to add ingredients
        toggleModal_() {
            this.toggleModal = !this.toggleModal
            this.showEdit = !this.showEdit
        },
        // toggle modal for update ingredients
        toggleModal_Update() {
            this.toggleModal_Up = !this.toggleModal_Up
            this.showEdit = !this.showEdit
        },
        // open update modal
        open_modal_update(ingredient) { 
            this.ingredientName = ingredient.name
            this.quantity = ingredient.quantity
            this.unit = ingredient.unit

            this.toggleModal_Up = !this.toggleModal_Up
            this.showEdit = !this.showEdit
        },
        // add ingredient to instance
        addIngredient() {
            
            for (var i = 0; i < this.ingredients.length; i++){
                if (this.ingredients[i].name === this.ingredientName){
                    this.alert_modal('error', "Ingredient of that name already in the recipe.");
                    return false;
                }
            }
            
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
            this.alert_modal('success', "Ingredient successfully added.");
            return true;
        },
        // delete ingredient from instance
        deleteIngredient(ingredient) {
            const url = `http://localhost:5000/instance/${this.instance.id}/ingredients`
            try{
                axios.delete(url, { data: ingredient })
                    .then(response => {
                        this.ingredients = response.data
                    })
                this.alert_detail('success', "Ingredient successfully deleted.");
            }
            catch{
                this.alert_detail('error', "Ooops, somethinw went wrong.");
            }
        },
        // get unique all unique ingredients
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

        // update ingredient
        updateIngredient() {
            
            const ingredient = {
                name: this.ingredientName,
                unit: this.unit,
                quantity: this.quantity
            }

            const url = `http://localhost:5000/instance/${this.instance.id}/ingredients`
            axios.put(url, ingredient )
                .then(response => {
                    this.ingredients = response.data
                })
        },
        // alert function
        alert_modal(type, msg) {
            this.$refs.alertModal.showAlert(type, msg);
        },
        alert_detail(type, msg) {
            this.$refs.alertDetail.showAlert(type, msg);
        },
    },
    mounted() {
        // fetch instance by id
        getInstance(this.$route.params.id)
            .then((data) => {
                this.instance = data
                this.ingredients = this.instance.ingredients
                // log name of instance
                console.log(this.instance.name)
            })
        // fetch groups
        getGroups()
            .then((data) => {
                this.groups = data
            })
    },
    computed: {
        // filter ingredients
        filteredList() {
            if (this.ingredientName !== '')
                return this.unique_ingredients.filter(item => item.toLowerCase().includes(this.ingredientName.toLowerCase()))
        },
    },
    watch: {
        $route(to, from) {
        // Check if the route parameter has changed
            if (to.params.id !== from.params.id) {
                // Update the instanceId and fetch data
                // this.instanceId = to.params.id;
                getInstance(this.$route.params.id)
                    .then((data) => {
                        this.instance = data
                        this.ingredients = this.instance.ingredients
                        // log name of instance
                        console.log(this.instance.name)
                    });
            }
        },
    },
    beforeRouteUpdate(to, from, next) {
        getInstance(this.$route.params.id)
            .then((data) => {
                this.instance = data
                this.ingredients = this.instance.ingredients
                // log name of instance
                console.log(this.instance.name)
            });
        // Call fetchData directly if the route is updated without leaving the component
        next();
    },
}

</script>

<style scoped>

.modal h2 {
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    font-family: sans-serif;
    color: var(--primary-color);
    margin-bottom: 5px;
    margin-top: 5px;
}
.btn-add-group {
    width: 60px;
    height: 40px;
    background-color: var(--primary-color);
    color: white;
    border-radius: 5px;
    transition: all 0.2s ease-in-out;
}

.btn-add-group:hover {
    background-color: var(--secondary-color);
    color: white;
}

.btn-close {
    margin: 10px auto;
    display: block;
    width: 100px;
    height: 40px;
    color: white;
    border-radius: 5px;
    background-color: rgb(218, 69, 69);
    transition: all 0.2s ease-in-out;
}

.btn-close:hover {
    background-color: rgb(218, 69, 69);
    color: white;
}

.group {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 10px;
    padding: 10px;
    border: 1px solid var(--primary-color);
    border-radius: 5px;
}

.add-to-group {
    margin: 10px;
    width: 100px;
    height: 40px;
    background-color: var(--primary-color);
    color: white;
    border-radius: 10px;
    transition: all 0.2s ease-in-out;
}

.add-to-group:hover {
    background-color: var(--secondary-color);
    color: white;
}

.headr{
    max-width: 500px;
    margin: 0 auto;
}
.btn-update, .btn-delete {
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

.btn-delete{
    background-color: rgb(218, 69, 69);
    color: white;
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

.form2 {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}

.headr {
    text-align: left;
}
.edit {
    text-align: center;
}
.edit h1 {
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    font-family: sans-serif;
    color: var(--primary-color);
    margin-bottom: 5px;
    margin-top: 5px;
}

.headr label {
    font-size: 20px;
    color: var(--primary-color);
    font-weight: bold;
    font-family: sans-serif;
    /* margin-bottom: 6px; */
}
.instance-name {
    font-size: 18px;
    font-weight: bold;
    font-family: sans-serif;
    color: black;
    text-align: left;
    margin-bottom: 10px;
}

.instance-desc {
    font-size: 15px;
    font-weight: bold;
    font-family: sans-serif;
    color: black;
    text-align: left;
    margin-bottom: 10px;
    height: 70px;
    width: 200px;
    color: grey;
    display: block;
}

.no-border {
    border: none;
}

.btn-create {
    width: 100px;
    height: 50px;
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

.btn-add {
    margin: 10px;
    width: 130px;
    height: 40px;
    background-color: var(--secondary-color);
    color: white;
    border-radius: 5px;
}

.range {
  align-items: center;
  height: 50px;
  width: 50px;
  text-align: center;
}

.num_show {
  height: 50px;
  width: 75px;
  margin: 25px;
  text-align: center;
}

.slider_info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px;
  appearance: textfield;
}

/* input[type=number] {
  -moz-appearance: textfield;
} */

.select_unit {
    display: flex;
    margin: 10px;
    flex-direction: column;
    align-items: center;
}

.headr .btn-create {
    margin-top: 10px;
}

.box {
    max-width: 100%;
    width: 1000px;
    height: 300px;
    margin: 0 auto;
}

.form2, .headr form {
    display:flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
}

.pinned {
    margin-right: 10px;
}

</style>

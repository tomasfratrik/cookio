<template>
    <div>
        <h1>Recipe class detail</h1>
        <label>Edit </label>
        <label class="switch">
            <input type="checkbox" v-model="edit">
            <span class="round slider"></span>
        </label>

        <div v-if="edit">
            <form @submit.prevent="handleSubmit">
                <label for="class_name">Class Name</label>
                <input type="text" id="class_name" v-model="recipe.class_name">
                <label for="class_desc">Class Description</label>
                <input type="text" id="class_desc" v-model="recipe.class_desc">
                <button type="submit">Save</button>
            </form>
        </div>
        <div v-else>
            <h2>{{ recipe.class_name }}</h2>
            <p>{{ recipe.class_desc }}</p>
        </div>
        <button @click="classInstances(recipe)">Instances</button>
        <button @click="_deleteClass(recipe)">Delete</button>
    </div>
</template>

<script>
import deleteRecipeClass from '@/composables/deleteRecipeClass'
import getRecipeClass from '@/composables/getRecipeClass'
import updateRecipeClass from '@/composables/updateRecipeClass'
export default {
    data() {
        return {
            recipe: {},
            instances: [],
            edit: false
        }
    },
    methods: {
        classInstances(recipe) {
            this.$router.push({ name: 'ClassInstances', params: { id: recipe.id } })
        },

        _deleteClass(recipe) {
            deleteRecipeClass(recipe.id)
                .then(() => {
                    console.log('deleted class')
                    this.$router.push({ name: 'home' })
                })
        },
        handleSubmit() {
            updateRecipeClass(this.recipe)
                .then(() => {
                    console.log('updated class')
                    this.edit = false
                })
        }

    },
    mounted() {
        // this.recipe = this.$store.state.recipe
        getRecipeClass(this.$route.params.id)
            .then((recipe) => {
                this.recipe = recipe
                this.instances = recipe.instances
            })
    }
}
</script>

<style>
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 25px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 25px;
  width: 25px;
  left: 0px;
  bottom: 0px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  /*background-color: #2196F3; */
  background-color: var(--secondary-color);
}

input:focus + .slider {
  box-shadow: 0 0 1px var(--secondary-color);
}

input:checked + .slider:before {
  -webkit-transform: translateX(16px);
  -ms-transform: translateX(16px);
  transform: translateX(16px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
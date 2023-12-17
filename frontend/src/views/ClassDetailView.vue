<template>
    <div class="ClassDetail">
        <Alert ref="alertBox"></Alert>
        <div class="head">
        <h1>Recipe class detail</h1>
        <div class="edit">
          <p>Edit</p>
          <label class="switch">
              <input type="checkbox" v-model="edit">
              <span class="round slider"></span>
          </label>
        </div>
        </div>

        <div v-if="edit">
            <form @submit.prevent="handleSubmit">
                <label for="class_name">Class name</label>
                <input class="name" type="text" id="class_name" v-model="recipe.class_name">
                <label for="class_desc">Class description</label>
                <!-- <input type="text" id="class_desc" v-model="recipe.class_desc"> -->
                <textarea id="class_desc" class="desc" v-model="recipe.class_desc"></textarea>
                <button class="btn-create" type="submit">Save</button>
            </form>
        </div>
        <div class="noedit" v-else>
            <label>Class name</label>
            <h3 class="name">{{ recipe.class_name }}</h3>
            <label>Class description</label>
            <textarea class="desc" v-model="recipe.class_desc" disabled></textarea>
        </div>
        <button  class="btn-go" @click="classInstances(recipe)">Instances</button>
        <button class="btn-delete" @click="_deleteClass(recipe)">Delete</button>
    </div>
</template>

<script>
import deleteRecipeClass from '@/composables/deleteRecipeClass'
import getRecipeClass from '@/composables/getRecipeClass'
import updateRecipeClass from '@/composables/updateRecipeClass'
import Alert from '@/components/Alert.vue'
export default {
  components: { Alert },
    data() {
        return {
            recipe: {},
            instances: [],
            edit: false
        }
    },
    methods: {
        alert(type, message) {
            this.$refs.alertBox.showAlert(type, message)
        },
        classInstances(recipe) {
            this.$router.push({ name: 'ClassInstances', params: { id: recipe.id } })
        },

        _deleteClass(recipe) {
            deleteRecipeClass(recipe.id)
                .then(() => {
                    console.log('deleted class')
                    this.$router.push({ name: 'home' })
                    this.alert('success', 'Class deleted!')
                })
        },
        handleSubmit() {
            updateRecipeClass(this.recipe)
                .then(() => {
                    console.log('updated class')
                    this.alert('success', 'Class updated!')
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

.ClassDetail {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;

}

.head {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.head .edit {
  margin-bottom: 15px;
}

.ClassDetail label {
  font-size: 25px;
  color: var(--primary-color);
  font-weight: bold;
  font-family: sans-serif;
}

.ClassDetail h3 {
  font-size: 20px;
  font-weight: bold;
  font-family: sans-serif;
  border: 1px solid black;
}
.ClassDetail .desc {
  font-size: 15px;
  font-weight: bold;
  font-family: sans-serif;
  border: 1px solid black;
  padding: 5px;
}

.ClassDetail .btn-delete, .btn-go {
  background-color: var(--secondary-color);
  color:white;
  border: none;
  border-radius: 5px;
  height: 50px;
  width: 100px;
  cursor: pointer;
}
.btn-got {
  background-color: var(--secondary-color);
}

.btn-go:hover {
  background-color: var(--primary-color);
}

.ClassDetail .btn-delete {
  background-color: rgb(224, 95, 95);

}

.ClassDetail .btn-delete:hover {
  background-color: rgb(255, 0, 0);
}

.ClassDetail form {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.ClassDetail textarea{

  display: block;
  height: 100px;
  width: 300px;
}


.ClassDetail .name {
  color: black;
  font-size: 20px;
}

.ClassDetail .desc {
  color: grey;
  font-size: 15px;
}

.ClassDetail .noedit {
  min-width: 300px;
}

.ClassDetail .noedit .name, .ClassDetail .noedit .desc {
  border: none;
}

</style>
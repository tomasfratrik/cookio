<template>
  <div class="homeview">
    <Alert ref="alertBox" theme="success"></Alert>
    <div class="header">
      <router-link :to="{ name: 'AssignRecipeClass' }" custom v-slot="{ navigate }">
      <button @click="navigate" >Add Instance</button>
      </router-link>
      <!-- search query -->
    </div>

    <div class="row">
      <div class="left">
        <div class="box">
          <div class="recipe" v-for="recipe in recipes" :key="recipe.id">
              <h2>{{ recipe.class_name }}</h2>
              <p>{{ recipe.class_desc }}</p>
              <button @click="classInstances(recipe)">Instances</button>
              <button>Detail</button>
              <button @click="_deleteClass(recipe)">Delete</button>
          </div>
        </div>
      </div>

      <div class="right">
        <!-- pinned instances -->
      </div>
    </div>

  </div> 
</template>

<script>
import axios from 'axios'
import getRecipes from '@/composables/getRecipes'
import deleteRecipeClass from '@/composables/deleteRecipeClass'
import Alert from '@/components/Alert.vue'
export default {
  components: {
    Alert
  },
  data() {
    return {
      recipes: []
    }
  },
  methods: {
    classInstances(recipe) {
      this.$router.push({ name: 'ClassInstances', params: { id: recipe.id } })
    },

    alert(type, msg) {
      this.$refs.alertBox.showAlert(type, msg);
    },

    _deleteClass(recipe) {
      deleteRecipeClass(recipe.id)
        .then(() => {
          console.log('deleted class')
          getRecipes()
            .then((data) => {
              this.recipes = data
            })
          this.alert('success',"Class deleted successfully")
          // this.alert('error',"Class deleted successfully")
          // this.alert('warn',"Class deleted successfully")
        })
    },

  },
  mounted() {
    getRecipes()
      .then((data) => {
          this.recipes = data
      })
  }
}
</script>

<style>

.row {
  display: flex;
  flex-direction: row;
}


.recipe {
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
  background-color: var(--neutral-color);
  max-width: 300px;
  margin-left: 0;
}

h2 {
  color: var(--primary-color);
}

p {
  color: #777;
}

h1 {
  color: var(--primary-color);
  margin-bottom: 20px;
}

/*
button {
  text-decoration: none;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 20px;
  cursor: pointer;
}
*/

</style>

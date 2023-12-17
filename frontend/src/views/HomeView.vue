<!-- ITU project 
  -- AUTHOR: xfratr01
-->
<template>
  <div class="home">
    <Alert ref="alertBox" theme="success"></Alert>
    <div class="header">
      <router-link :to="{ name: 'AssignRecipeClass' }" custom v-slot="{ navigate }">
      <button @click="navigate" class="btn-create">Add meal</button>
      </router-link>
        <input type="text" v-model="search" placeholder="Search">
    </div>

    <div class="row">

      <div class="left">
        <h2>Recipes </h2>
        <div class="box">
          <div class="recipe" v-for="recipe in filteredRecipes" :key="recipe.id">
              <h2>{{ recipe.class_name }}</h2>
              <button @click="classInstances(recipe)">Meals</button>
              <button @click="classDetail(recipe)">Detail</button>
              <button class="btn-delete" @click="_deleteClass(recipe)">Delete</button>
          </div>
        </div>
      </div>

      <div class="right">
        <h2>Pinned meals</h2>
        <div class="box">
          <div class="instance" @click="instanceDetail(instance)" v-for="instance in filteredInstances" :key="instance.id">
              <h3 v-if="instance.name.length < 15">{{ instance.name }}</h3>
              <h3 v-else>{{ instance.name.substring(0, 15) }}...</h3>
              <p v-if="instance.rating > 0">Rating: {{ instance.rating }}</p>
              <p v-else>Rating: not rated yet!</p>
            </div>
        </div>
      </div>

    </div>

  </div> 
</template>

<script>
import getRecipes from '@/composables/getRecipes'
import deleteRecipeClass from '@/composables/deleteRecipeClass'
import getPinnedInstances from '@/composables/getPinnedInstances'
import Alert from '@/components/Alert.vue'
export default {
  components: {
    Alert
  },
  data() {
    return {
      recipes: [],
      pinned_instances: [],
      search: '',
      orderBy: 'name',
    }
  },
  methods: {
    // go to instances of class
    classInstances(recipe) {
      this.$router.push({ name: 'ClassInstances', params: { id: recipe.id } })
    },
    // go to detail of class
    classDetail(recipe) {
      this.$router.push({ name: 'ClassDetail', params: { id: recipe.id } })
    },
    // go to detail of instance
    instanceDetail(instance) {
      this.$router.push({ name: 'InstanceDetail', params: { id: instance.id } })
    },
    // alert function
    alert(type, msg) {
      this.$refs.alertBox.showAlert(type, msg);
    },

    // delete this class
    _deleteClass(recipe) {
      deleteRecipeClass(recipe.id)
        .then(() => {
          console.log('deleted class')
          getRecipes()
            .then((data) => {
              this.recipes = data
            })
          this.alert('success',"Class deleted successfully")
        })
    },

  },
  computed: {
    // filter instaces
    filteredInstances() {
      return this.pinned_instances.filter(item => item.name.includes(this.search));
    },
    // filter recipes
    filteredRecipes() {
      return this.recipes.filter(item => item.class_name.includes(this.search));
    }

  },
  mounted() {
    // fetch recipes and pinned instances
    getRecipes()
      .then((data) => {
          this.recipes = data
      })
    getPinnedInstances()
      .then((data) => {
          this.pinned_instances = data
      })
  }
}
</script>

<style>

.row {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}


.recipe {
  border: 1px solid black;
  border-radius: 5px;
  padding: 5px;
  margin: 10px;
  background-color: var(--primary-color);
  margin-left: 0;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  min-height: 50px;
}
.recipe h2 {
  max-width: 270px;
  flex: 1;
  word-wrap: break-word;
  white-space: normal;
}

.recipe button {
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid black;
  background-color: white;
  color: black;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  height: 30px;
}

.recipe button:hover {
  background-color: var(--secondary-color);
  color: white;
}

.recipe button.btn-delete {
  background-color: rgb(225, 105, 105);
  color: white;
}
.recipe button.btn-delete:hover {
  background-color: rgb(255, 0, 0);
}

h2 {
  color: var(--primary-color);
}
.recipe h2 {
  color:white;
}

p {
  color: #777;
}

h1 {
  color: var(--primary-color);
  margin-bottom: 20px;
}

.home .box {
  width: 400px;
  height: 300px;
  padding-left:30px;
}

.home .right .box {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 10px;

}

.home .instance {
  border: 2px solid var(--primary-color);
  border-radius: 5px;
  background-color: var(--neutral-color);
  width: 45%;
  height: 130px;
  color: black;
  position: relative;

}
.home .instance h3 {
  text-align: center;
  font-size: 20px;
}
.home .instance:hover ::after {
  content:"";
  position:absolute;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color: var(--secondary-color);
  text-align: center;
  color: white;
  font-size: 30px;
  font-weight: bold;
  border-radius: 5px;
  line-height: 110px;
  animation: slideInFromLeft 0.5s ease-in-out;
  animation-fill-mode: forwards;
  cursor: pointer;
}


@keyframes slideInFromLeft {
  0% {
    width: 0;
  }
  100% {
    width: 100%;
    content:"Detail";
  }
}
.header input {

  width: 300px;
  display: block;
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
  height: 40px;
  border-radius: 20px;
}

.header button {
  width: 300px;
  display: block;
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
}

.home .left .box {
  width: 500px;
}
/* .instance:hover::after {

} */

</style>

<template>
  <div class="homeview">
    <router-link to="/createrecipe" custom v-slot="{ navigate }">
      <button @click="navigate" >Add Instance</button>
    </router-link>
  </div> 
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      recipes: []
    }
  },
}
</script>

<style>
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

</style>
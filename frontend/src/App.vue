<template>
  <div>
    <nav>
      <div class="nav-content">
        <button class="btn-arrow arrow-left" @click="goBack">
          <font-awesome-icon :icon="['fas', 'arrow-left']"/>
        </button>
        <button class="btn-arrow arrow-right" @click="goForward">
          <font-awesome-icon :icon="['fas', 'arrow-right']"/>
        </button>
        <router-link class="home-icon" :to="{ name: 'home' }">
          <font-awesome-icon :icon="['fas', 'house']" />
        </router-link>
        <router-link class="link" :to="{ name: 'home' }">
         <h1 class="name">Cookio</h1>
        </router-link>
      </div>
    </nav>
    <div class="content-container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(fas);

export default {
  components: {
    FontAwesomeIcon,
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    goForward() {
      this.$router.go(1);
    },
  },
}
</script>

<style scoped>
body {
  background-color: var(--bg-color);
}

.content-container{
  max-width: var(--size-md);
  margin: 20px auto;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 20px;
  border-radius: 15px;
  height: 100vh;
}

nav {
  max-width: var(--size-xl);
  margin: auto;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 3px;
  height: 50px;
  border-bottom: 1px solid var(--primary-color);
}


.nav-content{
  display: flex;
  justify-content: center;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  gap: 20px;
}

.link{
  text-decoration: none;
  color: black;
  position: absolute;
  top: 5px;
}

.nav-content .home-icon{
  color: var(--primary-color);
  position: absolute;
  left: calc(50% + 100px );
  top: 5px;
  font-size: 30px;
}

h1 {
  color: var(--primary-color);
  margin-bottom: 20px;
}

.btn-arrow {
  background-color: var(--primary-color);
  border: none;
  border-radius: 100px;
  height: 30px;
  width: 30px;
  cursor: pointer;
}
.arrow-right {
  color:white;
  font-size: 30px;
  position: absolute;
  left: calc(50% - 120px );
  top: 10px;
  font-size: 20px;
}



.arrow-left {
  color:white;
  font-size: 30px;
  position: absolute;
  left: calc(50% - 170px );
  top: 10px;
  font-size: 20px;
}

</style>


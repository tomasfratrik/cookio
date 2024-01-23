<!-- ITU project 
  -- AUTHOR: xfratr01
-->
<template>
  <div>
    <Alert ref="alertBox"></Alert>
    <nav>
      <div class="nav-content">
        <button class="btn-groups"  @click="groups_toggle = !groups_toggle">
          Groups
          <font-awesome-icon class="dropdown" :class="{ rotate: groups_toggle, rotateback: !groups_toggle  }" :icon="['fas', 'fa-caret-up']"/>
        </button>
        <div v-if="groups_toggle" class="groups">
          <div class="group add-group" >
            <div class="add-group-add" v-if="add_group_toggle">
              <p>adding group</p>
              <font-awesome-icon class="x" :icon="['fas', 'fa-x']" @click="add_group_toggle = false" />
              <font-awesome-icon class="check" :icon="['fas', 'fa-check']" @click="handleAddGroup" />
              <input type="text" v-model="new_group_name" placeholder="Group name">
            </div>
            <div class="add-group-default" v-else @click="add_group_toggle = true">
              <font-awesome-icon class="plus" :icon="['fas', 'fa-plus']"/>
              <p>Add group</p>
            </div>
          </div>
          <div class="group" v-for="group in groups" :key="group.name">
            <p>{{ group.name }}</p>
            <!-- <router-link :to="{ name: 'GroupDetail', params: { id: group.id } }">
              <p>{{ group.name }}</p>
            </router-link> -->
          </div>
        </div>
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
import getGroups from '@/composables/getGroups';
import addGroup from '@/composables/addGroup';
import Alert from '@/components/Alert.vue'

library.add(fas);

export default {
  components: {
    FontAwesomeIcon,
    Alert,
  },
  data() {
    return {
      groups_toggle: false,
      add_group_toggle: false,
      groups: [],
      new_group_name: '',
    }
  },
  methods: {
    alert(type, message) {
        this.$refs.alertBox.showAlert(type, message)
    },

    handleAddGroup(){
      this.add_group_toggle = false
      if(this.new_group_name == ''){
        this.alert('error', 'Group name cannot be empty!')
        return
      }
      if(this.groups.some(group => group.name.toUpperCase() == this.new_group_name.toUpperCase())){
        this.alert('error', 'Group with this name already exists!')
        return
      }
      addGroup(this.new_group_name)
        .then((response) => {
          getGroups()
            .then((data) => {
              this.groups = data
            })
          this.alert('success', 'Group added!')
      })
    },
    // go back and forward in history
    goBack() {
      this.$router.go(-1);
    },
    goForward() {
      this.$router.go(1);
    },
  },
  mounted() {
    // fetch groups
    getGroups()
      .then((data) => {
        this.groups = data
      })
  },
}
</script>

<style scoped>

.add-group {
  background-color: var(--primary-color);
  color: white;
  border-radius: 10px;
  padding: 5px;
  width: 100%;
  text-align: center;
  cursor: pointer;
  border-radius: 2px;
}

.add-group p {
  color: white;
}
.groups {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  position: absolute;
  top: 50px;
  left: calc(50% - 350px );
  width: 200px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

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

.btn-groups {
  color: var(--primary-color);
  width: 100px;
  position: absolute;
  top: 5px;
  padding: 8px;
  border-radius: 10px;
  background-color: var(--primary-color);
  border: none;
  color: white;
  left: calc(50% - 300px );
  font-size: 17px; 
  cursor: pointer;
}

.rotateback {
  transform: rotate(0deg);
  /* animation: rotate-back 0.5s ease-in-out forwards; */
}

@keyframes rotate-back {
  0% {
    transform: rotate(180deg);
  }
  100% {
    transform: rotate(0deg);
  }
}

.rotate {
  transform: rotate(180deg);
  /* animation: rotate 0.5s ease-in-out forwards; */
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(180deg);
  }
}

/* .groups-opened {

} */

  /* animation: rotate 0.5s ease-in-out forwards; */
/* .btn-groups:hover .dropdown {
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  -o-transform: rotate(180deg);
  transform: rotate(180deg);
  transition: all .3s ease;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(180deg);
  }
} */


</style>


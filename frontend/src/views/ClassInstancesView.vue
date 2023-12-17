<!-- ITU project 
  -- AUTHOR: xfratr01
-->
<template>
<div class="ClassInstances">
    <Alert ref="alertBox"></Alert>
    <div class="header">
        <h1>Recipe meals</h1>
        <div class="searchBox">
            <input type="text" class="search" v-model="search" placeholder="Search">
            <div>
                <p>Sort By</p>
                <select class="sort" v-model="sortBy">
                    <option value="date">Date</option>
                    <option value="name">Name</option>
                    <option value="rating">Rating</option>
                </select>
            </div>
            <div>
                <p>Reverse</p>
                <label class="switch">
                    <input type="checkbox" v-model="reverseSort">
                    <span class="round slider"></span>
                </label>
            </div>
        </div>
    </div>
    <div class="Instances box">
        <div class="instance" v-for="instance in filteredInstances" :key="instance.id">
            <h2 class="flex-item item1">{{ instance.name }}</h2>
            <p class="timestamp flex-item item2">({{ instance.timestamp }})</p>
            <p v-if="instance.rating > 0" class="rating flex-item item3">Rating: {{ instance.rating }}/10</p>
            <p v-else class="rating flex-item item3">Rating: not rated yet!</p>
            <div class="btns flex-item item4">
                <router-link :to="{ name: 'InstanceDetail', params: { id: instance.id } }">
                    <button class="btn-detail">Detail</button>
                </router-link>

                <button class="btn-delete" @click="_deleteInstance(instance)">Delete</button>
            </div>
        </div>
    </div>

</div>
</template>

<script>
import getInstances from '@/composables/getInstances'
import deleteInstance from '@/composables/deleteInstance'
import Alert from '@/components/Alert.vue'
import axios from 'axios'

export default {
    components: {
        Alert
    },
    data() {
        return {
            classInstances: [],
            search: '',
            sortBy: 'date',
            reverseSort: false,
        }
    },
    methods: {
        // alert function
        alert(type, msg) {
            this.$refs.alertBox.showAlert(type, msg);
        },
        // delete this instance
        _deleteInstance(instance) {
            deleteInstance(instance.id)
                .then(() => {
                    const id = this.$route.params.id
                    this.alert('success', 'Instance deleted!')
                    getInstances(id)
                        .then((data) => {
                            this.classInstances = data
                        })
                })
        }

    },
    mounted() {
        const id = this.$route.params.id
        // fetch instances of class
        getInstances(id)
            .then((data) => {
                this.classInstances = data
            })
    },
    computed: {
        // sort and filter instances
        filteredInstances() {
            const sorted = [...this.classInstances]; // Create a copy of the original list
            
            if (this.sortBy === 'name') {
                sorted.sort((a, b) => a.name.localeCompare(b.name));
            } else if (this.sortBy === 'rating') {
                sorted.sort((a, b) => b.rating - a.rating);
            } else if (this.sortBy === 'date') {
                sorted.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
            }
            
            if (this.reverseSort) {
                sorted.reverse();
            }

            return sorted.filter(item => item.name.includes(this.search));
        },
    },
}
</script>

<style scoped >
.instance {
    border: 1px solid black;
    padding: 10px;
    width: 100%;
    min-height: 50px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.instance h2 {
    max-width: 400px;
    word-wrap: break-word;
    white-space: normal;
}
.instance .btn-detail, .instance .btn-delete {
    height: 30px;
    width: 50px;
    border-radius: 1px;
    color:white;
    cursor: pointer;
}
.instance .btn-detail {
    background-color: var(--secondary-color);
}
.instance .btn-delete {
    background-color: rgb(218, 69, 69);
}
.search {
    width: 400px;
    height: 50px;
    border-radius: 25px;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}
.header {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
}

.ClassInstances .box {
    width: 100%;
    margin: 0 auto;
    height: 400px;
    overflow: scroll;
    border: 1px solid black;
    border-radius: 5px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
}

.searchBox {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    justify-content: space-evenly;
}

.rating {
    color: var(--secondary-color);
}


.flex-item {
  flex-grow: 0;
  flex-shrink: 0;
}

.item1 {
  flex-basis: 45%;
}

.item2 {
  flex-basis: 20%;
}

.item3 {
  flex-basis: 20%;
}

.item4 {
  flex-basis: 15%;
}

.sort {
    width: 70px;
    height: 30px;
    border-radius: 5px;
    border: 1px solid black;
    padding: 5px;
    margin: 5px;
}

</style>
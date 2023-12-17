<template>
<div class="ClassInstances">
    <h1>Class instances</h1>
    <div class="Instances">
        <div class="instance" v-for="instance in classInstances" :key="instance.id">
            <h2>{{ instance.name }}</h2>
            <p> Rating - {{ instance.rating }}</p>
            <div class="btns">
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
import axios from 'axios'
export default {
    data() {
        return {
            classInstances: []
        }
    },
    methods: {
        _deleteInstance(instance) {
            deleteInstance(instance.id)
                .then(() => {
                    const id = this.$route.params.id
                    getInstances(id)
                        .then((data) => {
                            this.classInstances = data
                        })
                })
        }

    },
    mounted() {
        const id = this.$route.params.id
        getInstances(id)
            .then((data) => {
                this.classInstances = data
                // return this.classInstances
            })
    }
}
</script>

<style scoped >
.instance {
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
    width: 100%;
    height: 50px;
    /* height: 300px; */
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.instance .btn-detail, .instance .btn-delete {
    /* padding: 10px; */
    height: 30px;
    width: 50px;
    border-radius: 1px;
    color:white;
    cursor: pointer;
}
.instance p {
    /* align right */
    /* align-self: flex-end; */
}

.instance .btn-detail {
    background-color: var(--secondary-color);
}
.instance .btn-delete {
    background-color: rgb(218, 69, 69);
}
</style>
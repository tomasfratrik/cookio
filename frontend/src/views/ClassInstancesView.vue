<template>
<div class="ClassInstances">
    <h1>Class instances</h1>
    <div class="Instances">
        <div class="instance" v-for="instance in classInstances" :key="instance.id">
            <h2>{{ instance.name }}</h2>
            <p>{{ instance.desc }}</p>
            <p> rating - {{ instance.rating }}</p>
            <router-link :to="{ name: 'InstanceDetail', params: { id: instance.id } }">
                <button>Detail</button>
            </router-link>

            <button @click="_deleteInstance(instance)">Delete</button>
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

<style >

</style>
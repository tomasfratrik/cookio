<template>
    <div>
        <h1>Recipe class detail</h1>
        <h2>{{ recipe.class_name }}</h2>
        <p>{{ recipe.class_desc }}</p>
        <button @click="classInstances(recipe)">Instances</button>
        <button @click="_deleteClass(recipe)">Delete</button>
    </div>
</template>

<script>
import deleteRecipeClass from '@/composables/deleteRecipeClass'
import getRecipeClass from '@/composables/getRecipeClass'
export default {
    data() {
        return {
            recipe: {} 
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

    },
    mounted() {
        // this.recipe = this.$store.state.recipe
        getRecipeClass(this.$route.params.id)
            .then((recipe) => {
                this.recipe = recipe
            })
    }
}
</script>

<style>

</style>
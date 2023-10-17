<template>
    <div>
        <h1>Create Recipe</h1>
        <form @submit.prevent="handleSubmit">
            <label>Title:</label>
            <input type="text" v-model="title">
            <label>Description:</label>
            <input type="text" v-model="desc">
            <div class="submit">
                <button>Create</button>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            title: '',
            desc: '',
        }
    },
    methods: {
        async handleSubmit(){
            try {
                const response = await axios.post('http://localhost:5000/createrecipe', {
                    name: this.title,
                    desc: this.desc
                })
                console.log(response)
            }
            catch(err){
                console.log(err)
            }
            this.title = ''
            this.desc = ''

        }
    }
}
</script>

<style>

form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
  }
  label {
    /* color: #aaa; */
    color: var(--primary-color);
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
  }
  input, select {
    background: white;
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  button {
    background: var(--secondary-color);
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
    cursor: pointer;
  }
  .submit {
    text-align: center;
  }
</style>
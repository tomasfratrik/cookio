<!-- ITU project 
  -- AUTHOR: xfratr01
-->
<template>
  <!-- <div v-if="isShowing" :class="{ success: theme === 'success', error: theme === 'error'}" > -->
    <div v-if="isShowing" :class="['alert', isActive ? 'active' : '', theme === 'success' ? 'success' : '', theme === 'error' ? 'error' : '', theme === 'warn' ? 'warn' : '']">
        <div v-if="theme === 'error'">
            <h2>Error</h2>
        </div>
        <div v-if="theme === 'success'">
            <h2>Success</h2>
        </div>
        <div v-if="theme === 'warn'">
            <h2>Alert</h2>
        </div>
        <div class="msg">
            {{ message }}
        </div>
    </div>
</template>

<script>
export default {
    // props: ['theme'],
    data() {
        return {
            isShowing: false,
            isActive: false,
            theme: '',
            message: ''
        }
    },
    methods: {
        showAlert(theme, message) {
            this.message = message;
            this.theme = theme;
            this.isShowing = true;

            setTimeout(() => {
                // this.isActive = true;
                this.isShowing = false;
            }, 1000); 

            // setTimeout(() => {
            //     this.isShowing = false;
            //     this.isActive = false;
            // }, 2000); 
        },
    }
}
</script>

<style scoped>
.alert {
    position: fixed;
    padding: 20px;
    width: 300px;
    background: white;
    top: -5px;
    left: 50%;
    transform: translateX(-50%);
    height: 100px;
    color: white;
    border-radius: 10px;

    opacity: 0;
    animation: showAlert 1s ease-out;
}

@keyframes showAlert{
    0% {
        top: -5px;
        opacity: 0;
    }
    33% {
        top: 10px;
        opacity: 1;
    }
    66% {
        top: 10px;
        opacity: 1;
    }
    100% {
        top: -5px;
        opacity: 0;
    }
}

@keyframes moveUp {
  from {
    top: 10px;
  }
  to {
    top: -100px;
  }
}
.alert.success {
    background: lightgreen;
    border: 1px solid green;
}

.alert.error {
    background: rgb(216, 113, 113);
    border: 1px solid red;
}
.alert.warn {
    background: rgb(255, 244, 180);
    border: 1px solid orange;
}

.error h2 {
    color: red;
}

.success h2 {
    color: green;
}

.warn h2 {
    color: orange;
}

.msg {
    color: white;
    display: block;
    margin: auto auto;
    font-size: 17px;
    text-align: center;
    font-weight: bold;

}

.warn .msg {
    color: black;
}


</style>
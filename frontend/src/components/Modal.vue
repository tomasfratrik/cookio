<template>
    <div class="backdrop" ref="popup" @click.self="closeModal">
        <div class="modal">
            <slot>

            </slot>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        closeModal() {
            // this.$refs.popup.style.display = 'none'
            this.$emit('close')
        }
    }
}
</script>

<style>
.modal {
    width: 400px;
    padding: 20px;
    margin: 100px auto;
    background: white;
    border-radius: 10px;
    position: fixed;
    left: 33%;
}

.backdrop {
    position: fixed;
    top: 0;
    left:0;
    width: 120%;
    height: 120%;
    background: rgba(0, 0, 0, 0.5);
}
</style>
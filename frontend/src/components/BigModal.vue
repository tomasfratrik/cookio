<!-- ITU project 
  -- AUTHOR: xfratr01
-->
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
    width: 900px;
    padding: 20px;
    margin: 50px auto;
    background: white;
    border-radius: 10px;
    position: fixed;
    left: calc(50% - 450px);

}

.backdrop {
    position: fixed;
    top: 0;
    left:0;
    width: 120%;
    height: 120%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 100;
}
</style>
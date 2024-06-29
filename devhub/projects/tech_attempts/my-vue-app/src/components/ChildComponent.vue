<template>
  <div>
    <p>Child Component: Count is {{ count }}</p>
    <button @click="reset">Reset Count</button>
  </div>
</template>

<script>
export default {
  name: 'ChildComponent',
  props: {
    count: Number
  },
  methods: {
    reset() {
      this.$emit('reset');
    }
  }
}
</script>

<style scoped>
button {
  margin-top: 10px;
}
</style>

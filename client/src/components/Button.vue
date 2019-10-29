<template>
  <button class="button" @click="$emit('click')">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'Button',
};
</script>

<style lang="scss" scoped>
.button {
  width: 100%;
  border: 0;
  font-weight: 700;
  padding: 1rem 5rem;
  background: #dff9fb;
  transition: transform 0.2s;
  font-size: 1.6rem;
  font-family: inherit;
  &:focus,
  &:hover {
    transform: translateY(-0.4rem);
  }

  &:active {
    transform: translateY(-0.1rem);
  }
}
</style>

<template>
  <div class="scale-select">
    <label for="scale" class="scale-select__label">Scale (0 - 1):</label>
    <input
      v-model="scale"
      type="number"
      name="scale"
      id="scale"
      step="0.1"
      class="scale-select__input"
    />
  </div>
</template>

<script>
export default {
  name: 'InverseSelect',
  computed: {
    scale: {
      get() {
        return this.$store.state.scale;
      },
      set(scale) {
        this.$store.dispatch('changeScale', scale);
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.scale-select {
  display: flex;
  align-items: center;
  margin-bottom: 3rem;
  margin-left: 1rem;
  width: 100%;
  &__label {
    font-weight: 700;
    color: #fff;
    font-weight: 700;
    font-size: 1.6rem;
    text-transform: uppercase;
  }

  &__input {
    background: transparent;
    border: 0;
    padding: 0;
    margin: 0 1rem;
    width: 3rem;
    font-size: 1.6rem;
    color: #fff;
    font-family: inherit;
    font-weight: 700;
  }
}
</style>

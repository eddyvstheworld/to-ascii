<template>
  <div class="column-select">
    <label for="columns" class="column-select__label">Number of columns:</label>
    <input
      v-model="columns"
      type="number"
      name="columns"
      id="columns"
      class="column-select__input"
    />
  </div>
</template>

<script>
export default {
  computed: {
    columns: {
      get() {
        return this.$store.state.columns;
      },
      set(columns) {
        this.$store.dispatch('changeColumns', columns);
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.column-select {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  margin-left: 1rem;
  width: 100%;
  margin-top: 3rem;
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

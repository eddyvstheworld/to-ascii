<template>
  <div class="inverse-select">
    <label for="inverse">INVERSE CONTRAST (Y/N): {{ getInversedText }}</label>
    <input
      type="checkbox"
      name="inverse"
      id="inverse"
      v-model="inversed"
      style="display: none"
    />
  </div>
</template>

<script>
export default {
  name: 'InverseSelect',
  computed: {
    inversed: {
      get() {
        return this.$store.state.inversed;
      },
      set(inversed) {
        this.$store.dispatch('changeInversed', inversed);
      },
    },
    getInversedText() {
      return this.inversed ? 'Y' : 'N';
    },
  },
};
</script>

<style lang="scss" scoped>
.inverse-select {
  margin-bottom: 1rem;
  font-family: inherit;
  color: inherit;
  font-weight: 700;
  font-size: 1.6rem;
  width: 100%;
  display: flex;
  margin-left: 1rem;
}
</style>

<template>
  <div class="converted-image-container">
    <p class="converted-image-container__result" v-text="convertedData"></p>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['convertedData']),
  },
};
</script>

<style lang="scss" scoped>
.converted-image-container {
  position: relative;
  height: 100%;
  width: 100%;

  &__result {
    color: #fff;
    white-space: pre;
    font-size: 8px;
    overflow: auto;
    position: absolute;
    top: 2rem;
    left: 2rem;
    width: calc(100% - 4rem);
    height: calc(100% - 4rem);
  }
}
</style>

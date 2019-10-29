<template>
  <MessageBox v-model="showInvalidImageType" v-if="showInvalidImageType">
    <template slot="title">
      Invalid File Format
    </template>
    <template slot="message">
      <p>
        The file you've uploaded is not a valid image.
        Please verify that the file is among the followings types:
        <ul class='file-types'>
          <li>JPG</li>
          <li>JPEG</li>
          <li>GIF</li>
          <li>PNG</li>
        </ul>
      </p>
    </template>
  </MessageBox>
</template>

<script>
import MessageBox from '../MessageBox.vue';

export default {
  computed: {
    showInvalidImageType: {
      get() {
        return this.$store.state.showInvalidImageType;
      },
      set(show) {
        this.$store.dispatch('toggleInvalidImageError', show);
      },
    },
  },
  name: 'InvalidImageErrorDialog',
  components: { MessageBox },
};
</script>
<style lang='scss' scoped>
.file-types {
  margin: 2rem;
}
</style>

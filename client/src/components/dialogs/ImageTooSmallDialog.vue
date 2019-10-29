<template>
  <MessageBox v-model="showImageTooSmallError" v-if="showImageTooSmallError">
    <template slot="title">
      Image Too Small Error
    </template>
    <template slot="message">
      <p>
        Your image is too small for the specified number of columns. Please
        select a smaller number and try again.
      </p>
    </template>
  </MessageBox>
</template>

<script>
import MessageBox from '../MessageBox.vue';

export default {
  computed: {
    showImageTooSmallError: {
      get() {
        return this.$store.state.showImageTooSmallError;
      },
      set(show) {
        this.$store.dispatch('toggleShowImageTooSmallError', show);
      },
    },
  },
  name: 'ImageTooSmallError',
  components: { MessageBox },
};
</script>

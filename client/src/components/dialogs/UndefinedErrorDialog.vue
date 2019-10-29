<template>
  <MessageBox v-model="showUndefinedError" v-if="showUndefinedError">
    <template slot="title">
      Critical Error
    </template>
    <template slot="message">
      <p>
        Something went wrong with the conversion process. Please verify that you
        uploaded a valid image and used valid settings before trying again.
      </p>
    </template>
  </MessageBox>
</template>

<script>
import MessageBox from '../MessageBox.vue';

export default {
  computed: {
    showUndefinedError: {
      get() {
        return this.$store.state.showUndefinedError;
      },
      set(show) {
        this.$store.dispatch('toggleUndefinedError', show);
      },
    },
  },
  name: 'UndefinedErrorDialog',
  components: { MessageBox },
};
</script>

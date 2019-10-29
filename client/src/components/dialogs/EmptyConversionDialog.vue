<template>
  <MessageBox v-model="showEmptyError" v-if="showEmptyError">
    <template slot="title">
      Empty Image Error
    </template>
    <template slot="message">
      <p>
        You cannot convert an empty image file. Please verify that you have
        selected an image and try again.
      </p>
    </template>
  </MessageBox>
</template>

<script>
import MessageBox from '../MessageBox.vue';

export default {
  computed: {
    showEmptyError: {
      get() {
        return this.$store.state.showEmptyError;
      },
      set(show) {
        this.$store.dispatch('toggleShowEmptyError', show);
      },
    },
  },
  name: 'EmptyConversionDialog',
  components: { MessageBox },
};
</script>

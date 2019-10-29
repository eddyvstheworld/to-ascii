<template>
  <MessageBox v-model="showAbout" v-if="showAbout">
    <template slot="title">
      Hello!
    </template>
    <template slot="message">
      <p>My name is Edward and I'm a full stack developer.</p>
      <p>
        My passions revolve around making custom solutions and experimenting
        with the most up to date technologies.
      </p>
      <br />
      <p>
        If you'd like to reach out to me, don't hesitate to email me at
        <a href="mailto:edw_lu@protonmail.ch">edw_lu@protonmail.ch</a>
      </p>
      <br />
      <p>
        Thank you!
      </p>
    </template>
  </MessageBox>
</template>

<script>
import MessageBox from '../MessageBox.vue';

export default {
  computed: {
    showAbout: {
      get() {
        return this.$store.state.showAbout;
      },
      set(show) {
        this.$store.dispatch('toggleShowAbout', show);
      },
    },
  },
  name: 'AboutDialog',
  components: { MessageBox },
};
</script>

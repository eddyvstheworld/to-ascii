<template>
  <MessageBox v-model="showThemes" v-if="showThemes">
    <template slot="title">
      Themes
    </template>
    <template slot="message">
      <div class="themes-container">
        <div
          v-for="theme in themes"
          :key="theme.name"
          class="themes-container__item"
        >
          <button
            class="themes-container__item__button"
            :style="{ background: theme.color }"
            @click="changeTheme(theme.name)"
          ></button>
          <span class="themes-container__item__text">{{ theme.name }}</span>
        </div>
      </div>
    </template>
  </MessageBox>
</template>

<script>
import { mapState } from 'vuex';
import MessageBox from '../MessageBox.vue';

export default {
  computed: {
    ...mapState(['themes']),
    showThemes: {
      get() {
        return this.$store.state.showThemes;
      },
      set(show) {
        this.$store.dispatch('toggleThemeDialog', show);
      },
    },
  },
  name: 'ThemeDialog',
  methods: {
    changeTheme(name) {
      this.$store.dispatch('changeCurrentTheme', name);
      try {
        localStorage.setItem('theme', name);
      } catch (ex) {
        console.error(ex);
      }
    },
  },
  components: { MessageBox },
};
</script>
<style lang="scss" scoped>
.themes-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  align-content: flex-start;

  &__item {
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 8rem;

    &__button {
      padding: 2rem;
      border: 0;
    }

    &__text {
      font-family: inherit;
      text-transform: uppercase;
      font-weight: 700;
    }
  }
}
</style>

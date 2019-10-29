<template>
  <nav class="options">
    <ul class="options__list">
      <li class="options__list__item">
        <button class="options__list__item__button" @click="showThemeDialog">
          Themes
        </button>
      </li>
      <li class="options__list__item">
        <button class="options__list__item__button" @click="saveText">
          Save
        </button>
      </li>
      <li class="options__list__item">
        <button class="options__list__item__button" @click="showAboutDialog">
          About
        </button>
      </li>
    </ul>
  </nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['convertedData']),
  },
  methods: {
    saveText() {
      if (this.convertedData) {
        const file = new Blob([this.convertedData], { type: 'txt' });
        if (window.navigator.msSaveOrOpenBlob) {
          window.navigator.msSaveOrOpenBlob(file, 'ascii_art');
        } else {
          const a = document.createElement('a');
          const url = URL.createObjectURL(file);
          a.href = url;
          a.download = 'ascii_art';
          document.body.appendChild(a);
          a.click();
          setTimeout(() => {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
          }, 0);
        }
      } else {
        this.$emit('show-empty-error');
      }
    },
    showThemeDialog() {
      this.$emit('show-theme');
    },
    showAboutDialog() {
      this.$emit('show-about');
    },
  },
};
</script>

<style lang="scss" scoped>
.options {
  padding: 1rem 4rem;
  border-bottom-width: 0.75rem;
  border-bottom-style: solid;
  border-bottom-color: inherit;

  &__list {
    list-style: none;
    display: flex;
    &__item {
      font-size: 1.4rem;
      font-weight: 700;
      text-transform: uppercase;
      &:not(:last-child) {
        margin-right: 3rem;
      }

      &__button {
        background: transparent;
        border: 0;
        font-size: 1.6rem;
        font-family: inherit;
        text-transform: uppercase;
        color: #fff;
        font-weight: 700;
      }
    }
  }
}
</style>

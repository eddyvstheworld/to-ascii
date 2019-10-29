<template>
  <div class="ascii-app" id="app">
    <fieldset :class="fieldSetCSS">
      <legend>
        <p>GITHUB @ eddyvstheworld</p>
      </legend>
      <div class="ascii-app__content">
        <div class="ascii-app__content__options">
          <ImageSelect />
          <ColumnsSelect />
          <InverseSelect />
          <ScaleSelect />
          <Button @click="sendImage">CONVERT</Button>
        </div>
        <div class="ascii-app__content__output">
          <Options
            @show-about="showAboutDialog"
            @show-empty-error="showEmptyErrorDialog"
            @show-theme="showThemeDialog"
          />
          <ConvertedImage />
        </div>
      </div>
    </fieldset>
    <AboutDialog />
    <EmptyConversionDialog />
    <ImageTooSmallDialog />
    <UndefinedErrorDialog />
    <InvalidErrorDialog />
    <ThemeDialog />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Button from './components/Button.vue';
import ImageSelect from './components/ImageSelect.vue';
import ColumnsSelect from './components/ColumnsSelect.vue';
import InverseSelect from './components/InverseSelect.vue';
import ScaleSelect from './components/ScaleSelect.vue';
import ConvertedImage from './components/ConvertedImage.vue';
import Options from './components/Options.vue';
import EmptyConversionDialog from './components/dialogs/EmptyConversionDialog.vue';
import ImageTooSmallDialog from './components/dialogs/ImageTooSmallDialog.vue';
import UndefinedErrorDialog from './components/dialogs/UndefinedErrorDialog.vue';
import AboutDialog from './components/dialogs/AboutDialog.vue';
import InvalidErrorDialog from './components/dialogs/InvalidErrorDialog.vue';
import ThemeDialog from './components/dialogs/ThemeDialog.vue';

export default {
  name: 'app',
  components: {
    Button,
    ImageSelect,
    ColumnsSelect,
    InverseSelect,
    ScaleSelect,
    ConvertedImage,
    Options,
    EmptyConversionDialog,
    ImageTooSmallDialog,
    UndefinedErrorDialog,
    AboutDialog,
    InvalidErrorDialog,
    ThemeDialog,
  },
  created() {
    try {
      const theme = localStorage.getItem('theme');
      if (theme) {
        this.$store.dispatch('changeCurrentTheme', theme);
      }
    } catch (ex) {
      console.error(ex);
    }
  },
  data() {
    return {
      imageTooSmallError: 'ImageTooSmallError',
      undefinedError: 'UndefinedError',
      invalidImageError: 'InvalidImageError',
    };
  },
  computed: {
    ...mapState(['currentTheme']),
    fieldSetCSS() {
      return {
        'ascii-app__fieldset': true,
        'ascii-app__fieldset--purple': this.currentTheme === 'purple',
        'ascii-app__fieldset--dark': this.currentTheme === 'dark',
        'ascii-app__fieldset--red': this.currentTheme === 'red',
        'ascii-app__fieldset--blue': this.currentTheme === 'blue',
        'ascii-app__fieldset--orange': this.currentTheme === 'orange',
        'ascii-app__fieldset--indigo': this.currentTheme === 'indigo',
        'ascii-app__fieldset--solarized': this.currentTheme === 'solarized',
      };
    },
  },
  methods: {
    showErrorType({ type }) {
      switch (type) {
        case this.imageTooSmallError:
          this.$store.dispatch('toggleShowImageTooSmallError', true);
          break;
        case this.undefinedError:
          this.$store.dispatch('toggleUndefinedError', true);
          break;
        case this.invalidImageError:
          this.$store.dispatch('toggleInvalidImageError', true);
          break;
        default:
          this.$store.dispatch('toggleUndefinedError', true);
          break;
      }
    },
    sendImage() {
      this.$store.dispatch('convertImage').then(() => {}, (error) => {
        if (error.status && error.type) {
          this.showErrorType(error);
        }
      });
    },
    showEmptyErrorDialog() {
      this.$store.dispatch('toggleShowEmptyError', true);
    },
    showAboutDialog() {
      this.$store.dispatch('toggleShowAbout', true);
    },
    showThemeDialog() {
      this.$store.dispatch('toggleThemeDialog', true);
    },
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Inconsolata:400,700&display=swap");

$color-blue-1: #70a1ff;
$color-blue-2: #1e90ff;
$color-dark-1: #636e72;
$color-dark-2: #2d3436;
$color-indigo-1: #30336b;
$color-indigo-2: #130f40;
$color-orange-1: #ff7f50;
$color-orange-2: #ff6348;
$color-purple-1: #686de0;
$color-purple-2: #4834d4;
$color-red-1: #eb2f06;
$color-red-2: #b71540;
$color-solarized-1: #073642;
$color-solarized-2: #002b36;
$color-white-1: #fff;
$options-width: 30rem;

*,
*::before,
*::after {
  padding: 0;
  margin: 0;
  box-sizing: inherit;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}

html {
  font-size: 62.5%;
  height: 100%;
}

body {
  height: 100%;
}

.ascii-app__fieldset {
  height: 100%;
  font-family: "Inconsolata";
  background: $color-purple-2;
  border: 2rem double $color-purple-1;
  border-color: $color-purple-1;
  color: $color-white-1;

  &--dark {
    background: $color-dark-2;
    border-color: $color-dark-1;
  }

  &--blue {
    background: $color-blue-2;
    border-color: $color-blue-1;
  }

  &--orange {
    background: $color-orange-2;
    border-color: $color-orange-1;
  }

  &--indigo {
    background: $color-indigo-2;
    border-color: $color-indigo-1;
  }

  &--red {
    background: $color-red-2;
    border-color: $color-red-1;
  }

  &--solarized {
    background: $color-solarized-2;
    border-color: $color-solarized-1;
  }
  & * {
    border-color: inherit;
  }
}

legend {
  text-align: center;
  margin: 0 auto;
  padding: 0 1rem;
  color: inherit;
  width: auto;
  display: block;
  font-family: "Inconsolata";
  font-weight: 700;
  letter-spacing: 1.3px;
  text-transform: uppercase;
  font-size: 1.5rem;
}
body {
  overflow: hidden;
  box-sizing: border-box;
  font-family: "Inconsolata", sans-serif;
}

.ascii-app {
  height: 100%;
  width: 100%;

  &__content {
    height: 100%;
    width: 100%;
    display: flex;
    &__output {
      display: flex;
      flex-direction: column;
      height: 100%;
      width: 100%;
    }

    &__options {
      height: 100%;
      width: $options-width;
      display: flex;
      flex-direction: column;
      align-items: center;
      flex: 0 0 $options-width;
      padding: 1rem 2rem;
      border-right-style: solid;
      border-right-width: 5px;
    }
  }
}
</style>

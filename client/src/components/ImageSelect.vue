<template>
  <div>
    <div
      class="image-select"
      :style="{ backgroundImage: 'url(' + imageString + ')' }"
    >
      <span v-if="!imageString">Please load an image</span>
    </div>
    <label for="image">
      <Button @click="$refs.imageInput.click()">SELECT AN IMAGE</Button>
      <input
        type="file"
        name="image"
        id="image"
        ref="imageInput"
        style="display:none"
        @change="receiveImage"
      />
    </label>
  </div>
</template>

<script>
import Button from './Button.vue';

export default {
  name: 'ImageSelect',
  components: { Button },
  computed: {
    imageString: {
      get() {
        return this.$store.state.imageString;
      },
      set(imageString) {
        this.$store.dispatch('changeImageString', imageString);
      },
    },
  },
  methods: {
    receiveImage(e) {
      e.preventDefault();
      const file = this.$refs.imageInput.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        this.imageString = reader.result;
      };
      reader.readAsDataURL(file);
    },
  },
};
</script>

<style lang="scss" scoped>
.image-select {
  width: 16rem;
  height: 16rem;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  border-style: solid;
  border-width: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: inherit;
  text-transform: uppercase;
  margin: 0 auto;
  margin-bottom: 2rem;
}
</style>

<template>
  <div class="message-box">
    <div class="message-box__dialog">
      <h1 class="message-box__dialog__title">
        <slot name="title"></slot>
      </h1>
      <p class="message-box__dialog__message">
        <slot name="message"></slot>
      </p>
      <div class="message-box__dialog__button">
        <Button @click="toggleShow">OK</Button>
      </div>
    </div>
  </div>
</template>

<script>
import Button from './Button.vue';

export default {
  name: 'MessageBox',
  components: { Button },
  props: ['value'],
  data() {
    return {
      title: '',
      msg: '',
      show: false,
    };
  },
  model: {
    prop: 'value',
    event: 'toggleShow',
  },
  methods: {
    toggleShow() {
      this.$emit('toggleShow', false);
    },
  },
};
</script>

<style lang="scss" scoped>
.message-box {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: inherit;

  &__dialog {
    padding: 4rem 5rem;
    background: #95afc0;
    color: #130f40;
    max-width: 30%;

    &__button {
      margin: 0 auto;
    }

    &__title {
      font-weight: 700;
      font-size: 2.2rem;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }

    &__message {
      font-size: 1.6rem;
      margin-bottom: 2rem;
    }
  }
}
</style>

import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    imageString: '',
    convertedData: '',
    inversed: false,
    columns: 80,
    scale: 0.5,
    showAbout: false,
    showEmptyError: false,
    showImageTooSmallError: false,
    showUndefinedError: false,
    showInvalidImageType: false,
    showThemes: false,
    currentTheme: 'purple',
    themes: [
      { name: 'dark', color: '#2d3436' },
      { name: 'purple', color: '#4834d4' },
      { name: 'red', color: '#b71540' },
      { name: 'blue', color: '#22a6b3' },
      { name: 'orange', color: '#f0932b' },
      { name: 'indigo', color: '#130f40' },
      { name: 'solarized', color: '#073642' },
    ],
    path: 'http://localhost:5000/image',
  },
  getters: {},
  mutations: {
    changeImageString(state, imageString) {
      state.imageString = imageString;
    },
    changeConvertedData(state, convertedData) {
      state.convertedData = convertedData;
    },
    changeColumns(state, columns) {
      state.columns = columns;
    },
    changeInversed(state, inversed) {
      state.inversed = inversed;
    },
    changeScale(state, scale) {
      state.scale = scale;
    },
    changeShowEmptyError(state, show) {
      state.showEmptyError = show;
    },
    changeShowImageTooSmallError(state, show) {
      state.showImageTooSmallError = show;
    },
    changeUndefinedError(state, show) {
      state.showUndefinedError = show;
    },
    changeShowAbout(state, show) {
      state.showAbout = show;
    },
    changeInvalidImageError(state, show) {
      state.showInvalidImageType = show;
    },
    changeShowTheme(state, show) {
      state.showThemes = show;
    },
    changeCurrentTheme(state, color) {
      state.currentTheme = color;
    },
  },
  actions: {
    changeCurrentTheme(context, color) {
      context.commit('changeCurrentTheme', color);
    },
    toggleThemeDialog(context, show) {
      context.commit('changeShowTheme', show);
    },
    toggleInvalidImageError(context, show) {
      context.commit('changeInvalidImageError', show);
    },
    toggleShowAbout(context, show) {
      context.commit('changeShowAbout', show);
    },
    toggleUndefinedError(context, show) {
      context.commit('changeUndefinedError', show);
    },
    toggleShowImageTooSmallError(context, show) {
      context.commit('changeShowImageTooSmallError', show);
    },
    toggleShowEmptyError(context, show) {
      context.commit('changeShowEmptyError', show);
    },
    changeImageString(context, imageString) {
      context.commit('changeImageString', imageString);
    },
    changeColumns(context, columns) {
      context.commit('changeColumns', columns);
    },
    changeInversed(context, inversed) {
      context.commit('changeInversed', inversed);
    },
    changeScale(context, scale) {
      context.commit('changeScale', scale);
    },
    convertImage(context) {
      return new Promise((resolve, reject) => {
        try {
          const { columns, inversed, scale } = context.state;
          axios
            .post(context.state.path, {
              data: context.state.imageString,
              columns: parseInt(columns, 10),
              inversed,
              scale: parseFloat(scale, 10),
            })
            .then((response) => {
              if (response.data.status === 'error') {
                reject(response.data);
              } else {
                context.commit('changeConvertedData', response.data.image);
                resolve();
              }
            }, (error) => {
              reject(error);
            });
        } catch (ex) {
          reject(ex);
        }
      });
    },
  },
});

export default store;

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify/lib'

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

Vue.config.productionTip = false

const axiosInstance = axios.create({
  // Ovdje postavite osnovni URL za API
  baseURL: 'http://127.0.0.1:8000',
})

axiosInstance.interceptors.request.use(
  (config) => {
    // Ovdje dodajte logiku za dodavanje tokena u zaglavlje zahtjeva
    const token = store.state.token;
    if (token) {
      config.headers.Authorization = 'Bearer ${token}';
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')

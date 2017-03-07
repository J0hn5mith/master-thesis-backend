import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import * as Vue2Leaflet from 'vue2-leaflet' // Required for using with external templates

Vue.component('v-map', Vue2Leaflet.Map);
Vue.component('v-tilelayer', Vue2Leaflet.TileLayer);


import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import './components/TagList.js'
import TagOverviewMap from './components/map.js'
//import * as Vue2Leaflet from 'vue2-leaflet' // Required for using with external templates

//Vue.component('v-map', Vue2Leaflet.Map);
//Vue.component('v-tilelayer', Vue2Leaflet.TileLayer);


var vue = new Vue({
  el: '#vue',
  components: {
    'v-tag-overview-map': TagOverviewMap,
  },
  created: function(){
  },
  methods: {
  },
})

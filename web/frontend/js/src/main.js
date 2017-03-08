import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import './components/TagList.js'
import TagOverviewMap from './components/TagOverviewMap.js'
import TagDetailMap from './components/TagDetailMap.js'
import DataSource from './DataSource.js'


////////////////////////////////////////
// Settings
////////////////////////////////////////
L.Icon.Default.imagePath = "/static/img/";


////////////////////////////////////////
// Globals
////////////////////////////////////////


var vue = new Vue({
  el: '#vue',
  components: {
    'v-tag-overview-map': TagOverviewMap,
    'v-tag-detail-map': TagDetailMap,
  },
  created: function(){
  },
  methods: {
  },
})

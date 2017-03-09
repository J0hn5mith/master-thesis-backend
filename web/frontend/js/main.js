import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import TagOverviewMap from './src/components/TagOverviewMap.js'
import DataSource from './src/DataSource.js'
import TagTable from './vue-components/tag_table.vue'


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
    //'v-tag-detail-map': TagDetailMap,
    'v-tag-table': TagTable,
  },
  created: function(){
  },
  methods: {
  },
})

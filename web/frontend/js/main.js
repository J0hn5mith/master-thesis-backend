import * as Vue from 'vue/dist/vue.common.js'; // Required for using with external templates
import TagOverviewMap from './vue-components/tag_overview_map.vue';
import TagTable from './vue-components/tag_table.vue';
import UserSettings from './vue-components/user_settings.vue';
import RESTClient from './src/RESTClient.js';


////////////////////////////////////////
// Settings
////////////////////////////////////////
L.Icon.Default.imagePath = '/static/img/';


////////////////////////////////////////
// Globals
////////////////////////////////////////

////////////////////////////////////////
// Utils
////////////////////////////////////////
if (!String.prototype.format) {
  String.prototype.format = function() {
    'use strict';
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] !== 'undefined' ? args[number] : match
      ;
    });
  };
}

var vue = new Vue({
  el: '#vue',
  components: {
    'v-tag-overview-map': TagOverviewMap,
    //'v-tag-detail-map': TagDetailMap,
    'v-tag-table': TagTable,
    'v-user-settings': UserSettings,
  },
  data: {
    //function() {return {user: {}};},
    user: false,
  },
  beforeCreate: function(){
    'use strict';
    var restClient = new RESTClient();
    restClient.getCurrentUser(function(data){
      this.user = data;
    }.bind(this));
  },
  created: function(){
  },
  methods: {
  },
  filters: {
    coordinates: function (coordinates) {
      'use strict';
      return coordinates.lat + ' | ' + coordinates.lng;
    },
  },
});

export default vue;

import TagTable from '../tag_table.vue';
import SharedTagTable from '../shared_tag_table.vue';
import TagOverviewMap from '../tag_overview_map.vue';
import RESTClient from './../../src/RESTClient.js';

var Dashboard = {
  components: {
    'v-tag-overview-map': TagOverviewMap,
    'v-tag-table': TagTable,
    'v-shared-tag-table': SharedTagTable,
  },
  data:  function() {
    return {
      tags:[],
      sharedTags:[],
      sharedTagsTags:[], //Only the tag objects of the shared tags
    };
  },
  beforeCreate: function(){
    var restClient = new RESTClient();
    restClient.getTags(
      function (results) { this.tags = this.tags.concat(results);}.bind(this),
      function (error) { console.log(error);}
    );
    restClient.getSharedTags(
      function (sharedTags) {
        var tags = [];
        for (var i = 0; i < sharedTags.length; i++) {
          sharedTags[i].tag.hover = false;
          this.sharedTagsTags.push(sharedTags[i].tag);
        }
        this.sharedTags = sharedTags;
      }.bind(this),
      function (error) { console.log(error);}
    );
  },
};
export default Dashboard;

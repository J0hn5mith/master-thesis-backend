import TagTable from '../tag_table.vue';
import SharedTagTable from '../shared_tag_table.vue';
import TagOverviewMap from '../tag_overview_map.vue';
import RESTClient from './../../src/RESTClient.js';
import UserData from './../../src/UserData.js';

var Dashboard = {
  components: {
    'v-tag-overview-map': TagOverviewMap,
    'v-tag-table': TagTable,
    'v-shared-tag-table': SharedTagTable,
  },
  data:  function() {
    return {
      tags:[],
      userData: new UserData(),
      sharedTags:[],
      sharedTagsTags:[], //Only the tag objects of the shared tags
    };
  },
  beforeCreate: function(){
    this.$emit('newMessage');
  },
};
export default Dashboard;

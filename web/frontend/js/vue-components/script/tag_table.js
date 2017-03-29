import TagTableEntry from '../tag_table_entry.vue';
import TagRegistrationModal from '../tag_registration_modal.vue';
import RESTClient from './../../src/RESTClient.js';


var TagTable = {
  components: {
    'v-tag-table-entry': TagTableEntry,
    'v-tag-registration-modal': TagRegistrationModal,
  },
  data: function(){
    return{
      tags: [],// Are set when mounted via AJAX
    };
  },
  created: function(){
    var instance = this;
    var restClient = new RESTClient();

    restClient.getTags(
      function (results) { instance.tags = results;},
      null
    );
  },
  computed: {
    hasTags: function(){
      return this.tags.length > 0;
    }
  }
};
export default TagTable;

import TagTableEntry from '../tag_table_entry.vue'
import axios from 'axios'
var TagTable = {
  components: {
     'v-tag-table-entry': TagTableEntry,
  },
  data: function(){
    return{
      tags: [],// Are set when mounted via AJAX
    }
  },
  created: function(){
    var instance = this;
    axios.get('/tags/rest/tags', { })
      .then(function (response) { instance.tags = response.data.results; })
      .catch(function (error) { console.log(error); });
  }
}
export default TagTable;

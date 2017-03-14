import PMTableEntry from '../pm_table_entry.vue'
import RESTClient from './../../src/RESTClient.js'

var PositionMeasurements = {
  props: ['tag'],
  components: {
    'v-pm-table-entry': PMTableEntry,
  },
  data: function(){
    return {
      measurements: [],
    }
  },
  created: function(){
    var instance = this;
    var restClient = new RESTClient();
    restClient.getTagData(instance.tag.uid).then(function (response) {
      instance.measurements = response.data.results;
    }).catch(function (error) {
      console.log(error);
    });
  },
  methods: {
    deleteTag: function(){
      this.measurements.splice(0,1);
    }

  }
}
export default PositionMeasurements;

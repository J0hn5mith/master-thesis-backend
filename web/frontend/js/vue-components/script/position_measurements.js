import PMTableEntry from '../pm_table_entry.vue'


var PositionMeasurements = {
  props: {
    tag: Object,
    posMes: Array,
  },
  components: {
    'v-pm-table-entry': PMTableEntry,
  },
  data: function(){return {}},
}
export default PositionMeasurements;

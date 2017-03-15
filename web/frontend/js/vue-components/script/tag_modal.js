import TagChargeBar from '../tag_charge_bar.vue'
import TagToggle from '../tag_toggle.vue'
import TagDetailMap from '../tag_detail_map.vue'
import PositionMeasurements from '../position_measurements.vue'
import CollapseSection from '../collapse_section.vue'
import RESTClient from './../../src/RESTClient.js'

function fetchPosMes(instance){
  var restClient = new RESTClient();
  restClient.getTagData(instance.tag.uid).then(function (response) {
    instance.posMes = response.data.results;
  }).catch(function (error) {
    console.log(error);
  });
}

//https://vuejs.org/v2/examples/modal.html
var TagModal = {
  props: {
    tag: Object,
  },
  components: {
    'v-tag-charge-bar': TagChargeBar,
    'v-tag-toggle': TagToggle,
    'v-tag-detail-map': TagDetailMap,
    'v-position-measurements': PositionMeasurements,
    'v-collapse-section': CollapseSection,
  },
  created: function(){
    fetchPosMes(this);
  },
  data: function(){
    return{
      posMes: [],
    }
  },
  methods: {
    setCenterToCurrentPosition: function(){
      if (this.tag.current_position && this.tag.alarm_config.area){
        this.tag.alarm_config.area.center.coordinates = this.tag.current_position.position.coordinates;
      }
    },
    save: function (event) {
      var restClient = new RESTClient();
      restClient.update(this.tag);
    },
  },
  watch: {
    // whenever question changes, this function will run
    'tag': function (value, oldValue) {
      console.log(value);
    },
    'tag.name': function (value, oldValue) {
      this.save();
    },
    'tag.alarm_config.area.center.coordinates': function(value, oldValue){
      var instance = this;
      var restClient = new RESTClient();
      restClient.update(this.tag, null, function(){
        instance.alarm_config.area.center.coordinates = oldValue;
        console.log(error);
      });
    },
    'tag.alarm_config.area.radius': function(value, oldValue){
      var instance = this;
      var restClient = new RESTClient();
      restClient.update(this.tag, null, function(){
        instance.alarm_config.area.center.radius = oldValue;
        console.log(error);
      });
    },
  },
}

export default TagModal;

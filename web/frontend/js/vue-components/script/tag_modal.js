import TagChargeBar from '../tag_charge_bar.vue';
import TagToggle from '../tag_toggle.vue';
import TagDetailMap from '../tag_detail_map.vue';
import SliderControll from '../slider_controll.vue';
import PositionMeasurements from '../position_measurements.vue';
import CollapseSection from '../collapse_section.vue';
import RESTClient from './../../src/RESTClient.js';

function fetchPosMes(instance){
  var restClient = new RESTClient();
  restClient.getSensorData(instance.tag.uid, function (data) {
    instance.posMes = data;
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
    'v-slider-controll': SliderControll,
  },
  created: function(){
    fetchPosMes(this);
  },
  data: function(){
    return{
      posMes: [],
    };
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
    },
    'tag.name': function (value, oldValue) {
      this.save();
    },
    'tag.alarm_config.area.center.coordinates': function(value, oldValue){
      var instance = this;
      var restClient = new RESTClient();
      restClient.update(this.tag, null, function(){
        instance.alarm_config.area.center.coordinates = oldValue;
      });
    },
    'tag.alarm_config.area.radius': function(value, oldValue){
      var instance = this;
      var restClient = new RESTClient();
      restClient.update(this.tag, null, function(){
        instance.alarm_config.area.center.radius = oldValue;
      });
    },
  },
};

export default TagModal;

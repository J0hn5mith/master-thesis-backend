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
    tags: Array,
    triggerModal: Boolean, // When this value changes, the modal's visibility is toggled.
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
    this.visible = window.location.pathname.endsWith(this.tag.pk +  "/");
  },
  data: function(){
    return{
      posMes: [],
      visible: false,
    };
  },
  methods: {
    toggle: function(){
      this.visible = !this.visible;
      if (this.visible){
        window.history.pushState({}, "", this.tag.pk + "/");
      } else {
        window.history.pushState({}, "", "./../");
      }
    },
    setCenterToCurrentPosition: function(){
      if (this.tag.current_position && this.tag.alarm_config.area){
        this.tag.alarm_config.area.center.coordinates = this.tag.current_position.position.coordinates;
      }
    },
    deleteTag: function (event) {
      var restClient = new RESTClient();
      restClient.remove(this.tag, function(){
        for (var i = 0; i < this.tags.length; i++) {
          if (this.tag === this.tags[i]) {
            this.tags.splice(i,1);
            this.toggle();
          }
        }
      }.bind(this));
    },
    save: function (event) {
      var restClient = new RESTClient();
      restClient.update(this.tag);
    },
  },
  watch: {
    'triggerModal': function (value, oldValue) {
      this.toggle();
    },
    // whenever question changes, this function will run
    'tag': function (value, oldValue) {
    },
    'tag.name': function (value, oldValue) { this.save();
    },
    'tag.alarm_config.area.center.coordinates': function(value, oldValue){
      var restClient = new RESTClient();
      restClient.update(this.tag.alarm_config.area,
        function(newArea){
          //this.tag.alarm_config.area = newArea;
        },
        function(error){
          this.tag.alarm_config.area.center.coordinates = oldValue;
        }.bind(this));
    },
    'tag.alarm_config.area.radius': function(value, oldValue){
      var restClient = new RESTClient();
      restClient.update(this.tag.alarm_config.area,
        function(newArea){
          //this.tag.alarm_config.area = newArea;
        },
        function(error){
          this.tag.alarm_config.area.center.radius = oldValue;
        }.bind(this));
    },
  },
  computed: {

    modalVisibilityStyle: function(){
      if (this.visible){
        return "display: inline";
      } else {
        return "display: none";
      }
    },
  },
};

export default TagModal;

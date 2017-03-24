import * as Vue2Leaflet from 'vue2-leaflet';
import TagMarker  from './../tag_marker.vue';
import AlarmConfigArea  from './../alarm_config_area.vue';

var TagDetailMap = {
  props: {
    tag: Object,
    posMes: Array,
  },
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-poly': Vue2Leaflet.Polyline,
    'v-marker': Vue2Leaflet.Marker,
    'v-circle': Vue2Leaflet.LCircle,
    'v-alarm-config-area': AlarmConfigArea,
  },
  data: function(){
    return {
      zoom:11,
      center:[47.413220, 8.519482],
      circleCenter: L.latLng(47.413220, 8.519482),
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
    };
  },
  computed: {
    area: function() {
      if(this.tag.alarm_config && this.tag.alarm_config.area){
        return this.tag.alarm_config.area;
      }
      return null;
    },
    areaCenter: function() {
      if(this.tag.alarm_config && this.tag.alarm_config.area){
        return {
          lat: this.tag.alarm_config.area.center.coordinates[0],
          lng: this.tag.alarm_config.area.center.coordinates[1],
        };
      }
      return {};
    },
    currentPosition: function(){
      if (this.posMes && this.posMes.length > 0){
        return this.posMes[0].coordinates;
      }
      return false;
    },
    positions: function(){
      var coords = [];
      if (this.posMes){
        for (var i = 0; i < this.posMes.length; i++) {
          coords.push(this.posMes[i].coordinates); }
      }
      return coords;
    },
  },
};

export default TagDetailMap;
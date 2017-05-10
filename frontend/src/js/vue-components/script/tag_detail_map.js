import * as Vue2Leaflet from 'vue2-leaflet';
import TagMarker  from './../tag_marker.vue';
import AlarmConfigArea  from './../alarm_config_area.vue';
import Settings from './../../settings.js';

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
    'v-geojson': Vue2Leaflet.GeoJSON,
  },
  data: function(){
    return {
      zoom:11,
      url: Settings.TILE_SET_URL,
      options: {
        style: function () {
          return {
            weight: 2,
            fillOpacity: 0.3
          };
        }
      },
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
          lng: this.tag.alarm_config.area.center.coordinates[0],
          lat: this.tag.alarm_config.area.center.coordinates[1],
        };
      }
      return {};
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

import * as Vue from 'vue';
import * as Vue2Leaflet from 'vue2-leaflet';
import TagMarker  from './../tag_marker.vue';


var TagOverviewMap = {
  props: {
    tags: {
      type: Array,
      default: function(){return [];},
    },
    sharedTags: {
      type: Array,
      default: function(){return [];},
    },
  },
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
    'v-circle': Vue2Leaflet.LCircle,
  },
  data: function(){
    return {
      zoom:11,
      circleCenter: L.latLng(47.413220, 8.519482),
      circleRadius: 200,
      url:'https://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    };
  },
  methods: {
    hovered: function(par){
      if(par.hover){
        return par.hover;
      }
    }
  },
  computed: {
    center: function() {
      for (var i = 0; i < this.tags.length; i++) {
        var tag = this.tags[i];
        if(tag.current_position){
          return tag.current_position.coordinates;
        }
      }
      return [47.413220, 8.519482];
    },
    icon: function() {
      return L.icon({
        iconUrl: '/static/img/icons/marker.svg',
        shadowUrl: '',
        iconSize: [40, 35],
        iconAnchor: [20, 17],
      });
    },
    iconOrange: function() {
      return L.icon({
        iconUrl: '/static/img/icons/marker--orange.svg',
        shadowUrl: '',
        iconSize: [40, 35],
        iconAnchor: [20, 17],
      });
    },
  }
};
export default TagOverviewMap;

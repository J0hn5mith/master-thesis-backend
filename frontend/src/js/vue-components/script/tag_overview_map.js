import * as Vue from 'vue';
import * as Vue2Leaflet from 'vue2-leaflet';
import StaticFile from '../../filters/static_file.js';
import Settings from  '../../settings.js';


var TagOverviewMap = {
  props: {
    userData: {
      type: Object,
      required: true,
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
      url: Settings.TILE_SET_URL,
      attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    };
  },
  methods: {
    hovered: function(par){
      if(par.hover){
        return par.hover;
      }
    },
    getTagIcon: function(tag, shared) {
      var url;
      if (tag.avatar){
          url =  tag.avatar;
      } else if (!shared){
        url = StaticFile('/img/icons/marker.svg');
      } else {
        url = StaticFile('/img/icons/marker--orange.svg');
      }

      return L.icon({
        iconUrl: url,
        shadowUrl: '',
        iconSize: [40, 35],
        iconAnchor: [20, 17],
      });
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
    tags: function(){
      return this.userData.tags;
    },
    sharedTags: function(){
      var sharedTags = [];
      for(var i in this.userData.sharedTags){
        sharedTags.push(this.userData.sharedTags[i].tag);
      }
      return sharedTags;
    },
    icon: function(data) {
      console.log(data);
      return L.icon({
        iconUrl: '/static/img/icons/marker.svg',
        shadowUrl: '',
        iconSize: [40, 35],
        iconAnchor: [20, 17],
      });
    },
    iconOrange: function(data) {
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

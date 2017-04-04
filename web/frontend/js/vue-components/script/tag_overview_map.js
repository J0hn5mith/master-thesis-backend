import * as Vue from 'vue';
import * as Vue2Leaflet from 'vue2-leaflet';
import TagMarker  from './../tag_marker.vue';
import RESTClient from './../../src/RESTClient.js';


var TagOverviewMap = {
  props: {
    //tags: Array
  },
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
  },
  data: function(){
    return {
      zoom:11,
      circleCenter: L.latLng(47.413220, 8.519482),
      circleRadius: 200,
      url:'https://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      tags: []
    };
  },
  beforeCreate: function(){
    var instance = this;
    var restClient = new RESTClient();
    restClient.getTags(
      function (results) { instance.tags = results;},
      function (error) { console.log(error);}
    );
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
  }
};


export default TagOverviewMap;

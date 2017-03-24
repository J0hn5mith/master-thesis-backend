import * as Vue from 'vue'
import * as Vue2Leaflet from 'vue2-leaflet'
import TagMarker  from './../tag_marker.vue'
import RESTClient from './../../src/RESTClient.js'


var TagOverviewMap = {
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
  },
  data: function(){
    return {
      zoom:11,
      center:[47.413220, 8.519482],
      circleCenter: L.latLng(47.413220, 8.519482),
      circleRadius: 200,
      url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      tags: []
    }
  },
  beforeCreate: function(){
    var instance = this;
    var restClient = new RESTClient();
    restClient.getTags(
      function (results) { instance.tags = results;},
      function (error) { console.log(error);}
    );
  },
}


export default TagOverviewMap
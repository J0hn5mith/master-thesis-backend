import * as Vue2Leaflet from 'vue2-leaflet'
import RESTClient from './../../src/RESTClient.js'

var TagDetailMap = {
  template: '#tag-detail-map',
  props: ['tag'],
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-poly': Vue2Leaflet.Polyline,
  },
  data: function(){
    return {
      zoom:11,
      center:[47.413220, 8.519482],
      circleCenter: L.latLng(47.413220, 8.519482),
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      positions: [],
    }
  },
  created: function(){
    var instance = this;

    var restClient = new RESTClient();
    restClient.getTagData(instance.tag.uid).then(function (response) {
      instance.measurements = response.data.results;
      var coords = [];
      for (var i = 0; i < instance.measurements.length; i++){
        coords.push(instance.measurements[i].coordinates);
      }
      instance.positions = coords;
    }).catch(function (error) {
      console.log(error);
    });
  },
}

export default TagDetailMap

import * as Vue from 'vue'
import * as Vue2Leaflet from 'vue2-leaflet'
import DataSource from '../DataSource.js'

var TagDetailMap = {
  template: '#tag-detail-map',
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
  beforeCreate: function(){
    var instance = this;
    var dataSource = new DataSource();
    dataSource.getTagData(1).then(function (response) {
      instance.measurements = response.data.results;
      console.log(instance.measurements);

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

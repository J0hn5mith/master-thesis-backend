import * as Vue2Leaflet from 'vue2-leaflet'

var TagDetailMap = {
  props: {
    tag: Object,
    posMes: Array,
  },
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
    }
  },
  computed: {
    positions: function(){
      var coords = [];
      if (this.posMes){
        for (var i = 0; i < this.posMes.length; i++){
          coords.push(this.posMes[i].coordinates);
        }
      }
      return coords;
    },
  },
}

export default TagDetailMap

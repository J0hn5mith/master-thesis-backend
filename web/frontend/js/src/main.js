import app1 from './components/TagList.js'
//import './components/map.js'
import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import * as Vue2Leaflet from 'vue2-leaflet' // Required for using with external templates

//Vue.component('v-map', Vue2Leaflet.Map);
//Vue.component('v-tilelayer', Vue2Leaflet.TileLayer);

var map = new Vue({
  el: '#map',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer' :Vue2Leaflet.TileLayer,
    'v-circle': Vue2Leaflet.LCircle,
    'v-marker': Vue2Leaflet.Marker,
  },
  created: function(){
  },
  methods: {
    sayHello: function(event) {
      var distance = event.latlng.lng - event.oldLatLng.lng;
      console.log(this.circleRadius);
      this.circleRadius += this.zoom * distance;
      console.log(this.circleRadius);
    },
  },
  data () {
    return {
      zoom:13,
      center:[47.413220, 8.519482],
      circleCenter: L.latLng(47.413220, 8.519482),
      circleRadius: 200,
      url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }
  }
})

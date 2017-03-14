import * as Vue2Leaflet from 'vue2-leaflet'

var AlarmConfigArea = {
  props: {
    area: Object,
  },
  components: {
    'v-circle': Vue2Leaflet.LCircle,
  },
  data: function(){
    return {hello: 'world'}
  },
  methods: {
    deferredMountedTo(parent) {
    },
  }
}
export default AlarmConfigArea;

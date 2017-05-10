import * as Vue2Leaflet from 'vue2-leaflet'

var TagMarker = {
  template: '#tag-marker',
  components: {
    'v-circle': Vue2Leaflet.LCircle,
  },
  data () {
    return {
    }
  }
}

export default TagMarker

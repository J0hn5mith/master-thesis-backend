import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import * as Vue2Leaflet from 'vue2-leaflet'

var TagMarker = {
  template: '#tag-marker',
  components: {
    'v-circle': Vue2Leaflet.LCircle,
  },
  data () {
    return {
      hello: "world"
    }
  }
}

export default TagMarker

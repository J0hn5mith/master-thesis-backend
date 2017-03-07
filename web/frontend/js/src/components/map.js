import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import * as Vue2Leaflet from 'vue2-leaflet' // Required for using with external templates
import axios from 'axios'

var TagOverviewMap = {
    template: '#tag-overview-map',
    components: {
        'v-map': Vue2Leaflet.Map,
        'v-tilelayer' :Vue2Leaflet.TileLayer,
        'v-circle': Vue2Leaflet.LCircle,
        'v-marker': Vue2Leaflet.Marker,
    },
    data: function(){
        return {
            zoom:13,
            center:[47.413220, 8.519482],
            circleCenter: L.latLng(47.413220, 8.519482),
            circleRadius: 200,
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            tags: [
                //{
                    //uid: '1',
                    //coordinates: {lat: 47.42322, lng: 8.519482,},
                    //trace: [],
                //}
            ]
        }
    },
    beforeCreate: function(){
        console.log(this.test);
        var instance = this;
        axios.get('/tags/rest/tags/', { })
            .then(function (response) {
                //console.log(response.data.results[0].current_position.geometry.coordinates)
                instance.tags = response.data.results
                console.log(instance.tags[0])
            })
            .catch(function (error) {
                console.log(error);
            });
    },
    methods: {
        sayHello: function(event) {
            var distance = event.latlng.lng - event.oldLatLng.lng;
            console.log(this.circleRadius);
            this.circleRadius += this.zoom * distance;
            console.log(this.circleRadius);
        },
    },
}

export default TagOverviewMap

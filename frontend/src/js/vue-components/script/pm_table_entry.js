import formater from './../../src/Formats.js';
import RESTClient from './../../src/RESTClient.js';

var PMTableEntry = {
  props: ['mes', 'l'],
  computed: {
    time_stamp : function(){
      return formater.date(this.mes.time_stamp);
    }
  },
  filters: {
    coordinates: function (coordinates) {
      return formater.coordinates(coordinates);
    }
  },
  methods: {
    deleteTag: function(){
      var restClient = new RESTClient();
      var instance = this;
      restClient.remove(this.mes, function(){
        for (var i = 0; i < instance.l.length; i++) {
          if (instance.mes === instance.l[i]) {
            instance.l.splice(i,1);
          }
        }
      });
    }
  }
};

export default PMTableEntry;

import RESTClient from './../../src/RESTClient.js';

var  ShareSettingsEntry = {
  props: {
    sharedTag: {
      type: Object,
      default: null,
    }
  },
  data:  function() {
    return {
      user: null,
    };
  },
  created: function(){
    if (!this.sharedTag){
      console.log('create prototype');
    }
  },
  methods: {
  }
};

export default ShareSettingsEntry;

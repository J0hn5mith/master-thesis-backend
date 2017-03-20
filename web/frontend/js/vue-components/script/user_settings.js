import RESTClient from './../../src/RESTClient.js'

var UserSettings = {
  props: ['user'],
  data: function(){
    return{
      emailDisabledInfo: "Set and activated a email address.",
      smsDisabledInfo: "Set and activated a mobile device.",
    }
  },
  mounted: function(){
  },
  watch: {
    'user.conf.notify_by_email': function(oldVal, newVal){
        var restClient = new RESTClient();
        restClient.update(this.user.conf);
    }
  }
}
export default UserSettings;

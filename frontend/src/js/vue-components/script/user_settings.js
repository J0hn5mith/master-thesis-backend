import RESTClient from './../../src/RESTClient.js';
import UserData from './../../src/UserData.js';

var UserSettings = {
  data: function(){
    return{
      userData: new UserData(),
      emailDisabledInfo: "Set and activated a email address.",
      smsDisabledInfo: "Set and activated a mobile device.",
    };
  },
  mounted: function(){
  },
  watch: {
    'userData.user.conf.notify_by_email': function(oldVal, newVal){
      var restClient = new RESTClient();
      restClient.update(this.userData.user.conf);
    },
    'userData.user.conf.notify_by_sms': function(oldVal, newVal){
      var restClient = new RESTClient();
      restClient.update(this.userData.user.conf);
    },
    'userData.user.username': function(oldVal, newVal){
      var restClient = new RESTClient();
      console.log(this.userData.user);
      restClient.update(this.userData.user);
    },
  }
};

export default UserSettings;

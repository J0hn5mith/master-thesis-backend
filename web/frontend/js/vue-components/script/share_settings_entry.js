import RESTClient from './../../src/RESTClient.js';
import vSelect from 'vue-select';

var  ShareSettingsEntry = {
  props: {
    userData: {
      type: Object,
      required: true
    },
    sharedTag: {
      type: Object,
      default: null,
    },
    sharedTags: {
      type: Array,
      required: true,
    }
  },
  components: {
    'v-select': vSelect,
  },
  data:  function() {
    return {
      user: null,
      userOptions: [],
    };
  },
  created: function(){
    if (!this.sharedTag.pk){
      var restClient = new RESTClient();
      restClient.getUsers(
        function (users) {
          var unavailableUrls = [];
          for(var i in this.sharedTags){
            var tag = this.sharedTags[i];
            if(tag.user){
              unavailableUrls.push(tag.user.url);
            }
          }
          unavailableUrls.push(this.userData.user.url);
          for (var i in users) {
            var user = users[i];
            if(unavailableUrls.indexOf(user.url)<0){
              this.userOptions.push({value: user.pk, label: user.username});
            }
          }
        }.bind(this),
        function (error) { console.log(error);}
      );
    }
  },
  watch: {
    sharedTag: function(newValue, oldValue){
      console.log(newValue);
    },
    'sharedTag.permissions': function(newValue, oldValue){
      var restClient = new RESTClient();
      restClient.update(this.sharedTag);
    },
  },
  computed: {
    permissionsValue: function(){
      return 'Read';
    },
    permissionsOptions: function(){
      return [
        {label: 'Read on Al', value: 0},
        {label: 'Read', value: 1},
        {label: 'Edit', value: 2},
        {label: 'Admin', value: 3},
      ];
    }
  },
  methods: {
    removeSharedTag: function(value){
      var restClient = new RESTClient();
      restClient.remove(
        this.sharedTag,
        function (success) {
          for (var i = 0; i < this.sharedTags.length; i++) {
            if (this.sharedTag === this.sharedTags[i]) {
              this.sharedTags.splice(i,1);
            }
          }
        }.bind(this),
        function (error) {console.log(error);}
      );
    },
    userSet: function(value){
      var restClient = new RESTClient();
      this.sharedTag.user_id = value.value;
      restClient.createSharedTag(
        this.sharedTag,
        function (sharedTag) {
          //TODO: very ugly! Find better solution
          this.sharedTag.pk = sharedTag.pk;
          this.sharedTag.user = sharedTag.user;
          this.sharedTag.tag = sharedTag.tag;
          this.sharedTag.permissions = sharedTag.permissions;
          this.sharedTag.url = sharedTag.url;
          delete this.sharedTag.user_id;
          delete this.sharedTag.tag_id;
        }.bind(this),
        function (error) { console.log(error);}
      );
    }
  }
};

export default ShareSettingsEntry;

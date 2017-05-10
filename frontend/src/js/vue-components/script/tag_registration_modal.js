import RESTClient from './../../src/RESTClient.js';

var TagRegistrationModal={
  props: {
    userData : {
      type: Object,
      required: true,
    }
  },
  data: function() {
    return {
      visible: false,
      urlSuffix: "new-tag/",
      tag: null,
      error: false,
    };
  },
  methods: {
    cancel: function(){
      this.setPrototype();
      this.toggle();
    },
    toggle: function(){
      this.visible = !this.visible;
      if (this.visible){
        var stateObj = {};
        window.history.pushState(stateObj, "Create new tag", this.urlSuffix + "/");
      } else {
        window.history.pushState({}, "", "./../");
      }
    },
    create: function(){
      this.userData.addNewTag(
        this.tag,
        function(newInstance){
          this.setPrototype();
          this.toggle();
        }.bind(this),
        function(error){
          console.log(error);
          this.error = true;
        }.bind(this)
      );
    },
    handleFileDrop: function(e){
      if (e.preventDefault) { e.preventDefault(); }
      var files = e.dataTransfer.files;
      for (var i=0; i<files.length; i++) {
        var file = files[i];
        this.updateImage(file);
      }
    },
    imageChangeHandler: function(e){
      this.updateImage(e.target.files[0]);
    },
    updateImage: function(file){
      var restClient = new RESTClient();

      restClient.uploadFile(file, function(url){
        this.tag.avatar = url;
      }.bind(this));

    },
    setPrototype: function(){
      this.tag = {
        name: "",
        uid: "",
        avatar: "",
      };
    },
  },
  created: function() {
    this.visible = window.location.pathname.endsWith(this.urlSuffix);
    this.setPrototype();
  },
  computed: {
    modalVisibilityStyle: function(){
      if (this.visible){
        return "display: inline";
      } else {
        return "display: none";
      }
    },
  },
};

export default TagRegistrationModal;

import RESTClient from './../../src/RESTClient.js';

var TagRegistrationModal={
  props: {
    tagList : {
      default: function(){return [];},
    }
  },
  data: function() {
    return {
      visible: false,
      urlSuffix: "new-tag",
      tag: null,
    };
  },
  methods: {
    create: function(){
      var restClient = new RESTClient();
      var instance = this;
      restClient.createTag(this.tag, function(newInstance){
        instance.tagList.push(newInstance);
        instance.tag = null;
        instance.toggle();
      }.bind(this));
    },
    toggle: function(){
      this.visible = !this.visible;
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
    }
  },
  created: function() {
    this.visible = window.location.pathname.endsWith(this.urlSuffix);
    var restClient = new RESTClient();
    restClient.getTagPrototype(function(result){
      this.tag = result;
    }.bind(this));
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

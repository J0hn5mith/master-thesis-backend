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
    cancel: function(){
        this.setPrototype();
        this.toggle();
    },
    toggle: function(){
      this.visible = !this.visible;
    },
    create: function(){
      var restClient = new RESTClient();
      var instance = this;
      restClient.createTag(this.tag, function(newInstance){
        instance.tagList.push(newInstance);
        this.setPrototype();
        this.toggle();
      }.bind(this));
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
      var restClient = new RESTClient();
      restClient.getTagPrototype(function(result){
        this.tag = result;
      }.bind(this));
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

import RESTClient from './RESTClient.js';

/**
 * A single interaction point for the data fetched from the webapp and the vue
 * components.
 */
class UserData {
  constructor(){
    this._tags = null;
    this._sharedTags = null;
    this._user = null;

    this._load_user();
    setInterval(this._updateTags.bind(this), 5000);
  }

  get user() {
    return this._user;
  }

  set user(value) {
    console.log('Invaclid action!');
  }

  get tags() {
    if(!this._tags){
      this._tags = [];
      this._load_tags();
    }
    return this._tags;
  }

  set tags(value) {
    console.log('Invaclid action!');
  }

  get sharedTags() {
    if(!this._sharedTags){
      this._sharedTags = [];
      this._load_shared_tags();
    }
    return this._sharedTags;
  }

  set sharedTags(value) {
    console.log('Invalid action!');
  }

  addNewTag(data, successHandler, errorHandler) {
    data.user = this._user.url;
    var restClient = new RESTClient();
    restClient.createTag(
      data,
      function(newTag){
        this._tags.push(newTag);
        successHandler(newTag);
      }.bind(this),
      errorHandler
    );
  }

  deleteTag(tag, successHandler, errorHandler) {
    var restClient = new RESTClient();
    restClient.remove(
      tag,
      function(result){
        for (var i = 0; i < this._tags.length; i++) {
          if (tag === this._tags[i]) {
            this._tags.splice(i,1);
          }
        }
        successHandler(result);
      }.bind(this),
      errorHandler
    );
  }

  _load_shared_tags(){
    var restClient = new RESTClient();
    restClient.getSharedTags(
      function (sharedTags) {
        for (var i = 0; i < sharedTags.length; i++) {
          sharedTags[i].tag.hover = false;
          var sharedTag = sharedTags[i];
          if(this.user.url !== sharedTag.tag.user){
            this._sharedTags.push(sharedTag);
          }
        }
      }.bind(this),
      function (error) { console.log(error);}
    );
  }

  _load_tags(){
    var restClient = new RESTClient();
    restClient.getTags(
      function (tags) {
        for (var i = 0; i < tags.length; i++) {
          this._tags.push(tags[i]);
        }
      }.bind(this),
      function (error) { console.log(error);}
    );
  }

  _updateTags(){
    if(!this._tags){
      return;
    }
    var restClient = new RESTClient();
    restClient.getTags(
      function (tags) {
        for (var i = 0; i < tags.length; i++) {
          var newVersion = tags[i];
          for (var ii = 0; ii < this._tags.length; ii++) {
            var oldVersion = this._tags[ii];
            if (newVersion.url === oldVersion.url){
              console.log(oldVersion);
              //todo check if tag actually has changed!
              oldVersion.current_position = newVersion.current_position;
            }
          }
        }
      }.bind(this),
      function (error) { console.log(error);}
    );
  }

  _load_user(){
    var restClient = new RESTClient();
    restClient.getCurrentUser(
      function(user){
        this._user = user;
      }.bind(this),
      null
    );
  }
}

export default UserData;

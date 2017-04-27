import axios from 'axios';
import Raven from 'raven-js';

var URL_CONFIG = {
  tags: '/tags/rest/tags/',
  sharedTags: '/tags/rest/shared_tags/',
  tagPrototype: '/tags/rest/prototype/',
  tagData: '/sensor-data/rest/position_measurements/',
  currentUser: '/user/rest/current-user/',
  users: '/user/rest/user/',
  fileUpload: '/utils/file-upload/',
};

class RESTClient {

  /**
   * Sends an delete request to the REST server.
   * @param{instance} Instance which has to be deleted.
   * @param{success} Success callback function.
   * @param{success} error callback function.
   */
  remove(instance, success, error_handler) {
    axios.delete(instance.url, {headers: {'X-CSRFToken': csrfToken}})
      .then(function (response) {if(success){success(response);}})
      .catch(function (error) {
        if(error_handler){
          error_handler(error);
        }
        Raven.captureException(error);
      });
  }

  update(instance, success, error_handler) {
    axios.put(instance.url, instance, {headers: {'X-CSRFToken': csrfToken}})
      .then(function (response) {
        if(success){success(response.data);}
      }.bind(success))
      .catch(function (error) {
        if(error_handler){
          error_handler(error);
        }
        Raven.captureException(error);
      });
  }

  get(url, success, error_handler) {
    axios.get(url, {})
      .then(function(response){
        if(success){
          var data = null;
          if(response.data.results){
            data = response.data.results;
          } else{
            data = response.data;
          }
          success(data);
        }
      })
      .catch(function (error) {
        if(error_handler){
          error_handler(error);
        }
        Raven.captureException(error);
      });
  }

  create(url, instance, success, error_handler) {
    axios.post(url, instance, {headers: {'X-CSRFToken': csrfToken}})
      .then(function(response){
        if(success){
          var newInstance  = response.data;
          success(newInstance);
        }
      }.bind(success)).catch(function (error) {
        if(error_handler){
          error_handler(error);
        }
        Raven.captureException(error);
      }.bind(error_handler));
  }

  getTags(success, error) {
    this.get(URL_CONFIG.tags, success, error);
  }

  getSharedTags(success, error) {
    this.get(URL_CONFIG.sharedTags, success, error);
  }

  getUsers(success, error) {
    this.get(URL_CONFIG.users, success, error);
  }

  getTagPrototype(success, error_handler) {
    axios.get(URL_CONFIG.tagPrototype)
      .then(function(response){
        if(success){
          success(response.data);
        }
      }).catch(function (error) {
        if(error_handler){
          error_handler(error);
        }
        Raven.captureException(error);
      });
  }

  createTag(instance, success, error_handler) {
    this.create(URL_CONFIG.tags, instance, success, error_handler);
  }

  createSharedTag(instance, success, error_handler) {
    this.create(URL_CONFIG.sharedTags, instance, success, error_handler);
  }

  getSensorData(id, success, error) {
    var url = URL_CONFIG.tagData + '?uid=' + id;
    this.get(url, success, error);
  }

  getCurrentUser(success, error) {
    this.get(URL_CONFIG.currentUser, success, error);
  }

  uploadFile(file, success, error_handler) {
    var formData = new FormData();
    formData.append('image', file);
    axios.post(URL_CONFIG.fileUpload, formData, {
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'multipart/form-data',
      },
    }).then(function(response){
      if(success){
        success(response.data.url);
      }
    }).catch(function (error) {
      if(error_handler){
        error_handler(error);
      }
      Raven.captureException(error);
    });
  }
}

export default RESTClient;

import axios from 'axios';

var URL_CONFIG = {
  tags: '/tags/rest/tags/',
  tagData: '/sensor-data/rest/position_measurements/',
  currentUser: '/user/rest/current-user/',
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
        } else { console.log(error); }
      });
  }

  update(instance, success, error_handler) {
    axios.put(instance.url, instance, {headers: {'X-CSRFToken': csrfToken}})
      .then(function (response) { if(success){success(response);}})
      .catch(function (error) {
        if(error_handler) {
          error_handler(error_handler);
        } else {
          console.log(error);
        }
      });
  }

  get(url, success, error) {
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
      .catch(function (e) {if(error){console.log(e.stack);}});
  }

  getTags(success, error) {
    this.get(URL_CONFIG.tags, success, error);
  }

  getSensorData(id) {
    return axios.get(URL_CONFIG.tagData + '?uid=' + id, { });
  }

  getCurrentUser(success, error) {
    this.get(URL_CONFIG.currentUser, success, error);
  }
}

export default RESTClient;

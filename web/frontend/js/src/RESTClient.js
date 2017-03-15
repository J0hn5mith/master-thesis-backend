import axios from 'axios'

var URL_CONFIG = {
  tags: '/tags/rest/tags/',
  tagData: '/sensor-data/rest/position_measurements/',
}

class RESTClient {

  /**
   * Sends an delete request to the REST server.
   * @param{instance} Instance which has to be deleted.
   * @param{success} Success callback function.
   * @param{success} error callback function.
   */
  remove(instance, success, error) {
    axios.delete(instance.url, {headers: {"X-CSRFToken": csrfToken}})
      .then(function (response) { if(success){success(response)}})
      .catch(function (error) {
        if(error){ console.log(error); }
      });
  }

  update(instance, success, error) {
    axios.put(instance.url, instance, {headers: {"X-CSRFToken": csrfToken}})
      .then(function (response) { if(success){success(response)}})
      .catch(function (error) {
        if(error){
          console.log(error);
        }
      });
  }

  get(url, success, error) {
    axios.get(url, {})
      .then(function(response){
        if(success){
          var data = response.data.results;
          success(data);
        }
      })
      .catch(function (e) {if(error){console.log(e.stack);}});
  }

  getTags(success, error) {
    this.get(URL_CONFIG.tags, success, error)
  }

  getSensorData(id) {
    return axios.get( URL_CONFIG.tagData + '?uid=' + id, { })
  }
}

export default RESTClient;

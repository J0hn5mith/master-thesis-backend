import axios from 'axios'

var URL_CONFIG = {
  tags: '/tags/rest/tags/',
  tagData: '/sensor-data/rest/position_measurements/',
}

class RESTClient {

  getTags() {
    return axios.get(URL_CONFIG.tags, { })
  }

  updateTag(tag) {
    console.log(csrfToken);
    return axios.put(URL_CONFIG.tags+ tag.pk + '/', tag, {headers: {"X-CSRFToken": csrfToken}})
  }

  getTagData(id) {
    return axios.get( URL_CONFIG.tagData + '?uid=' + id, { })
  }

  deletePositionMeasurement(pk) {
    return axios.delete(URL_CONFIG.tagData + pk, {headers: {"X-CSRFToken": csrfToken}})
  }
}

export default RESTClient;

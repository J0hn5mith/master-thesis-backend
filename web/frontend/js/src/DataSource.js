import axios from 'axios'

class DataSource {

  getTags() {
    return axios.get('/tags/rest/tags/', { })
  }

  getTagData(id) {
    var url = '/sensor-data/rest/position_measurements/?uid=' + id;
    console.log(url);
    return axios.get( url, { })
  }
}

export default DataSource;

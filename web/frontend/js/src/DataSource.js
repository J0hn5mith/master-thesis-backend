import axios from 'axios'

class DataSource {

  getTags() {
    return axios.get('/tags/rest/tags/', { })
  }

  getTagData(id) {
    return axios.get('/sensor-data/rest/position_measurements/', { })
  }
}

export default DataSource;

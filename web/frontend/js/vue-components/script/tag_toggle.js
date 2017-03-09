import axios from 'axios'

var TagToggle = {
  props: ['tag'],
  methods: {
    toggle: function (event) {
      this.tag.active = !this.tag.active;
      axios.put('/tags/rest/tags/' + this.tag.pk + '/', this.tag, {headers: {"X-CSRFToken": csrfToken}})
        .then(function (response) {
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
}
export default TagToggle

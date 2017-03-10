import RESTClient from './../../src/RESTClient.js'

var TagToggle = {
  props: ['tag'],
  methods: {
    toggle: function (event) {
      this.tag.active = !this.tag.active;
      var restClient = new RESTClient();
      restClient.updateTag(this.tag).then(function(response){})
        .catch(function (error) {
          console.log(error);
        });
    },
  },
}
export default TagToggle

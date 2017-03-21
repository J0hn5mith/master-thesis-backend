import RESTClient from './../../src/RESTClient.js'

var TagToggle = {
  props: ['tag'],
  methods: {
    toggle: function (event) {
      this.tag.active = !this.tag.active;
      var restClient = new RESTClient();
      restClient.update(this.tag, null, function(){
      this.tag.active = !this.tag.active;
      });
    },
  },
}
export default TagToggle

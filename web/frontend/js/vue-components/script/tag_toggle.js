import RESTClient from './../../src/RESTClient.js';

var TagToggle = {
  props: {
    'tag': {
      type: Object,
      required: true
    },
    'disabled': {
      type: Boolean,
      default: false,
    }
  },
  methods: {
    toggle: function (event) {
      this.tag.active = !this.tag.active;
      var restClient = new RESTClient();
      restClient.update(this.tag, null, function(){
        this.tag.active = !this.tag.active;
      }.bind(this));
    },
  },
};

export default TagToggle;

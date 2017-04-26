
var ShareTagButton = {
  props: {
    sharedTags: {
      type: Array,
      default: function(){return [];},
    }
  },
  data: function() {
    return {
      expanded: false,
    };
  },
  methods: {
    toggle: function(){
        this.sharedTags.push({pk: null});
    }
  },
};
export default ShareTagButton;

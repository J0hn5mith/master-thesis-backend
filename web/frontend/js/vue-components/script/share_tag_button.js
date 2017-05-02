
var ShareTagButton = {
  props: {
    tag: {
      type: Object,
      required: true,
    },
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
      //add pk so it can be watched by vue component
        this.sharedTags.push({pk: null, tag_id: this.tag.pk, permissions: 0});
    }
  },
};
export default ShareTagButton;

var CollapseSection = {
  data: function(){
    return{
      collapsed: true,
    }
  },
  methods: {
    toggle: function() {
      this.collapsed = !this.collapsed;
    }
  }
}

export default CollapseSection;

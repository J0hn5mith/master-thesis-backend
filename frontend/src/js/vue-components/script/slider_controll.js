import range from 'lodash/range';

var SliderControll = {
  props:{
    min: {
      type: Number,
      default: 0,
    },
    max: {
      type: Number,
      default: 100,
    },
    step: {
      type: Number,
      default: 5,
    },
    area: {
      type: Object,
      required: true,
    },
    tick_interval: {
      type: Number,
      default: 5,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    ticks: function() {
      return range((this.max-this.min)/this.tick_interval+1);
    },
    labels: function() {
      var labels = [];
      range((this.max-this.min)/this.tick_interval+1).forEach(function(item, index, array){
        if (item%5 === 0){
          labels.push((index) * this.tick_interval);
        }
      }.bind(this));
      return labels;
    },
  },
};

export default SliderControll;

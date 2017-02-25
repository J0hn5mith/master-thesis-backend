import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import axios from 'axios'

Vue.component('tag-charge-bar', {
  props: ['tag'],
  template: '#tag-charge-bar',
});

Vue.component('tag-toggle', {
  props: ['tag'],
  template: '#tag-toggle',
  methods: {
    toggle: function (event) {
      this.tag.active = !this.tag.active;
      console.log(this.tag);
      axios.put('/tags/rest/tags/' + this.tag.pk + '/', this.tag, {headers: {"X-CSRFToken": csrfToken}})
        .then(function (response) {
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
});

Vue.component('tag-list-item', {
  props: ['tag'],
  template: '#tag-list-item',
  data: function(){
    return{
      showModal: false,
    }
  },
  methods: {
    toggleModal: function (event) {
      this.showModal = true; //TODO:
    },
  }
});


//https://vuejs.org/v2/examples/modal.html
Vue.component('tag-modal', {
  props: ['tag'],
  template: '#tag-modal',
  created: function(){
  },
  data: function(){
    return{
      edited: false,
    }
  },
  methods: {
    save: function (event) {
      axios.put('/tags/rest/tags/' + this.tag.pk + '/', this.tag, {headers: {"X-CSRFToken": csrfToken}})
        .then(function (response) {
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  watch: {
    // whenever question changes, this function will run
    'tag': function (value, oldValue) {
      console.log(value);
    },
    'tag.name': function (value, oldValue) {
      this.edited = true;
    }
  },
});

var tagList = new Vue({
  el: '#tag-list',
  data: {
    tags: [],// Are set when mounted via AJAX
  },
  created: function(){
    var instance = this;
    axios.get('/tags/rest/tags', { })
      .then(function (response) {
        instance.tags = response.data.results;
      })
      .catch(function (error) {
        console.log(error);
      });
  }
})

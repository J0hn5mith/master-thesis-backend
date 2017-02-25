import app1 from './components/TagList.js'
import * as Vue from 'vue/dist/vue.common.js' // Required for using with external templates
import axios from 'axios'


Vue.component('tag-list-item', {
  props: ['tag'],
  template: '\
    <tr class="table__row">\
    <td class="table__cell">\
    <img v-if="tag.avatar" class="table__icon table__icon--hexagon" :src="tag.avatar"></img>\
    <img v-else class="table__icon" src="/static/img/icons/tag.svg"></img>\
    </td>\
    <td class="table__cell">\
    <p class="table__cell-text">\
  {{ tag.name }}\
    </p>\
    </td>\
    <td class="table__cell">\
    <p class="table__cell-text">{{ tag.get_status }}</p>\
    </td>\
    <td class="table__cell">\
    <p v-if="tag.last_update" class="table__cell-text table__cell-text--small">\
  {{ tag.last_update }}\
    </p>\
    <p v-else class="table__cell-text table__cell-text--small">\
  Unknown\
    </p>\
    </td>\
    <td class="table__cell">\
    <div v-if="tag.charge_status" >\
        <span class="hint--top" :aria-label="\'Charge level: \' + tag.charge_status + \'%\'">\
    <div class="progress">\
    <div class="progress-bar progress-bar-info" role="progressbar" v-bind:style="\'width:\' + tag.charge_status + \'%\'"></div>\
    <div class="progress-bar progress-bar-danger" role="progressbar" v-bind:style="\'width:\' + (100 - tag.charge_status) + \'%\'"></div>\
    </div>\
    <span>\
    </div>\
    <div v-else>\
        <span class="hint--top" :aria-label="\'Charge level: Unknown\'">\
    <div class="progress">\
    <div class="progress-bar progress-bar-info" role="progressbar" v-bind:style="\'width:\' + tag.charge_status + \'%\'"></div>\
    <div class="progress-bar progress-bar-disabled" role="progressbar" style="width:100%"></div>\
    </div>\
    </div>\
    </div>\
    </p>\
    </td>\
  \
    <td class="table__cell">\
    <a v-if="tag.active" class="btn btn-success" v-on:click="toggle">On</a>\
    <a v-else type="button" class="btn btn-outline btn-outline-danger" v-on:click="toggle">Off</a>\
    </td>\
  \
    </tr>\
  ',
  methods: {
    toggle: function (event) {
      this.tag.active = !this.tag.active;
      axios.put('/tags/rest/tags/' + this.tag.pk + '/', this.tag, {headers: {"X-CSRFToken": csrfToken}})
        .then(function (response) {
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }
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
        console.log(instance.tags);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
})

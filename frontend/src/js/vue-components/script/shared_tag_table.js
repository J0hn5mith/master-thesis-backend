import SharedTagTableEntry from '../shared_tag_table_entry.vue';
import TagRegistrationModal from '../tag_registration_modal.vue';

var props = {
  userData: {
    type: Object,
    required: true,
  }
};

var SharedTagTable = {
  components: {
    'v-shared-tag-table-entry': SharedTagTableEntry,
    'v-tag-registration-modal': TagRegistrationModal,
  },
  props: props,
  created: function(){
  },
  computed: {
    tags: function(){
      return this.userData.sharedTags;
    },
    hasTags: function(){
      return this.userData.sharedTags.length > 0;
    }
  }
};
export default SharedTagTable;

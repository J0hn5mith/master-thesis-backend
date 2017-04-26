import SharedTagTableEntry from '../shared_tag_table_entry.vue';
import TagRegistrationModal from '../tag_registration_modal.vue';


var SharedTagTable = {
  components: {
    'v-shared-tag-table-entry': SharedTagTableEntry,
    'v-tag-registration-modal': TagRegistrationModal,
  },
  props: {
      tags: {
        type: Array,
        defaul: [],
      }
  },
  created: function(){
  },
  computed: {
    hasTags: function(){
      return this.tags.length > 0;
    }
  }
};
export default SharedTagTable;

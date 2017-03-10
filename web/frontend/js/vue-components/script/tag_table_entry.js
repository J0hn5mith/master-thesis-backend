import TagChargeBar from '../tag_charge_bar.vue'
import TagToggle from '../tag_toggle.vue'
import TagModal from '../tag_modal.vue'

var TagTableEntry = {
    props: ['tag'],
    components: {
        'v-tag-charge-bar': TagChargeBar,
        'v-tag-toggle': TagToggle,
        'v-tag-modal': TagModal,
    },
    data: function(){
        return{
            showModal: false,
        }
    },
    methods: {
        toggleModal: function (event) {
            this.showModal = !this.showModal; //TODO:
        },
    }
}

export default TagTableEntry;

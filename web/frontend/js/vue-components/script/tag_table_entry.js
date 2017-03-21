import TagChargeBar from '../tag_charge_bar.vue'
import TagToggle from '../tag_toggle.vue'
import TagModal from '../tag_modal.vue'
import formater from './../../src/Formats.js'

var TagTableEntry = {
    props: ['tag'],
    components: {
        'v-tag-charge-bar': TagChargeBar,
        'v-tag-toggle': TagToggle,
        'v-tag-modal': TagModal,
    },
    filters: {
        date: function (date) {
            return formater.date(date);
        },
    },
    data: function(){
        return{
            showModal: false,
        }
    },
    computed: {
        alertStatusHint: function(){
            if(this.tag.alarm){
                return "Alert triggered at {0}".format(
                    formater.date(this.tag.alarm.start_time)
                );
            } else {
                return "No alert";
            }
        }
    },
    methods: {
        toggleModal: function (event) {
            this.showModal = !this.showModal; //TODO:
        },
    }
}

export default TagTableEntry;

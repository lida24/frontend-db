<template>
    <div class="wrap">
        <h4 class="h3 mb-3 font-weight-normal main-title">
            Этапы сборки
        </h4>
        <h5 class="h4 mb-3 font-weight-normal step-title">0 этап</h5>
        <div class="rectangle" :style="computedStyleCables">
            <div class="title">
                Монтаж кабелей/кабельных сборок/стяжек/метизов
            </div>
            <span class="is-disabled">
                <button @click="add_cables()" class="btn btn-primary add-server" :disabled="computedConditionCables">
                    Добавить
                </button>
            </span>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">1 этап</h5>
        <div class="rectangle" :style="computedStyleFans140">
            <div class="title">
                Монтаж 3 верхних вентиляторов в корпус
            </div>
            <span class="is-disabled">
                <button @click="add_fans_140()" class="btn btn-primary add-server" :disabled="computedConditionFans140">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleFanControlBoard">
            <div class="title">
                Монтаж платы управления вентиляторами
            </div>
            <span class="is-disabled">
                <button @click="add_fan_control_board()" class="btn btn-primary add-server" :disabled="computedConditionFanControlBoard">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleCablesFCB">
            <div class="title">
                Подключение кабелей в плату управления вентиляторами
            </div>
            <span class="is-disabled">
                <button @click="add_cables_fcb()" class="btn btn-primary add-server" :disabled="computedConditionCablesFCB">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleFans40">
            <div class="title">
                Монтаж 6 нижних вентиляторов в корпус
            </div>
            <span class="is-disabled">
                <button @click="add_fans_40()" class="btn btn-primary add-server" :disabled="computedConditionFans40">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleIndicatorBoard">
            <div class="title">
                Монтаж платы индикации
            </div>
            <span class="is-disabled">
                <button @click="add_indicator_board()" class="btn btn-primary add-server" :disabled="computedConditionIndicatorBoard">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStylePowerManagementModule">
            <div class="title">
                Монтаж платы управления питанием
            </div>
            <span class="is-disabled">
                <button @click="add_power_management_module()" class="btn btn-primary add-server" :disabled="computedConditionPowerManagementModule">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleCablesPMM">
            <div class="title">
                Подключение кабелей в плату управления питанием
            </div>
            <span class="is-disabled">
                <button @click="add_cables_pmm()" class="btn btn-primary add-server" :disabled="computedConditionCablesPMM">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleMemoryAndSSD">
            <div class="title">
                Монтаж модулей памяти и SSD диска в материнскую плату
            </div>
            <span class="is-disabled">
                <button @click="add_memory_and_ssd()" class="btn btn-primary add-server" :disabled="computedConditionMemoryAndSSD">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleNetworkCard">
            <div class="title">
                Монтаж сетевой карты в плату «Райзер-2U» и платы «Райзер-2U» в материнскую плату
            </div>
            <span class="is-disabled">
                <button @click="add_network_card()" class="btn btn-primary add-server" :disabled="computedConditionNetworkCard">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleRaiser2UBoard">
            <div class="title">
                Установка батарейки в плату «Райзер-2U»
            </div>
            <span class="is-disabled">
                <button @click="add_raiser_2U_board()" class="btn btn-primary add-server" :disabled="computedConditionRaiser2UBoard">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж материнской платы в корпус
            </div>
            <span class="is-disabled">
                <button class="btn btn-primary add-server">
                    <router-link :to="{ name: 'AddMotherBoard', params: { id: this.id }}">Добавить</router-link>
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleRaidCard">
            <div class="title">
                Монтаж RAID-контроллера в плату «Райзер-1U» и платы «Райзер-1U» в материнскую плату
            </div>
            <span class="is-disabled">
                <button @click="add_raid_card()" class="btn btn-primary add-server" :disabled="computedConditionRaidCard">
                    Добавить
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleCablesMB">
            <div class="title">
                Подключение всех кабелей в материнскую плату и карты расширения
            </div>
            <span class="is-disabled">
                <button @click="add_cables_mb()" class="btn btn-primary add-server" :disabled="computedConditionCablesMB">
                    Добавить
                </button>
            </span>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">2 этап</h5>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 4 (над материнской платой)
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddDiskBasket', params: { id: n, count: 4 }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 3
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddDiskBasket', params: { id: n, count: 3 }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 2
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddDiskBasket', params: { id: n, count: 2 }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 1
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddDiskBasket', params: { id: n, count: 1 }}">Добавить</router-link>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">3 этап</h5>
        <div class="rectangle">
            <div class="title">
                Установка блоков питания 2.6 кВт в соответствующие отсеки
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddPowerSupply2K6', params: { id: n }}">Добавить</router-link>
        </div>
    </div>
</template>

<style>
    .main-title {
      margin-top: 1rem !important;
      font-weight: 600 !important;
    }
    .step-title {
        text-align: start;
        margin-left: 10px;
        font-size: 24px !important;
        font-weight: 600 !important;
        margin-bottom: 0 !important;
    }
    .rectangle {
        padding: 6px 9px 6px 9px;
        width: inherit;
        height: 100px;
        margin: 40px 10px;
        /* background-color: #22ed4ef2; */
        /* background-color: #343a40; */
        display: flex;
        justify-content: space-between;
        box-sizing: border-box;
        align-items: center;
    }
    .title {
        display: inline-block;
        text-align: start;
        margin-left: 20px;
        font-size: 24px;
        font-weight: 600;
    }
    .add-server {
        display: inline-block;
        height: max-content;
        margin-right: 20px;
    }
    a[aria-disabled="true"] {
        color: #007bff;
        display: inline-block;
        pointer-events: none;
        text-decoration: none;
    }
</style>

<script>
   import axios from "axios";
    export default {
      data() {
        return {
          /* n: Number, */
          /* components: [], */
          indicator_board: '',
          fans_40: '',
          cables: '',
          fans_140: '',
          fan_control_board: '',
          power_management_module: '',
          cables_pmm: '',
          cables_fcb: '',
          memory_and_ssd: '',
          network_card: '',
          raiser_2U_board: '',
          raid_card: '',
          cables_mb: '',
        };
      },
      props: {
        id: {
            type: [Number, String],
            required: true,
        },
        success: {
            type: [Boolean],
            required: true,
        },
        order: {
            type: [Number, String],
            required: true,
        },
        stat: {
            type: [Number, String],
            required: true,
        },
      },
      methods: {
        add_indicator_board() {
        axios
          .post(`http://192.168.75.11:5000/app/add_indicator_board/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.indicator_board = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.indicator_board = response.data.indicator_board;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_fans_40() {
        axios
          .post(`http://192.168.75.11:5000/app/add_fan40/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fans_40 = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fans_40 = response.data.fans_40;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_cables() {
        axios
          .post(`http://192.168.75.11:5000/app/add_cables/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables = response.data.cables;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_fans_140() {
        axios
          .post(`http://192.168.75.11:5000/app/add_fan140/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fans_140 = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fans_140 = response.data.fans_140;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_fan_control_board() {
        axios
          .post(`http://192.168.75.11:5000/app/add_fan_control_board/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fan_control_board = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fan_control_board = response.data.fan_control_board;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_power_management_module() {
        axios
          .post(`http://192.168.75.11:5000/app/add_power_management_module/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.power_management_module = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.power_management_module = response.data.power_management_module;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_cables_pmm() {
        axios
          .post(`http://192.168.75.11:5000/app/add_cables_pmm/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_pmm = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_pmm = response.data.cables_pmm;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_cables_fcb() {
        axios
          .post(`http://192.168.75.11:5000/app/add_cables_fcb/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_fcb = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_fcb = response.data.cables_fcb;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_memory_and_ssd() {
        axios
          .post(`http://192.168.75.11:5000/app/add_memory_and_ssd/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.memory_and_ssd = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.memory_and_ssd = response.data.memory_and_ssd;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_network_card() {
        axios
          .post(`http://192.168.75.11:5000/app/add_network_card/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.network_card = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.network_card = response.data.network_card;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_raiser_2U_board() {
        axios
          .post(`http://192.168.75.11:5000/app/add_raiser_2U_board/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.raiser_2U_board = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.raiser_2U_board = response.data.raiser_2U_board;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_raid_card() {
        axios
          .post(`http://192.168.75.11:5000/app/add_raid_card/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.raid_card = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.raid_card = response.data.raid_card;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_cables_mb() {
        axios
          .post(`http://192.168.75.11:5000/app/add_cables_mb/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_mb = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_mb = response.data.cables_mb;
          })
          .catch((error) => {
            console.log(error);
          });
        },
      }, 
      created() {
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            this.indicator_board = response.data.indicator_board;
            this.fans_40 = response.data.fans_40;
            this.cables = response.data.cables;
            this.fans_140 = response.data.fans_140;
            this.fan_control_board = response.data.fan_control_board;
            this.power_management_module = response.data.power_management_module;
            this.cables_pmm = response.data.cables_pmm;
            this.cables_fcb = response.data.cables_fcb;
            this.memory_and_ssd = response.data.memory_and_ssd;
            this.network_card = response.data.network_card;
            this.raiser_2U_board = response.data.raiser_2U_board;
            this.raid_card = response.data.raid_card;
            this.cables_mb = response.data.cables_mb;
            console.log(response);
           /*  if (this.stat == 'установлен в изделие') {
                console.log("SUCCESS");
                
                let elem = document.getElementsByClassName("rectangle");
                elem[this.order].style.backgroundColor = "#22ed4ef2";
                console.log("ORDER: ", this.order);

                let span = document.getElementsByClassName("is-disabled");
                console.log(span);
                span[0].style.cursor = "not-allowed";
                span[1].style.cursor = "not-allowed";

                let btn = document.getElementsByClassName("add-server");
                btn[this.order].style.backgroundColor = "#636869";
                btn[this.order].style.borderColor = "#636869";
                btn[this.order].style.color = "#ffffff";
                btn[this.order].style.opacity = "1";
                btn[this.order].setAttribute('aria-disabled', true);
            } */
          })
          .catch((error) => {
            console.log(error);
          });
      },
      computed: {
        computedConditionIndicatorBoard() {
            if (this.indicator_board) {
                return true;
            }
            return false;
        },
        computedStyleIndicatorBoard() {
            if (this.indicator_board) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionFans40() {
            if (this.fans_40) {
                return true;
            }
            return false;
        },
        computedStyleFans40() {
            if (this.fans_40) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionCables() {
            if (this.cables) {
                return true;
            }
            return false;
        },
        computedStyleCables() {
            if (this.cables) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionFans140() {
            if (this.fans_140) {
                return true;
            }
            return false;
        },
        computedStyleFans140() {
            if (this.fans_140) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionFanControlBoard() {
            if (this.fan_control_board) {
                return true;
            }
            return false;
        },
        computedStyleFanControlBoard() {
            if (this.fan_control_board) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionPowerManagementModule() {
            if (this.power_management_module) {
                return true;
            }
            return false;
        },
        computedStylePowerManagementModule() {
            if (this.power_management_module) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionCablesPMM() {
            if (this.cables_pmm) {
                return true;
            }
            return false;
        },
        computedStyleCablesPMM() {
            if (this.cables_pmm) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionCablesFCB() {
            if (this.cables_fcb) {
                return true;
            }
            return false;
        },
        computedStyleCablesFCB() {
            if (this.cables_fcb) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionMemoryAndSSD() {
            if (this.memory_and_ssd) {
                return true;
            }
            return false;
        },
        computedStyleMemoryAndSSD() {
            if (this.memory_and_ssd) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionNetworkCard() {
            if (this.network_card) {
                return true;
            }
            return false;
        },
        computedStyleNetworkCard() {
            if (this.network_card) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionRaiser2UBoard() {
            if (this.raiser_2U_board) {
                return true;
            }
            return false;
        },
        computedStyleRaiser2UBoard() {
            if (this.raiser_2U_board) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionRaidCard() {
            if (this.raid_card) {
                return true;
            }
            return false;
        },
        computedStyleRaidCard() {
            if (this.raid_card) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        computedConditionCablesMB() {
            if (this.cables_mb) {
                return true;
            }
            return false;
        },
        computedStyleCablesMB() {
            if (this.cables_mb) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
      },
    };
</script>
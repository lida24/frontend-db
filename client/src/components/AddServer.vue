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
                <button v-if="!this.cables" @click="add_cables()" class="btn btn-primary add-server" :disabled="computedConditionCables" :style="StyleCables">
                    Добавить
                </button>
                <button v-else @click="add_cables()" class="btn btn-primary add-server" :disabled="computedConditionCables" :style="StyleCables">
                    Выполнено
                </button>
            </span>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">1 этап</h5>
        <div class="rectangle" :style="computedStyleFans140">
            <div class="title">
                Монтаж 3 верхних вентиляторов в корпус
            </div>
            <span class="is-disabled">
                <button v-if="!this.fans_140" @click="add_fans_140()" class="btn btn-primary add-server" :disabled="computedConditionFans140" :style="StyleFans140">
                    Добавить
                </button>
                <button v-else @click="add_fans_140()" class="btn btn-primary add-server" :disabled="computedConditionFans140" :style="StyleFans140">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleFanControlBoard">
            <div class="title">
                Монтаж платы управления вентиляторами
            </div>
            <span class="is-disabled">
                <button v-if="!this.fan_control_board" @click="add_fan_control_board()" class="btn btn-primary add-server" :disabled="computedConditionFanControlBoard" :style="StyleFanControlBoard">
                    Добавить
                </button>
                <button v-else @click="add_fan_control_board()" class="btn btn-primary add-server" :disabled="computedConditionFanControlBoard" :style="StyleFanControlBoard">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleCablesFCB">
            <div class="title">
                Подключение кабелей в плату управления вентиляторами
            </div>
            <span class="is-disabled">
                <button v-if="!this.cables_fcb" @click="add_cables_fcb()" class="btn btn-primary add-server" :disabled="computedConditionCablesFCB" :style="StyleCablesFCB">
                    Добавить
                </button>
                <button v-else @click="add_cables_fcb()" class="btn btn-primary add-server" :disabled="computedConditionCablesFCB" :style="StyleCablesFCB">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleFans40">
            <div class="title">
                Монтаж 6 нижних вентиляторов в корпус
            </div>
            <span class="is-disabled">
                <button v-if="!this.fans_40" @click="add_fans_40()" class="btn btn-primary add-server" :disabled="computedConditionFans40" :style="StyleFans40">
                    Добавить
                </button>
                <button v-else @click="add_fans_40()" class="btn btn-primary add-server" :disabled="computedConditionFans40" :style="StyleFans40">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleIndicatorBoard">
            <div class="title">
                Монтаж платы индикации
            </div>
            <span class="is-disabled">
                <button v-if="!this.indicator_board" @click="add_indicator_board()" class="btn btn-primary add-server" :disabled="computedConditionIndicatorBoard" :style="StyleIndicatorBoard">
                    Добавить
                </button>
                <button v-else @click="add_indicator_board()" class="btn btn-primary add-server" :disabled="computedConditionIndicatorBoard" :style="StyleIndicatorBoard">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStylePowerManagementModule">
            <div class="title">
                Монтаж платы управления питанием
            </div>
            <span class="is-disabled">
                <button v-if="!this.power_management_module" @click="add_power_management_module()" class="btn btn-primary add-server" :disabled="computedConditionPowerManagementModule" :style="StylePowerManagementModule">
                    Добавить
                </button>
                <button v-else @click="add_power_management_module()" class="btn btn-primary add-server" :disabled="computedConditionPowerManagementModule" :style="StylePowerManagementModule">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleCablesPMM">
            <div class="title">
                Подключение кабелей в плату управления питанием
            </div>
            <span class="is-disabled">
                <button v-if="!this.cables_pmm" @click="add_cables_pmm()" class="btn btn-primary add-server" :disabled="computedConditionCablesPMM" :style="StyleCablesPMM">
                    Добавить
                </button>
                <button v-else @click="add_cables_pmm()" class="btn btn-primary add-server" :disabled="computedConditionCablesPMM" :style="StyleCablesPMM">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleMemoryAndSSD">
            <div class="title">
                Монтаж модулей памяти и SSD диска в материнскую плату
            </div>
            <span class="is-disabled">
                <button v-if="!this.memory_and_ssd" @click="add_memory_and_ssd()" class="btn btn-primary add-server" :disabled="computedConditionMemoryAndSSD" :style="StyleMemoryAndSSD">
                    Добавить
                </button>
                <button v-else @click="add_memory_and_ssd()" class="btn btn-primary add-server" :disabled="computedConditionMemoryAndSSD" :style="StyleMemoryAndSSD">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleNetworkCard">
            <div class="title">
                Монтаж сетевой карты в плату «Райзер-2U» и платы «Райзер-2U» в материнскую плату
            </div>
            <span class="is-disabled">
                <button v-if="!this.network_card" @click="add_network_card()" class="btn btn-primary add-server" :disabled="computedConditionNetworkCard" :style="StyleNetworkCard">
                    Добавить
                </button>
                <button v-else @click="add_network_card()" class="btn btn-primary add-server" :disabled="computedConditionNetworkCard" :style="StyleNetworkCard">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleRaiser2UBoard">
            <div class="title">
                Установка батарейки в плату «Райзер-2U»
            </div>
            <span class="is-disabled">
                <button v-if="!this.raiser_2U_board" @click="add_raiser_2U_board()" class="btn btn-primary add-server" :disabled="computedConditionRaiser2UBoard" :style="StyleRaiser2UBoard">
                    Добавить
                </button>
                <button v-else @click="add_raiser_2U_board()" class="btn btn-primary add-server" :disabled="computedConditionRaiser2UBoard" :style="StyleRaiser2UBoard">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleMotherboard">
            <div class="title">
                Монтаж материнской платы в корпус
            </div>
            <span class="is-disabled">
                <router-link v-if="!this.motherboard" :to="{ name: 'AddMotherBoard', params: { id: this.id }}">
                  <button class="btn btn-primary add-server" :disabled="computedConditionMotherboard">Добавить</button>
                </router-link>
                <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionMotherboard" :style="StyleMotherboard">Выполнено</button></div>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleRaidCard">
            <div class="title">
                Монтаж RAID-контроллера в плату «Райзер-1U» и платы «Райзер-1U» в материнскую плату
            </div>
            <span class="is-disabled">
                <button v-if="!this.raid_card" @click="add_raid_card()" class="btn btn-primary add-server" :disabled="computedConditionRaidCard" :style="StyleRaidCard">
                    Добавить
                </button>
                <button v-else @click="add_raid_card()" class="btn btn-primary add-server" :disabled="computedConditionRaidCard" :style="StyleRaidCard">
                    Выполнено
                </button>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleCablesMB">
            <div class="title">
                Подключение всех кабелей в материнскую плату и карты расширения
            </div>
            <span class="is-disabled">
                <button v-if="!this.cables_mb" @click="add_cables_mb()" class="btn btn-primary add-server" :disabled="computedConditionCablesMB" :style="StyleCablesMB">
                    Добавить
                </button>
                <button v-else @click="add_cables_mb()" class="btn btn-primary add-server" :disabled="computedConditionCablesMB" :style="StyleCablesMB">
                    Выполнено
                </button>
            </span>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">2 этап</h5>
        <div class="rectangle" :style="computedStyleDiskBasket4">
            <div class="title">
                Монтаж дисковой корзины 4 (над материнской платой)
            </div>
            <span class="is-disabled">
              <router-link v-if="!this.disk_basket4" :to="{ name: 'AddDiskBasket4', params: { id: this.id }}">
                <button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket4">Добавить</button>
              </router-link>
              <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket4" :style="StyleDiskBasket4">Выполнено</button></div>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleDiskBasket3">
            <div class="title">
                Монтаж дисковой корзины 3
            </div>
            <span class="is-disabled">
              <router-link v-if="!this.disk_basket3" :to="{ name: 'AddDiskBasket3', params: { id: this.id }}">
                <button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket3">Добавить</button>
              </router-link>
              <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket3" :style="StyleDiskBasket3">Выполнено</button></div>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleDiskBasket2">
            <div class="title">
                Монтаж дисковой корзины 2
            </div>
            <span class="is-disabled">
              <router-link v-if="!this.disk_basket2" :to="{ name: 'AddDiskBasket2', params: { id: this.id }}">
                <button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket2">Добавить</button>
              </router-link>
              <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket2" :style="StyleDiskBasket2">Выполнено</button></div>
            </span>
        </div>
        <div class="rectangle" :style="computedStyleDiskBasket1">
            <div class="title">
                Монтаж дисковой корзины 1
            </div>
            <span class="is-disabled">
              <router-link v-if="!this.disk_basket1" :to="{ name: 'AddDiskBasket1', params: { id: this.id }}">
                <button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket1">Добавить</button>
              </router-link>
              <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionDiskBasket1" :style="StyleDiskBasket1">Выполнено</button></div>
            </span>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">3 этап</h5>
        <div class="rectangle" :style="computedStylePowerSupply2K6">
            <div class="title">
                Установка блоков питания 2.6 кВт в соответствующие отсеки
            </div>
            <span class="is-disabled">
                <button v-if="!this.power_supply_2k6" @click="add_power_supply_2k6()" class="btn btn-primary add-server" :disabled="computedConditionPowerSupply2K6" :style="StylePowerSupply2K6">
                    Добавить
                </button>
                <button v-else @click="add_power_supply_2k6()" class="btn btn-primary add-server" :disabled="computedConditionPowerSupply2K6" :style="StylePowerSupply2K6">
                    Выполнено
                </button>
            </span>
        </div>
        <router-link v-if="this.indicator_board && this.fans_40 && this.cables && this.fans_140 && this.fan_control_board && this.power_management_module && this.cables_pmm && this.cables_fcb && this.memory_and_ssd && this.network_card && this.raiser_2U_board && this.raid_card && this.cables_mb && this.motherboard && this.power_supply_2k6 && this.disk_basket4 && this.disk_basket3 && this.disk_basket2 && this.disk_basket1" :to="{ name: 'ServerList' }">
        <button class="btn btn-primary add-server" :disabled="computedConditionFinish">Завершить сборку СХД</button>
      </router-link>
      <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionFinish">Завершить сборку СХД</button></div>
    </div>
</template>

<style>
    a {
        text-decoration: none;
        background-color: transparent;
        /* pointer-events: none; */
    }
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
          motherboard: '',
          power_supply_2k6: '',
          disk_basket4: '',
          disk_basket3: '',
          disk_basket2: '',
          disk_basket1: '',
        };
      },
      props: {
        id: {
            type: [Number, String],
            required: true,
        },
      },
      methods: {
        add_indicator_board() {
        axios
          .post(`http://185.129.98.66:5000/app/add_indicator_board/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.indicator_board = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_fan40/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fans_40 = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_cables/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_fan140/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fans_140 = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_fan_control_board/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.fan_control_board = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_power_management_module/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.power_management_module = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_cables_pmm/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_pmm = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_cables_fcb/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_fcb = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_memory_and_ssd/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.memory_and_ssd = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_network_card/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.network_card = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_raiser_2U_board/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.raiser_2U_board = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_raid_card/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.raid_card = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
          .post(`http://185.129.98.66:5000/app/add_cables_mb/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_mb = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.cables_mb = response.data.cables_mb;
          })
          .catch((error) => {
            console.log(error);
          });
        },
        add_power_supply_2k6() {
        axios
          .post(`http://185.129.98.66:5000/app/add_power_supply_2k6/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.power_supply_2k6 = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            console.log(response.data);
            this.power_supply_2k6 = response.data.power_supply_2k6;
          })
          .catch((error) => {
            console.log(error);
          });
        },
      }, 
      created() {
        axios
          .get(`http://185.129.98.66:5000/app/get_chassis/${this.id}/`)
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
            this.motherboard = response.data.motherboard;
            this.power_supply_2k6 = response.data.power_supply_2k6;
            this.disk_basket4 = response.data.disk_basket4;
            this.disk_basket3 = response.data.disk_basket3;
            this.disk_basket2 = response.data.disk_basket2;
            this.disk_basket1 = response.data.disk_basket1;
            console.log(response);
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
        StyleIndicatorBoard() {
          if (this.indicator_board) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleFans40() {
          if (this.fans_40) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleCables() {
          if (this.cables) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleFans140() {
          if (this.fans_140) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleFanControlBoard() {
          if (this.fan_control_board) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StylePowerManagementModule() {
          if (this.power_management_module) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleCablesPMM() {
          if (this.cables_pmm) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleCablesFCB() {
          if (this.cables_fcb) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleMemoryAndSSD() {
          if (this.memory_and_ssd) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleNetworkCard() {
          if (this.network_card) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleRaiser2UBoard() {
          if (this.raiser_2U_board) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleRaidCard() {
          if (this.raid_card) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
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
        StyleCablesMB() {
          if (this.cables_mb) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionMotherboard() {
            if (this.motherboard) {
                return true;
            }
            return false;
        },
        computedStyleMotherboard() {
            if (this.motherboard) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        StyleMotherboard() {
          if (this.motherboard) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionPowerSupply2K6() {
            if (this.power_supply_2k6) {
                return true;
            }
            return false;
        },
        computedStylePowerSupply2K6() {
            if (this.power_supply_2k6) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        StylePowerSupply2K6() {
          if (this.power_supply_2k6) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionDiskBasket4() {
            if (this.disk_basket4) {
                return true;
            }
            return false;
        },
        computedStyleDiskBasket4() {
            if (this.disk_basket4) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        StyleDiskBasket4() {
          if (this.disk_basket4) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionDiskBasket3() {
            if (this.disk_basket3) {
                return true;
            }
            return false;
        },
        computedStyleDiskBasket3() {
            if (this.disk_basket3) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        StyleDiskBasket3() {
          if (this.disk_basket3) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionDiskBasket2() {
            if (this.disk_basket2) {
                return true;
            }
            return false;
        },
        computedStyleDiskBasket2() {
            if (this.disk_basket2) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        StyleDiskBasket2() {
          if (this.disk_basket2) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionDiskBasket1() {
            if (this.disk_basket1) {
                return true;
            }
            return false;
        },
        computedStyleDiskBasket1() {
            if (this.disk_basket1) {
                return {backgroundColor : '#22ed4ef2'};
            }
            return {backgroundColor : '#343a40'};
        },
        StyleDiskBasket1() {
          if (this.disk_basket1) {
                return {backgroundColor : '#636869', borderColor : '#636869'};
            }
        },
        computedConditionFinish() {
            if (this.indicator_board && this.fans_40 && this.cables && this.fans_140 && this.fan_control_board && this.power_management_module && this.cables_pmm && this.cables_fcb && this.memory_and_ssd && this.network_card && this.raiser_2U_board && this.raid_card && this.cables_mb && this.motherboard && this.power_supply_2k6 && this.disk_basket4 && this.disk_basket3 && this.disk_basket2 && this.disk_basket1) {
              return false;
            }
            return true;
        },
      },
    };
</script>
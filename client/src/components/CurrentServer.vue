<template>
    <div>
      <router-link class="go-back" :to="{ name: 'ServerList' }">Вернуться к списку серверов</router-link>
      <!--       <h3>{{ component.decoding }}</h3> -->
      <table class="table table-hover table-dark">
          <tr><td>ID</td><td>{{ server.id }}</td></tr>
          <tr><td>QR-код</td><td>{{ server.qrcode }}</td></tr>
          <tr><td>Статус</td><td>{{ server.sstat }}</td></tr>
          <tr><td>Выполнено:</td><td></td></tr>
          <tr v-if="server.cables" class="tr-item-success"><td></td><td>Монтаж кабелей/кабельных сборок/стяжек/метизов</td></tr>
          <tr v-if="server.fans_140" class="tr-item-success"><td></td><td>Монтаж 3 верхних вентиляторов в корпус</td></tr>
          <tr v-if="server.fan_control_board" class="tr-item-success"><td></td><td>Монтаж платы управления вентиляторами</td></tr>
          <tr v-if="server.cables_fcb" class="tr-item-success"><td></td><td>Подключение кабелей в плату управления вентиляторами</td></tr> 
          <tr v-if="server.fans_40" class="tr-item-success"><td></td><td>Монтаж 6 нижних вентиляторов в корпус</td></tr> 
          <tr v-if="server.indicator_board" class="tr-item-success"><td></td><td>Монтаж платы индикации</td></tr> 
          <tr v-if="server.power_management_module" class="tr-item-success"><td></td><td>Монтаж платы управления питанием</td></tr> 
          <tr v-if="server.cables_pmm" class="tr-item-success"><td></td><td>Подключение кабелей в плату управления питанием</td></tr> 
          <tr v-if="server.memory_and_ssd" class="tr-item-success"><td></td><td >Монтаж модулей памяти и SSD диска в материнскую плату</td></tr> 
          <tr v-if="server.network_card" class="tr-item-success"><td></td><td>Монтаж сетевой карты в плату «Райзер-2U» и платы «Райзер-2U» в материнскую плату</td></tr> 
          <tr v-if="server.raiser_2U_board" class="tr-item-success"><td></td><td>Установка батарейки в плату «Райзер-2U»</td></tr> 
          <tr v-if="server.motherboard" class="tr-item-success"><td></td><td>Монтаж материнской платы в корпус</td></tr> 
          <tr v-if="server.raid_card" class="tr-item-success"><td></td><td>Монтаж RAID-контроллера в плату «Райзер-1U» и платы «Райзер-1U» в материнскую плату</td></tr> 
          <tr v-if="server.cables_mb" class="tr-item-success"><td></td><td>Подключение всех кабелей в материнскую плату и карты расширения</td></tr> 
          <tr v-if="server.disk_basket4" class="tr-item-success"><td></td><td>Монтаж дисковой корзины 4 (над материнской платой)</td></tr> 
          <tr v-if="server.disk_basket3" class="tr-item-success"><td></td><td>Монтаж дисковой корзины 3</td></tr>
          <tr v-if="server.disk_basket2" class="tr-item-success"><td></td><td>Монтаж дисковой корзины 2</td></tr>
          <tr v-if="server.disk_basket1" class="tr-item-success"><td></td><td>Монтаж дисковой корзины 1</td></tr>
          <tr v-if="server.power_supply_2k6" class="tr-item-success"><td></td><td>Установка блоков питания 2.6 кВт в соответствующие отсеки</td></tr>
          <tr><td>В работе:</td><td></td></tr>
          <tr v-if="!server.cables" class="tr-item"><td></td><td>Монтаж кабелей/кабельных сборок/стяжек/метизов</td></tr>
          <tr v-if="!server.fans_140" class="tr-item"><td></td><td>Монтаж 3 верхних вентиляторов в корпус</td></tr>
          <tr v-if="!server.fan_control_board" class="tr-item"><td></td><td>Монтаж платы управления вентиляторами</td></tr>
          <tr v-if="!server.cables_fcb" class="tr-item"><td></td><td>Подключение кабелей в плату управления вентиляторами</td></tr> 
          <tr v-if="!server.fans_40" class="tr-item"><td></td><td>Монтаж 6 нижних вентиляторов в корпус</td></tr> 
          <tr v-if="!server.indicator_board" class="tr-item"><td></td><td>Монтаж платы индикации</td></tr> 
          <tr v-if="!server.power_management_module" class="tr-item"><td></td><td>Монтаж платы управления питанием</td></tr> 
          <tr v-if="!server.cables_pmm" class="tr-item"><td></td><td>Подключение кабелей в плату управления питанием</td></tr> 
          <tr v-if="!server.memory_and_ssd" class="tr-item"><td></td><td>Монтаж модулей памяти и SSD диска в материнскую плату</td></tr> 
          <tr v-if="!server.network_card" class="tr-item"><td></td><td>Монтаж сетевой карты в плату «Райзер-2U» и платы «Райзер-2U» в материнскую плату</td></tr> 
          <tr v-if="!server.raiser_2U_board" class="tr-item"><td></td><td>Установка батарейки в плату «Райзер-2U»</td></tr> 
          <tr v-if="!server.motherboard" class="tr-item"><td></td><td>Монтаж материнской платы в корпус</td></tr> 
          <tr v-if="!server.raid_card" class="tr-item"><td></td><td>Монтаж RAID-контроллера в плату «Райзер-1U» и платы «Райзер-1U» в материнскую плату</td></tr> 
          <tr v-if="!server.cables_mb" class="tr-item"><td></td><td>Подключение всех кабелей в материнскую плату и карты расширения</td></tr> 
          <tr v-if="!server.disk_basket4" class="tr-item"><td></td><td>Монтаж дисковой корзины 4 (над материнской платой)</td></tr> 
          <tr v-if="!server.disk_basket3" class="tr-item"><td></td><td>Монтаж дисковой корзины 3</td></tr>
          <tr v-if="!server.disk_basket2" class="tr-item"><td></td><td>Монтаж дисковой корзины 2</td></tr>
          <tr v-if="!server.disk_basket1" class="tr-item"><td></td><td>Монтаж дисковой корзины 1</td></tr>
          <tr v-if="!server.power_supply_2k6" class="tr-item"><td></td><td>Установка блоков питания 2.6 кВт в соответствующие отсеки</td></tr>
          <tr><td>Опции</td><td><router-link v-if="server.indicator_board && server.fans_40 && server.cables && server.fans_140 && server.fan_control_board && server.power_management_module && server.cables_pmm && server.cables_fcb && server.memory_and_ssd && server.network_card && server.raiser_2U_board && server.raid_card && server.cables_mb && server.motherboard && server.power_supply_2k6 && server.disk_basket4 && server.disk_basket3 && server.disk_basket2 && server.disk_basket1" :to="{ name: 'ServerList' }">
        <button class="btn btn-primary add-server" :disabled="computedConditionFinish">Протестировать</button>
      </router-link>
      <div v-else><button class="btn btn-primary add-server" :disabled="computedConditionFinish">Протестировать</button></div></td></tr>
      </table>
    </div>
  </template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      server: [],
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    //   get server
    serverDetail() {
      axios
        .get(`http://192.168.88.11:5000/app/current_server/${this.id}/`)
        .then((response) => {
          this.server = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
      this.serverDetail();
  },
  computed : {
    computedConditionFinish() {
            if (this.server.indicator_board && this.server.fans_40 && this.server.cables && this.server.fans_140 && this.server.fan_control_board && this.server.power_management_module && this.server.cables_pmm && this.server.cables_fcb && this.server.memory_and_ssd && this.server.network_card && this.server.raiser_2U_board && this.server.raid_card && this.server.cables_mb && this.server.motherboard && this.server.power_supply_2k6 && this.server.disk_basket4 && this.server.disk_basket3 && this.server.disk_basket2 && this.server.disk_basket1) {
              return false;
            }
            return true;
        },
  }
};
</script>

<style>
.tr-item {
  background-color: #848f9a;
}
.tr-item-success {
  background-color: #16ac36c7;
}
</style>
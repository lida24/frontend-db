import Vue from 'vue';
import Router from "vue-router";
import CreateComponent from "@/components/CreateComponent";
import Ping from "@/components/Ping";
import Home from "@/components/Home";
import SelectAction from "@/components/SelectAction";
import ComponentList from "@/components/ComponentList";
import ComponentDetail from "@/components/ComponentDetail";
import ServerList from "@/components/ServerList";
import AddChassis from "@/components/AddChassis";
import AddFan140 from "@/components/AddFan140";
import AddFanControlBoard from "@/components/AddFanControlBoard";
import AddFan40 from "@/components/AddFan40";
import AddIndicatorBoard from "@/components/AddIndicatorBoard";
import AddPowerManagementModule from "@/components/AddPowerManagementModule";
import AddMotherBoard from "@/components/AddMotherBoard";

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/ping",
      name: "Ping",
      component: Ping,
    },
    {
      path: "/create_component",
      name: "CreateComponent",
      component: CreateComponent,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/select_action',
      name: 'SelectAction',
      component: SelectAction,
    },
    {
      path: '/component_list',
      name: 'ComponentList',
      component: ComponentList,
    },
    {
      path: '/component_detail/:id',
      name: 'ComponentDetail',
      component: ComponentDetail,
      props: true,
    },
    {
      path: '/server_list',
      name: 'ServerList',
      component: ServerList,
    },
    {
      path: '/add_chassis',
      name: 'AddChassis',
      component: AddChassis,
    },
    {
      path: '/add_fan140/:id',
      name: 'AddFan140',
      component: AddFan140,
      props: true,
    },
    {
      path: '/add_fan_control_board/:id',
      name: 'AddFanControlBoard',
      component: AddFanControlBoard,
      props: true,
    },
    {
      path: '/add_fan40/:id',
      name: 'AddFan40',
      component: AddFan40,
      props: true,
    },
    {
      path: '/add_indicator_board/:id',
      name: 'AddIndicatorBoard',
      component: AddIndicatorBoard,
      props: true,
    },
    {
      path: '/add_power_management_module/:id',
      name: 'AddPowerManagementModule',
      component: AddPowerManagementModule,
      props: true,
    },
    {
      path: '/add_motherboard/:id',
      name: 'AddMotherBoard',
      component: AddMotherBoard,
      props: true,
    },
    {
      path: '/add_ddr4_memory_module/:id',
      name: 'AddDDR4MemoryModule',
      component: AddDDR4MemoryModule,
      props: true,
    },
    {
      path: '/add_m2_ssd/:id',
      name: 'AddM2SSD',
      component: AddM2SSD,
      props: true,
    },
  ],
});

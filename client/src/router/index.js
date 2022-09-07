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
      path: '/add_fan140',
      name: 'AddFan140',
      component: AddFan140,
      props: true,
    },
  ],
});

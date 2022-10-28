<!-- <template>
  <div>
    <router-link class="go-back" :to="{ name: 'ComponentList' }">Вернуться к компонентам</router-link>
    <h3>{{ component[0].decoding }}</h3>
    <table class="table table-hover table-dark">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Заключение</th>
                <th scope="col">QR-код</th>
                <th scope="col">Статус</th>
                <th scope="col">Ссылка на результаты теста</th>
                <th scope="col">Комментарий</th>
                <th scope="col">Опции</th>
            </tr>
        </thead>
        <tbody v-for="c in component">
            <td>{{ c.id }}</td>          
            <td>{{ c.conclusion }}</td>
            <td>{{ c.qrcode }}</td>
            <td>{{ c.cstat }}</td>
            <td><a class="btn btn-outline btn-info disabled" href="#">{{ c.tests }}</a></td>
            <td><a class="btn btn-outline btn-info disabled" href="#">{{ c.rem }}</a></td>
            <td><router-link class="btn btn-outline btn-info" :to="{ name: 'Testing', params: { id: c.id }}">Протестировать</router-link></td>
        </tbody>
    </table>
  </div>
</template> -->

<template>
  <div>
    <router-link class="go-back" :to="{ name: 'ComponentList' }">Вернуться к компонентам</router-link>
    <h3>{{ component[0].decoding }}</h3>
    <table class="table table-hover table-dark">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">QR-код</th>
                <th scope="col">Опции</th>
            </tr>
        </thead>
        <tbody v-for="c in component">
            <td>{{ c.id }}</td>          
            <td>{{ c.qrcode }}</td>
            <td><router-link class="btn btn-outline btn-info" :to="{ name: 'CurrentComponent', params: { id: c.id }}">Подробнее</router-link></td>
            <!-- <td><router-link class="btn btn-outline btn-info" :to="{ name: 'Testing', params: { id: c.id }}">Протестировать</router-link></td> -->
        </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      component: [],
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    //   get component
    componentDetail() {
      axios
        .get(`http://192.168.75.11:5000/app/component/${this.id}/`)
        .then((response) => {
          this.component = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
      this.componentDetail();
  },
};
</script>
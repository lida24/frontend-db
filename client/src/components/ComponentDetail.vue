<template>
  <div>
    <router-link class="go-back" :to="{ name: 'ComponentList' }">Вернуться к компонентам</router-link>
    <h3>{{ component[0].decoding }}</h3>
    <table class="table table-hover table-dark">
        <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">QR-код</th>
                <th scope="col">Последнее время изменения статуса</th>
                <th scope="col">Статус</th>
                <th scope="col">Заключение</th>
                <th scope="col">Опции</th>
            </tr>
        </thead>
        <tbody v-for="c in component">
            <td>{{ c.id }}</td>          
            <td>{{ c.qrcode }}</td>
            <!-- <td>{{ c.addts.split('GMT').join('').split('Mon,').join('').split('Tue,').join('').split('Wed,').join('').split('Thu,').join('').split('Fri,').join('').split('Sat,').join('').split('Sun,').join('') }}</td> -->
            <td>{{ c.statts.split('GMT').join('').split('Mon,').join('').split('Tue,').join('').split('Wed,').join('').split('Thu,').join('').split('Fri,').join('').split('Sat,').join('').split('Sun,').join('') }}</td>
            <td>{{ c.cstat }}</td>
            <td>{{ c.conclusion }}</td>
            <td><router-link class="btn btn-outline btn-info" :to="{ name: 'CurrentComponent', params: { id: c.id }}">Подробнее</router-link></td>
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
        .get(`http://192.168.88.11:5000/app/component/${this.id}/`)
        .then((response) => {
          this.component = response.data;
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
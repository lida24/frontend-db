<template>
    <div>
      <router-link class="go-back" :to="{ name: 'ComponentDetail', params: { id: component.ctype_id } }">Вернуться к компонентам</router-link>
      <h3>{{ component.decoding }}</h3>
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
          <tbody>
              <td>{{ this.component.id }}</td>          
              <td>{{ this.component.conclusion }}</td>
              <td>{{ this.component.qrcode }}</td>
              <td>{{ this.component.cstat }}<div class="stage" style="display: none;"><div class="dot-spin"></div></div></td>
              <td><a class="btn btn-outline btn-info disabled" href="#">{{ this.component.tests }}</a></td>
              <td><a class="btn btn-outline btn-info disabled" href="#">{{ this.component.rem }}</a></td>
              <td><button class="btn btn-outline btn-info" @click="testing()" :disabled="computedCondition">Протестировать</button></td>
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
        .get(`http://192.168.75.11:5000/app/current_component/${this.id}/`)
        .then((response) => {
          this.component = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    testing() {
      axios
        .get(`http://192.168.75.11:5000/app/testing/${this.component.id}/`)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error, error.response);
        });
        setInterval(() => { axios
            .get(`http://192.168.75.11:5000/app/getstatus/${this.component.id}/`)
            .then((response) => {
              if (response.data == null) {
                this.component.cstat = 'тестируется';
                let elem = document.querySelector(".stage");
                if (elem != null) {
                  elem.style.display = "flex";
                }
              } else if (response.data != null) {
                    this.component.cstat = response.data;
                    /* this.component.conclusion = response.data.conclusion; */
                    let element = document.querySelector(".stage");
                    element.style.display = "none";
                    console.log("Status: ", this.component.cstat);
                    console.log(response);
              }
            })
            .catch((error) => {
              console.log(error, error.response);
            });
          }, 2000);
    }
  },
  computed: {
    computedCondition() {
      if (this.component.cstat == 'протестирован') {
        return true;
      }
      else {
        return false;
      } 
    }
   },
  created() {
      this.componentDetail();
  },
};
</script>

<style>
.stage {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    padding: 2rem 0;
    margin: 0 -5%;
    overflow: hidden;
}
.dot-spin {
    position: relative;
    width: 10px;
    height: 10px;
    border-radius: 5px;
    background-color: transparent;
    color: transparent;
    box-shadow: 0 -18px 0 0 #9880ff, 12.72984px -12.72984px 0 0 #9880ff, 18px 0 0 0 #9880ff, 12.72984px 12.72984px 0 0 rgb(152 128 255 / 0%), 0 18px 0 0 rgb(152 128 255 / 0%), -12.72984px 12.72984px 0 0 rgb(152 128 255 / 0%), -18px 0 0 0 rgb(152 128 255 / 0%), -12.72984px -12.72984px 0 0 rgb(152 128 255 / 0%);
    animation: dotSpin 1.5s infinite linear;
}
@keyframes dotSpin {
  0%,
  100% {
    box-shadow: 0 -18px 0 0 #9880ff, 12.72984px -12.72984px 0 0 #9880ff, 18px 0 0 0 #9880ff, 12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), 0 18px 0 -5px rgba(152, 128, 255, 0), -12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), -18px 0 0 -5px rgba(152, 128, 255, 0), -12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0);
  }
  12.5% {
    box-shadow: 0 -18px 0 -5px rgba(152, 128, 255, 0), 12.72984px -12.72984px 0 0 #9880ff, 18px 0 0 0 #9880ff, 12.72984px 12.72984px 0 0 #9880ff, 0 18px 0 -5px rgba(152, 128, 255, 0), -12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), -18px 0 0 -5px rgba(152, 128, 255, 0), -12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0);
  }
  25% {
    box-shadow: 0 -18px 0 -5px rgba(152, 128, 255, 0), 12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0), 18px 0 0 0 #9880ff, 12.72984px 12.72984px 0 0 #9880ff, 0 18px 0 0 #9880ff, -12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), -18px 0 0 -5px rgba(152, 128, 255, 0), -12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0);
  }
  37.5% {
    box-shadow: 0 -18px 0 -5px rgba(152, 128, 255, 0), 12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0), 18px 0 0 -5px rgba(152, 128, 255, 0), 12.72984px 12.72984px 0 0 #9880ff, 0 18px 0 0 #9880ff, -12.72984px 12.72984px 0 0 #9880ff, -18px 0 0 -5px rgba(152, 128, 255, 0), -12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0);
  }
  50% {
    box-shadow: 0 -18px 0 -5px rgba(152, 128, 255, 0), 12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0), 18px 0 0 -5px rgba(152, 128, 255, 0), 12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), 0 18px 0 0 #9880ff, -12.72984px 12.72984px 0 0 #9880ff, -18px 0 0 0 #9880ff, -12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0);
  }
  62.5% {
    box-shadow: 0 -18px 0 -5px rgba(152, 128, 255, 0), 12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0), 18px 0 0 -5px rgba(152, 128, 255, 0), 12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), 0 18px 0 -5px rgba(152, 128, 255, 0), -12.72984px 12.72984px 0 0 #9880ff, -18px 0 0 0 #9880ff, -12.72984px -12.72984px 0 0 #9880ff;
  }
  75% {
    box-shadow: 0 -18px 0 0 #9880ff, 12.72984px -12.72984px 0 -5px rgba(152, 128, 255, 0), 18px 0 0 -5px rgba(152, 128, 255, 0), 12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), 0 18px 0 -5px rgba(152, 128, 255, 0), -12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), -18px 0 0 0 #9880ff, -12.72984px -12.72984px 0 0 #9880ff;
  }
  87.5% {
    box-shadow: 0 -18px 0 0 #9880ff, 12.72984px -12.72984px 0 0 #9880ff, 18px 0 0 -5px rgba(152, 128, 255, 0), 12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), 0 18px 0 -5px rgba(152, 128, 255, 0), -12.72984px 12.72984px 0 -5px rgba(152, 128, 255, 0), -18px 0 0 -5px rgba(152, 128, 255, 0), -12.72984px -12.72984px 0 0 #9880ff;
  }
}
</style>
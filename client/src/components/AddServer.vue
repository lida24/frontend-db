<template>
    <div class="wrap">
        <h4 class="h3 mb-3 font-weight-normal main-title">
            Этапы сборки
        </h4>
        <h5 class="h4 mb-3 font-weight-normal step-title">0 этап</h5>
        <div class="rectangle">
            <div class="title">
                Монтаж кабелей/кабельных сборок/стяжек/метизов
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">1 этап</h5>
        <div class="rectangle">
            <div class="title">
                Монтаж 3 верхних вентиляторов в корпус
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddFan140', params: { id: n }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж платы управления вентиляторами
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddFanControlBoard', params: { id: n }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Подключение кабелей в плату управления вентиляторами
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж 6 нижних вентиляторов в корпус
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddFan40', params: { id: n }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж платы индикации
            </div>
            <span class="is-disabled">
                <router-link class="btn btn-primary add-server" :to="{ name: 'AddIndicatorBoard', params: { id: n }}">Добавить</router-link>
            </span>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж платы управления питанием
            </div>
            <span class="is-disabled">
                <router-link class="btn btn-primary add-server" :to="{ name: 'AddPowerManagementModule', params: { id: n }}">Добавить</router-link>
            </span>
        </div>
        <div class="rectangle">
            <div class="title">
                Подключение кабелей в плату управления питанием
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж модулей памяти и SSD диска в материнскую плату
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddMotherBoard', params: { id: n }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж сетевой карты в плату «Райзер-2U» и платы «Райзер-2U» в материнскую плату
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddRaiser2UBoard', params: { id: n }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Установка батарейки в плату «Райзер-2U»
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж материнской платы в корпус
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж RAID-контроллера в плату «Райзер-1U» и платы «Райзер-1U» в материнскую плату
            </div>
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddRaiser1UBoard', params: { id: n }}">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Подключение всех кабелей в материнскую плату и карты расширения
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
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
        background-color: #343a40;
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
          n: Number,
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
      },
    
      created() {
        axios
          .get(`http://192.168.75.11:5000/app/get_chassis/${this.id}/`)
          .then((response) => {
            this.n = response.data;
            console.log(response);
            console.log("AddServer: ", this.success);
            if (this.success) {
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
            }
          })
          .catch((error) => {
            console.log(error);
          });
      },
    };
</script>
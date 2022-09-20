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
            <router-link class="btn btn-primary add-server" :to="{ name: 'AddFan140' }">Добавить</router-link>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж платы управления вентиляторами
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
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
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж платы индикации
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж платы управления питанием
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
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
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж сетевой карты в плату «Райзер-2U» и платы «Райзер-2U» в материнскую плату
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
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
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
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
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 3
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 2
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <div class="rectangle">
            <div class="title">
                Монтаж дисковой корзины 1
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
        </div>
        <h5 class="h4 mb-3 font-weight-normal step-title">3 этап</h5>
        <div class="rectangle">
            <div class="title">
                Установка блоков питания 2.6 кВт в соответствующие отсеки
            </div>
            <button type="submit" class="btn btn-primary add-server">
                Добавить
            </button>
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
</style>
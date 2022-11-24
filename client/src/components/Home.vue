<!-- <template>
    <div class="multiple-button-states">
      <button type="button" :class="buttonClass" @click="changeButtonState">Trigger color change</button>
    </div>
  </template>
  
  <script>
    export default {
      data() {
        return {
          buttonState: 1
        }
      },
      computed: {
        buttonClass() {
          let returnClass = ''
          switch(this.buttonState) {
            case 2:
              returnClass = 'green';
              break;
            case 3:
              returnClass = 'blue';
              break;
            case 4:
              returnClass = 'yellow';
              break;
            default:  // 1
              returnClass = 'red';
          }
  
          return returnClass;
        }
      },
      methods: {
        changeButtonState() {
          if (this.buttonState === 4) {
            this.buttonState = 1;
          }
          else {
            this.buttonState++;
          }
        }
      }
  
    }
  </script>
  
  <style scoped>
  .red {
    background-color: red;
  }

  .green {
    background-color: green;
  }

  .blue {
    background-color: blue;
  }

  .yellow {
    background-color: yellow;
  }
</style> -->

<!-- <template>
    <div>
      <div>
        <div v-for="(i, index) in buttonsGroup" :key="index">
          <button
            :class="{
              EthnicityActive:
                i === EthnicityActive && 'EthnicityActive-' + index,
            }"
            v-on:click="EthnicityActive = i"
          >
            {{ i.btnText }}
          </button>
        </div>
      </div>
  
      <div class="save">
        <button @click="save">Save to local storage</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        buttonsGroup: [
          { btnText: "Green", value: "green-value" },
          { btnText: "Blue", value: "blue-value" },
          { btnText: "Orange", value: "orange-value" },
        ],
        Save: null,
        EthnicityActive: "",
      };
    },
    methods: {
        save() { localStorage.setItem('selectedBtn',JSON.stringify(this.EthnicityActive)); }
    },
  };
</script> -->

<!-- <template>
    <div class="container">
        <button :disabled="!isActive">Disable</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isActive: false,
      };
    },
  }
  </script> -->

  <!-- <template>
    <div class="hello">
      <button @click="test" :disabled="cnt > 1">test</button>
      {{ cnt }}
    </div>
  </template>
  
  <script>
      export default {
          name: 'HelloWorld',
          data: function () {
             return {
                 disableBtnFlag: false,
                 cnt: 1
             }
          },
          methods: {
              test: function () {
                  if(!this.disableBtnFlag) {
                      this.disableBtnFlag = true;
                      // something to do
                      this.cnt = ++this.cnt;
                  }
              }
          }
      }
  </script>
   -->
  
<template>
    <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-dark"
     style="color:white">
    <div class="col-md-5 p-lg-5 mx-auto my-5">
        <h1 class="display-4 font-weight-normal">Система контроля</h1>
        <p class="lead font-weight-normal">Начните работу, нажав кнопку ниже</p>
        <router-link class="btn btn-primary" :to="{ name: 'SelectAction' }">Начать</router-link>
    </div>
    <div class="product-device box-shadow d-none d-md-block"></div>
    <div class="product-device product-device-2 box-shadow d-none d-md-block"></div>
    </div>
</template>
<template>
  <div class="hand testing">
    <div>
      <div class="container form">
      <br />
      <form method="post" @submit.prevent="setConclusion">
        <h4 class="h3 mb-3 font-weight-normal">
            Определите годность изделия
        </h4>
          <br>
          <div class="btn btn-success">Годен<input type="radio" value="годен" class="btn btn-success radio" v-model="form.conclusion"/></div>
          <div class="btn btn-danger">Не годен<input type="radio" value="не годен" class="btn btn-danger radio" v-model="form.conclusion"/></div>
          <br>
          <br>
          <br>
          <br>
          <button v-if="this.form.conclusion != ''" type="submit" class="btn btn-primary">
            Добавить
          </button>
      </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
 data() {
    return {
      form: {
        conclusion: "",
      },
    };
 },
 props: {
    id: {
      type: [Number, String],
      required: true,
    },
 },
 methods: {
    setConclusion() {
        axios
        .post(`http://127.0.0.1:5000/app/hand_testing/${this.id}/`, this.form)
        .then((response) => {
          console.log(response);
          this.$router.push({ name: 'CurrentComponent', params: { id: this.id } });
        })
        .catch((error) => {
          console.log(error, error.response);
        });
    }
 },
};
</script>

<style>
.radio {
    margin-left: 5px;
}
</style>
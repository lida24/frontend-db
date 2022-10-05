<template>
    <div class="container">
      Testing
    </div>
</template>

<script>
    import axios from "axios";
    export default {
      data() {
        return {
          servers: [],
        };
      },
      props: {
        id: {
          type: [Number, String],
          required: true,
        },
      },
        created() {
          axios
            .get(`http://192.168.75.11:5000/app/testing/${this.id}/`)
            .then((response) => {
              this.servers = response.data;
              console.log(response);
            })
            .catch((error) => {
              console.log(error, error.response);
            });
        }
    };
</script>
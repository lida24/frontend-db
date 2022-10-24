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
            .get(`http://127.0.0.1:5001/app/testing/${this.id}/`)
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
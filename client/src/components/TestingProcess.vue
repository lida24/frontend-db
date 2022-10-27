<template>
    <div class="container">
      Status: {{ this.status }}
    </div>
</template>


<script>
    import axios from "axios";
    export default {
      data() {
        return {
          status: ''
        };
      },
      props: {
        id: {
          type: [Number, String],
          required: true,
        },
      },
        created() {
          setInterval(() => { axios
            .get(`http://192.168.75.11:5000/app/getstatus/${this.id}/`)
            .then((response) => {
              if (response.data == null) {
                this.status = 'тестируется';
              } else if (response.data != null) {
                    this.status = response.data;
                    console.log("Status: ", this.status);
                    console.log(response);
              }
            })
            .catch((error) => {
              console.log(error, error.response);
            });
          }, 2000);
        },
    };
</script>
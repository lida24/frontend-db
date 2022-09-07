<template>
  <div>
    <h3>Все серверы</h3>
    <table class="table table-hover table-dark">
        <thead>
            <tr>
                <th scope="col">QR-код</th>
                <th scope="col">Время начала сбора</th>
                <th scope="col">ID сборщика</th>
                <th scope="col">Время начала тестового прогона</th>
                <th scope="col">Результаты тестового прогона</th>
                <th scope="col">Статус</th>
                <th scope="col">Опции</th>
            </tr>
        </thead>
        <tbody v-for="server in servers">
                <td>{{ server.qrcode }}</td>
                <td>{{ server.asts }}</td>
                <td>{{ server.aid}}</td>
                <td>{{ server.tstts }}</td>
                <td>{{ server.tstres }}</td>
                <td>{{ server.sstat }}</td>
                <td>
                    <a class="btn btn-outline btn-info" href="#">Просмотреть</a>
                </td>
        </tbody>
    </table>
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
    
      created() {
        axios
          .get("http://127.0.0.1:5000/app/server_list")
          .then((response) => {
            this.servers = response.data;
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
      },
    };
</script>
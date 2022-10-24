<template>
    <div>
        <h3>Все компоненты</h3>
        <table class="table table-hover table-dark">
            <thead>
                <tr>
                    <th scope="col">Изделие</th>
                    <th scope="col">Количество</th>
                    <th scope="col">Опции</th>
                </tr>
            </thead>
            <tbody v-for="component in components" :key="component.id">
                    <td>{{ component.decoding }}</td>
                    <td>{{ component.count }}</td>
                    <td>
                        <router-link class="btn btn-outline btn-info" :to="{ name: 'ComponentDetail', params: { id: component.id } }">Просмотреть</router-link>
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
          components: [],
        };
      },
    
      created() {
        axios
          .get("http://127.0.0.1:5001/app/component_list")
          .then((response) => {
            this.components = response.data;
            console.log("Components: ",this.components);
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
      },
    };
    </script>
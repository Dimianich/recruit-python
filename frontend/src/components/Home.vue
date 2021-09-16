<template>
  <div>
    <navbar />
    <div class="buttons">
      <b-button type="is-primary" outlined @click="getDataDb"
        >Данные из БД</b-button
      >
      <b-button type="is-primary" outlined @click="getDataRedis"
        >Данные из Redis</b-button
      >
      <b-button type="is-primary" outlined @click="getDataLog"
        >Данные из log.json</b-button
      >
    </div>
    <b-table :data="data" :columns="columns"></b-table>
  </div>
</template>

<script>
import Navbar from "./Navbar.vue";

export default {
  name: "Home",
  components: {
    navbar: Navbar,
  },
  data() {
    return {
      data: [],
      columns: [
        {
          field: "info",
          label: "Info",
        },
      ],
    };
  },
  methods: {
    async getDataDb() {
      try {
        let response = await fetch("http://backend/db", {
          method: "GET",
          headers: {
            Authorization: "Bearer " + localStorage.getItem("user"),
          },
        });

        if (response.ok) {
          let result = await response.json();
          this.data = result;
        } else {
          this.$buefy.notification.open({
            message: "Ошибка HTTP: " + response.status + " " + response.message,
            position: "is-bottom-right",
            type: "is-danger",
          });
        }
      } catch (err) {
        console.log(err.response);
      }
    },
    async getDataRedis() {
      try {
        let response = await fetch("http://backend/redis", {
          method: "GET",
          headers: {
            Authorization: "Bearer " + localStorage.getItem("user"),
          },
        });

        if (response.ok) {
          let result = await response.json();
          this.data = result;
        } else {
          this.$buefy.notification.open({
            message: "Ошибка HTTP: " + response.status + " " + response.message,
            position: "is-bottom-right",
            type: "is-danger",
          });
        }
      } catch (err) {
        console.log(err.response);
      }
    },
    async getDataLog() {
      try {
        let response = await fetch("http://backend/log", {
          method: "GET",
          headers: {
            Authorization: "Bearer " + localStorage.getItem("user"),
          },
        });

        if (response.ok) {
          let result = await response.json();
          this.data = result;
        } else {
          this.$buefy.notification.open({
            message: "Ошибка HTTP: " + response.status + " " + response.message,
            position: "is-bottom-right",
            type: "is-danger",
          });
        }
      } catch (err) {
        console.log(err.response);
      }
    },
  },
};
</script>


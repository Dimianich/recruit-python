<template>
  <div>
    <navbar />
    <div class="buttons">
      <b-button type="is-primary" outlined @click="setDataDb"
        >Сохранить данные в БД</b-button
      >
      <b-button type="is-primary" outlined @click="setDataRedis"
        >Сохранить данные в Redis</b-button
      >
    </div>
    <b-field label="Info">
      <b-input
        maxlength="200"
        type="textarea"
        required
        v-model="msg.info"
      ></b-input>
    </b-field>
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
      msg: {
        info: "",
      },
    };
  },
  methods: {
    async setDataDb() {
      if (this.msg.info === "") {
        this.$buefy.notification.open({
          message: "Не заполнено поле Info",
          position: "is-bottom-right",
          type: "is-danger",
        });
        return false;
      }

      try {
        let response = await fetch("backend/db", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            Authorization: "Bearer " + localStorage.getItem("user"),
          },
          body: JSON.stringify(this.msg),
        });

        if (response.ok) {
          this.$buefy.notification.open({
            message: "Данные сохранены в БД",
            position: "is-bottom-right",
            type: "is-success",
          });
          this.msg.info = "";
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
    async setDataRedis() {
      if (this.msg.info === "") {
        this.$buefy.notification.open({
          message: "Не заполнено поле Info",
          position: "is-bottom-right",
          type: "is-danger",
        });
        return false;
      }

      try {
        let response = await fetch("backend/redis", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            Authorization: "Bearer " + localStorage.getItem("user"),
          },
          body: JSON.stringify(this.msg),
        });

        if (response.ok) {
          this.$buefy.notification.open({
            message: "Данные сохранены в Redis",
            position: "is-bottom-right",
            type: "is-success",
          });
          this.msg.info = "";
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


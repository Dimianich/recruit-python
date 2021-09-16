<template>
  <section>
    <div class="title">Авторизация</div>
    <b-field label="Имя" horizontal>
      <b-input type="text" required v-model="login.username"></b-input>
    </b-field>

    <b-field label="Пароль" horizontal>
      <b-input type="password" required v-model="login.password"></b-input>
    </b-field>

    <b-button type="is-primary" @click="logIn">Войти</b-button>

    <div>
      У вас еще нет аккаунта? Нажмите
      <router-link to="/register"> сюда </router-link> для регистрации
    </div>
  </section>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      login: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async logIn() {
      if (this.login.username === "" || this.login.password === "") {
        this.$buefy.notification.open({
          message: "Не заполнено поле Имя или Пароль",
          position: "is-bottom-right",
          type: "is-danger",
        });
        return false;
      }
      try {
        let response = await fetch("http://backend/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify(this.login),
        });

        if (response.ok) {
          let result = await response.json();
          let token = result.acces_token;
          localStorage.setItem("user", token);
          localStorage.setItem("username", this.login.username);
          this.$router.push("/home");
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

<style>
section {
  width: 40%;
  margin: auto;
  text-align: center;
}
</style>

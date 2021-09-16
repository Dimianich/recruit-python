<template>
  <section>
    <div class="title">Регистрация</div>
    <b-field label="Имя" horizontal>
      <b-input type="text" required v-model="register.username"></b-input>
    </b-field>

    <b-field label="Пароль" horizontal>
      <b-input type="password" required v-model="register.password"></b-input>
    </b-field>

    <b-field label="Пароль" horizontal>
      <b-input
        type="password"
        required
        v-model="register.confirmPassword"
      ></b-input>
    </b-field>

    <b-button type="is-primary" @click="signUp">Зарегистрироваться</b-button>
  </section>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      register: {
        username: "",
        password: "",
        confirmPassword: "",
      },
    };
  },
  methods: {
    async signUp() {
      if (
        this.register.username === "" ||
        this.register.password === "" ||
        this.register.confirmPassword === ""
      ) {
        this.$buefy.notification.open({
          message: "Не заполнено поле Имя или Пароль",
          position: "is-bottom-right",
          type: "is-danger",
        });
        return false;
      }

      if (this.register.password !== this.register.confirmPassword) {
        this.$buefy.notification.open({
          message: "Не верно заполнено имя Пароль",
          position: "is-bottom-right",
          type: "is-danger",
        });
        return false;
      }

      try {
        let response = await fetch("http://backend:5000/registration", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
          body: JSON.stringify(this.register),
        });

        if (response.ok) {
          let result = await response.json();
          let token = result.acces_token;
          localStorage.setItem("user", token);
          localStorage.setItem("username", this.register.username);
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

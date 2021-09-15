<template>
  <b-navbar>
    <template #start>
      <b-navbar-item>
        <router-link to="/home"> Отобразить данные </router-link>
      </b-navbar-item>
      <b-navbar-item>
        <router-link to="/save"> Сохранить данные </router-link>
      </b-navbar-item>
    </template>

    <template #end>
      <b-navbar-item>
        <div class="usernameText">{{ username }}</div>
        <b-button type="is-primary" @click="logOut">Выйти</b-button>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    logOut() {
      localStorage.removeItem("user");
      this.$router.push("/");
    },
  },
  mounted() {
    this.username = localStorage.getItem("username");
  },
};
</script>

<style>
.usernameText {
  font-size: 20px;
  margin-right: 10px;
}
</style>
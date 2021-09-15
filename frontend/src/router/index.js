import Vue from 'vue';
import VueRouter from 'vue-router';
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import Home from '../components/Home.vue'
import Save from '../components/Save.vue'
Vue.use(VueRouter);


export default new VueRouter({
    routes: [
        {
            path: '/register',
            name: 'Register',
            component: Register
        },
        {
            path: '/',
            name: 'Login',
            component: Login
        },
        {
            path: '/save',
            name: 'Save',
            component: Save
        },
        {
            path: '/home',
            name: 'Home',
            component: Home
        }]
});
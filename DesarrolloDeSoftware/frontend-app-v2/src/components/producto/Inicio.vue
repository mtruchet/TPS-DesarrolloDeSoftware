<template>
  <div>
    <b-row v-if="!loggedIn">
      <div class="login-container">
        <br>
        <br>
        <b-card class="small-card mx-auto">
          <b-card-title
            title-tag="h2"
            class="font-weight-bold mb-1 text-center"
          >
            <b>Inicio de Sesión</b>
          </b-card-title>
          <form @submit.prevent="login">
            <b-input
              type="text"
              v-model="username"
              placeholder="Nombre de usuario"
            />
            <br>
            <b-input
              type="password"
              v-model="password"
              placeholder="Contraseña"
            />
            <br>
            <b-button type="submit">Iniciar Sesión</b-button>
          </form>
        </b-card>
      </div>
    </b-row>
    <b-row v-else>
      <b-col
        md="3"
        class="side-menu p-0"
      >
        <div class="side-menu-inner">
          <ul>
            <li></li>
            <li
              :class="{ active: activeTab === 'Inicio' }"
              @click="changeTab('Inicio')"
            ><b>Inicio</b></li>
            <li
              :class="{ active: activeTab === 'Productos' }"
              @click="changeTab('Productos')"
            ><b>Productos</b>
            </li>
          </ul>
        </div>
      </b-col>
      <b-col md="9">
        <div
          :style="{ backgroundColor: user.color }"
          class="background"
        >
          <h3 class="title-text">
            <b>Pagina de productos deportivos</b>
          </h3>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'Inicio',
  data() {
    return {
      loggedIn: false,
      username: '',
      password: '',
      activeTab: 'Inicio',
      users: [
        { username: 'diegoAmeri', password: '123456', name: 'Diego Ameri', color: 'grey' },
        { username: 'user2', password: 'password2', name: 'Usuario 2', color: 'blue' },
        // Agrega más usuarios aquí con diferentes colores
      ],
      user: null,
    };
  },
  methods: {
    changeTab(tab) {
      this.activeTab = tab;
      if (tab === 'Productos') {
        this.$router.push('/productoLista')
      }
    },
    login() {
      const foundUser = this.users.find(
        (user) => user.username === this.username && user.password === this.password
      );
      if (foundUser) {
        this.user = foundUser;
        this.loggedIn = true;
      } else {
        alert('Credenciales inválidas');
      }
    },
    logout() {
      this.loggedIn = false;
      this.user = null;
    },
  },
};
</script>

<style>
.side-menu {
  background-color: #367888;
  padding: 20px;
}

.side-menu-inner {
  height: 100vh;
}

.side-menu ul {
  list-style-type: none;
  padding: 0;
}

.side-menu ul li {
  cursor: pointer;
  padding: 10px;
}

.side-menu ul li.active {
  background-color: #ddd;
  font-weight: bold;
}
.background {
  background-image: url("~@/img/fondo_inicio.jpg"); /* Agrega el fondo descargado */
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
  padding: 20px;
  height: 100vh;
  position: relative;
  overflow: hidden;
}
.title-text {
  font-family: Arial, sans-serif;
  font-weight: bold;
  color: black;
  font-size: 43px; /* ajusta el tamaño del texto */
  position: absolute; /* posiciona el texto */
  top: 12%; /* ubica el texto a la mitad de la imagen */
  left: 50%; /* ubica el texto a la mitad de la imagen */
  transform: translate(-50%, -50%); /* centra el texto */
}
.login-container {
  background-image: url("~@/img/fondo_login.jpg"); /* Agrega el fondo descargado */
  background-size: cover;
  padding: 20px;
  height: 100vh;
  overflow: hidden;
}

.login-form {
  background: rgba(255, 255, 255, 0.8); /* Fondo de recuadro clarito */
  padding: 20px;
  border-radius: 10px;
}
.small-card {
  max-width: 400px; /* Ajusta el ancho máximo de la tarjeta */
  text-align: center;
}
</style>

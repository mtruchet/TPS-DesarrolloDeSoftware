<template>
  <div class="background-image">
    <br>
    <br>
    <br>
    <b-card class="small-card mx-auto">
      <h1>{{ modo === 'new' ? 'Nuevo Producto' : 'Detalles del Producto' }}</h1>
      <b-input
        v-model="productoDto.name"
        placeholder="Nombre"
        :disabled="modo === 'view'"
      ></b-input>
      <br>
      <b-input
        v-model="productoDto.description"
        placeholder="Descripción"
        :disabled="modo === 'view'"
      ></b-input>
      <br>
      <b-input
        v-model="productoDto.price"
        type="number"
        placeholder="Precio"
        :disabled="modo === 'view'"
      ></b-input>
      <br>
      <b-input
        v-model="productoDto.quantity"
        type="number"
        placeholder="Cantidad"
        :disabled="modo === 'view'"
      ></b-input>
      <br>
      <b-button
        class="custom-button"
        @click="guardarProducto"
        v-if="modo !== 'view'"
      >
        {{ modo === 'new' ? 'Crear Producto' : 'Guardar Cambios' }}
      </b-button>
    </b-card>
    <br>
    <br>
    <br>
    <br>
    <b-row>
      <b-col
        md="auto"
        class="ml-auto"
      >
        <b-button
          class="custom-button"
          @click="redirigirALista()"
        >Volver a la lista de productos</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'
import { BButton } from 'bootstrap-vue'

export default {
  name: 'Producto',
  components: {
    BButton
  },
  props: ['modo', 'idProducto'],
  data: function () {
    return {
      productoDto: {
        nombre: '',
        descripcion: '',
        price: '',
        quantity: ''
      },
    }
  },
  created() {
    if (this.modo !== 'new') {
      this.findById(this.idProducto)
    }
  },
  methods: {
    guardarProducto() {
      if (this.modo === 'new') {
        const nuevoProducto = {
          name: this.productoDto.name,
          description: this.productoDto.description,
          price: this.productoDto.price,
          quantity: this.productoDto.quantity
        }

        axios.post('http://localhost:8080/products', nuevoProducto)
          .then((response) => {
            console.log('Producto creado:', response.data)
          })
          .catch((error) => {
            console.error('Error al crear el producto:', error)
          })
          .finally(() => {
            this.redirigirALista()
          })
      } else {
        axios.put(`http://localhost:8080/products/${this.idProducto}`, this.productoDto)
          .then((response) => {
            console.log('Producto actualizado:', response.data)
          })
          .catch((error) => {
            console.error('Error al actualizar el producto:', error)
          })
          .finally(() => {
            this.redirigirALista()
          })
      }
    },
    redirigirALista() {
      if (this.$router) {
        this.$router.push('/productoLista')
      } else {
        console.error('Router no definido o inexistente.')
      }
    },
    findById(idProducto) {
      axios.get(`http://localhost:8080/products/${idProducto}`)
        .then((response) => {
          this.productoDto = response.data
        })
        .catch((error) => {
          console.error('Error al buscar el producto:', error)
        })
    }
  }
}
</script>
<style>
.small-card {
  max-width: 400px; /* Ajusta el ancho máximo de la tarjeta */
  text-align: center;
}
.background-image,
html,
body,
#app {
  margin: 0;
  padding: 0;
  height: 100%;
}
.background-image {
  background-image: url("~@/img/fondo-lista.jpg");
  background-size: cover;
  padding: 20px;
  height: 100vh;
  margin: 0;
}
</style>

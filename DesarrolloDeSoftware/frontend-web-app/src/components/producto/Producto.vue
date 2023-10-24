<template>
  <div>
    <input v-model="nombre" >
    <br>
    Hola, mi nombre es {{ nombre }}
    <button @click="crearProducto">Crear Producto</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ExampleComponent",
  data: function () {
    return {
      nombre: 'Juan'
    };
  },
  methods: {
    crearProducto () {
      const nuevoProducto = {
        name: this.nombre
        // Otras propiedades del producto
      };

      axios.post("/api/products", nuevoProducto)
        .then((response) => {
          // Maneja la respuesta del backend después de crear el producto
          console.log("Producto creado:", response.data)
        })
        .catch((error) => {
          // Maneja cualquier error
          console.error("Error al crear el producto:", error)
        })
    }
  }
}
</script>

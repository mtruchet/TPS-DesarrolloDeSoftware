<template>
  <div>
    <h1>Lista de Productos Ordenados por Precio</h1>
    <ul>
      <li
        v-for="product in products"
        :key="product.id"
      >
        {{ product.name }} - {{ product.price }}
      </li>
    </ul>
  </div>
</template>

  <script>
  import axios from "axios";

  export default {
    name: "ProductoLista",
    data() {
      return {
        products: [],
      };
    },
    created() {
      axios
        .get("http://localhost:8080/products/sorted-by-price")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error("Error al cargar la lista de productos:", error);
        });
    },
  };
  </script>

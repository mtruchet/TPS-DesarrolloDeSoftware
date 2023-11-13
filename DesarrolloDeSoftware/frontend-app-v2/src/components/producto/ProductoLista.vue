<template>
  <div class="background-image">
    <br>
    <br>
    <b-card>
      <b-row>
        <b-col md="12">
          <h2> <b>Gestión de productos</b></h2>
        </b-col>
      </b-row>
      <br>
      <b-row>
        <b-col md="3">
          <b-form @submit.prevent="onSubmit">
            <b-form-group
              id="frmNombre"
              label="Nombre"
              class="text-left"
            >
              <b-input-group>
                <b-input-group-append>
                  <b-button
                    id="btnClearSearchProducto"
                    v-b-tooltip.hover="'Limpiar filtro'"
                    class="closeStyle"
                    size="sm"
                    @click="()=>clearSearchNombre()"
                  >
                    <font-awesome-icon icon="fa-solid fa-eraser" />
                  </b-button>
                </b-input-group-append>
                <b-form-input
                  id="txtFiltro"
                  v-model="productFilterDto.name"
                  autocomplete="off"
                  placeholder=" Búsqueda por ( Nombre )"
                  maxlength="250"
                />
              </b-input-group>
            </b-form-group></b-form>
        </b-col>
        <b-col md="3">
          <b-form @submit.prevent="onSubmit">
            <b-form-group
              id="frmPrecio"
              label="Precio"
            >
              <b-input-group>
                <b-input-group-append>
                  <b-button
                    id="btnClearSearchProducto"
                    v-b-tooltip.hover="'Limpiar filtro'"
                    class="closeStyle"
                    size="sm"
                    @click="()=>clearSearchPrecio()"
                  >
                    <font-awesome-icon icon="fa-solid fa-eraser" />
                  </b-button>
                </b-input-group-append>
                <b-form-input
                  id="txtFiltro"
                  v-model="productFilterDto.price"
                  autocomplete="off"
                  placeholder=" Búsqueda por ( Precio )"
                  maxlength="250"
                />
              </b-input-group>
            </b-form-group></b-form>
        </b-col>
        <b-col md="3">
          <b-form @submit.prevent="onSubmit">
            <b-form-group
              id="frmDescripcion"
              label="Descripcion"
            >
              <b-input-group>
                <b-input-group-append>
                  <b-button
                    id="btnClearSearchProducto"
                    v-b-tooltip.hover="'Limpiar filtro'"
                    class="closeStyle"
                    size="sm"
                    @click="()=>clearSearchDescripcion()"
                  >
                    <font-awesome-icon icon="fa-solid fa-eraser" />
                  </b-button>
                </b-input-group-append>
                <b-form-input
                  id="txtFiltro"
                  v-model="productFilterDto.description"
                  autocomplete="off"
                  placeholder=" Búsqueda por ( Descripcion )"
                  maxlength="250"
                />
              </b-input-group>
            </b-form-group></b-form>
        </b-col>
        <b-col md="3">
          <b-button
            class="custom-button"
            id="btnSearchProducto"
            v-b-tooltip.hover
            title="Buscar Producto"
            variant="primary"
            size="sm"
            @click="searchProducts()"
          >
            <feather-icon name="search" />
          </b-button>
          <b-button
            class="custom-button"
            @click="redirigirAProducto()"
          >Agregar Producto</b-button>
        </b-col>
      </b-row>
      <br>
      <b-row>
        <b-col
          md="12"
          class="backgraund"
        >
          <b-table
            id="tblProducto"
            ref="refTblProducto"
            :items="tableDataProducto"
            :busy="isWorking"
            :fields="fieldsProducto"
            outlined
            show-empty
            small
            hover
            sticky-header="70vh"
            :no-border-collapse="true"
            empty-text="No existe producto cargado"
            class="styled-table"
          >
            <template v-slot:table-busy>
              <div class="text-center">
                <b-spinner />
              </div>
            </template>
            <template #cell(actions)="row">
              <div
                class="btn-group"
                role="group"
                aria-label="Basic example"
              >
                <b-button
                  size="sm"
                  @click="viewDetalleProducto(row.item, row.index, $event.target)"
                  variant="primary"
                >
                  Ver
                </b-button>
                <b-button
                  size="sm"
                  @click="editDetalleProducto(row.item, row.index, $event.target)"
                  variant="success"
                >
                  Editar
                </b-button>
                <b-button
                  size="sm"
                  @click="deleteDetalleProducto(row.item, row.index, $event.target)"
                  variant="danger"
                >
                  Eliminar
                </b-button>
              </div>
            </template>
          </b-table>
        </b-col>
      </b-row>
      <br>
      <br>
    </b-card>
    <br>
    <br>
    <b-row>
      <b-col
        md="auto"
        class="ml-auto"
      >
        <b-button
          class="custom-button"
          @click="redirigirAInicio()"
        >Redirigir al inicio</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'
import { BButton, BCol, BRow, BTable, BCard } from 'bootstrap-vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import FeatherIcon from 'feather-icons-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { dom } from '@fortawesome/fontawesome-svg-core'

library.add(fas)
dom.watch()

export default {
  name: 'ProductoLista',
  components: {
    FeatherIcon,
    FontAwesomeIcon,
    BRow,
    BCol,
    BTable,
    BButton,
    BCard
  },
  data() {
    return {
      products: [],
      tableDataProducto: null,
      isWorking: false,
      isEditable: false,
      productFilterDto: {
        name: '',
        description: '',
        price: null,
      },
      fieldsProducto: [
        {
          key: 'name', label: 'Nombre', thStyle: { width: '20%' },
        },
        {
          key: 'description', label: 'Descripción', thStyle: { width: '20%' },
        },
        {
          key: 'price', label: 'Precio', thStyle: { width: '20%' },
        },
        {
          key: 'quantity', label: 'Cantidad', thStyle: { width: '20%' },
        },
        { key: 'actions', label: 'Acciones', thStyle: { width: '10%' } },
      ],
    }
  },
  created() {
    this.fetchProducts()

  },
  methods: {
    fetchProducts() {
      axios
        .get('http://localhost:8080/products/sorted-by-price')
        .then((response) => {
          this.tableDataProducto = response.data
        })
        .catch((error) => {
          console.error('Error al cargar la lista de productos:', error)
        })
    },
    searchProducts() {
      if (this.productFilterDto.price === null) {
        this.productFilterDto.price = 0
        this.productFilterDto.name = null
        this.productFilterDto.description = null
      }
      if (this.productFilterDto.name === "") {
        this.productFilterDto.name = null
      }
      if (this.productFilterDto.description === "") {
        this.productFilterDto.description = null
      }
      axios.post('http://localhost:8080/products/searchProduct', this.productFilterDto)
        .then(response => {
          this.tableDataProducto = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    redirigirAProducto() {
      if (this.$router) {
        this.$router.push('/producto/new')
      } else {
        console.error('Router no definido o inexistente.')
      }
    },
    redirigirAInicio() {
      if (this.$router) {
        this.$router.push('/')
      } else {
        console.error('Router no definido o inexistente.')
      }
    },
    editDetalleProducto(item) {
      if (this.$router) {
        this.$router.push(`/producto/edit/${item.id}`)
      } else {
        console.error('Router no definido o inexistente.')
      }
    },
    viewDetalleProducto(item) {
      if (this.$router) {
        this.$router.push(`/producto/view/${item.id}`)
      } else {
        console.error('Router no definido o inexistente.')
      }
    },
    deleteDetalleProducto(item) {
      axios.delete(`http://localhost:8080/products/${item.id}`)
        .then((response) => {
          console.log('Producto eliminado:', response.data)
        })
        .catch((error) => {
          console.error('Error al eliminar el producto:', error)
        })
        .finally(() => {
          this.fetchProducts()
        })
    },
    clearSearchNombre() {
      this.productFilterDto.name = ''
    },
    clearSearchDescripcion() {
      this.productFilterDto.description = ''
    },
    clearSearchPrecio() {
      this.productFilterDto.price = ''
    },
  }
}
</script>

<style>
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

.custom-button {
  border: 1px solid #333;
  padding: 10px 20px;
  transition: all 0.3s ease;
}

.custom-button:hover {
  cursor: pointer;
  background-color: #f0f0f0;
}

.styled-table {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.backgraund {
  background-color: #effdff;
}
</style>

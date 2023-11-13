import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'inicio',
    component: () => import('../components/producto/Inicio.vue'),
    meta: {
      nameParent: 'inicio',
    },
  },
  {
    path: '/productoLista',
    name: 'producto',
    component: () => import('../components/producto/ProductoLista.vue'),
    meta: {
      nameParent: 'producto',
    },
  },
  {
    path: '/producto/:modo/:idProducto',
    name: 'producto-mode',
    component: () => import('../components/producto/Producto.vue'),
    props: route => ({
      modo: route.params.modo,
      idProducto: route.params.idProducto
    }),
    meta: {
      nameParent: 'producto'
    }
  },
  {
    path: '/producto/edit/:idProducto',
    name: 'producto-edit',
    component: () => import('../components/producto/Producto.vue'),
    props: route => ({ idProducto: route.params.idProducto }),
    meta: {
      nameParent: 'producto',
    },
  },
  {
    path: '/producto/new',
    name: 'producto-new',
    component: () => import('../components/producto/Producto.vue'),
    props: () => ({
      modo: 'new'
    }),
    meta: {
      nameParent: 'producto',
    },
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router

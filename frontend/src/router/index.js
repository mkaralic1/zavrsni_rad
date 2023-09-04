import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/destinacije',
    name: 'destinacije',
    component: () => import('@/views/DestinationView.vue')
  },
  {
    path: '/registracija',
    name: 'registracija',
    component: () => import('@/views/RegistrationView')
  },
  {
    path: '/prijava',
    name: 'prijava',
    component: () => import('@/views/LoginView')
  },
  {
    path: '/dodaj',
    name: 'dodaj',
    component: () => import('@/views/AddPostsView')
  },
  {
    path: '/recenzije',
    name: 'recenzije',
    component: () => import('@/views/SeePostsView')
  },
  {
    path: '/moj_profil',
    name: 'moj_profil',
    component: () => import('@/views/ProfileView')
  },
  {
    path: '/editpost/:postId',
    name: 'EditMyPostView',
    component: () => import('@/views/EditMyPostView')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

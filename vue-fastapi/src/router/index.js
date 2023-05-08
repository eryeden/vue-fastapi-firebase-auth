import { createRouter, createWebHistory } from 'vue-router'
import Top from '../components/Top.vue'
import Api from '../components/Api.vue'

import FirebaseAuthUI from  '../components/FirebaseAuthUI.vue'

import { getAuth, onAuthStateChanged } from "firebase/auth";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'top',
      component: Top
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/login',
      name: 'login',
      component: FirebaseAuthUI
    },
  ]
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const isLoginPage = to.matched.some(record => (record.name==="login"))
  const auth = getAuth();

  if (requiresAuth) {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        // The user is already logged in, so that the page will be redirected to the restricted area.
        next()
      } else {
        // User is signed out
        // User will be redirected to the sign-in page
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      }
    });
  } else if(isLoginPage){
    onAuthStateChanged(auth, (user) => {
      if (user) {
        // The user is already logged in, so that the page will be redirected to the top page.
        next({
          path: '/',
          query: { redirect: to.fullPath }
        })
      } else {
        // User is signed out
        // User will be redirected to the sign-in page.
        next()
      }
    });
  }
  else {
    next()
  }
})

export default router

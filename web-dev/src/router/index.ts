import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "game",
      component: () => import("../views/game/JockpokView.vue"),
    },

    {
      path: "/home",
      name: "home",
      component: () => import("../views/home/HomeView.vue"),
    },

    //
  ],
});

export default router;

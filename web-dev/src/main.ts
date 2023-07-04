import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/main.css";
// import service from "./config/api.js";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

import { createPinia } from "pinia";
import mitt from "mitt";
import VueKinesis from "vue-kinesis";
import VuePrlx from "vue-prlx";
// Vue.config.productionTip = false
// Vue.prototype.Web3 = Web3

// import "vform3-builds/dist/designer.style.css";
import service from "./config/api.js";
const app = createApp(App);
const pinia = createPinia();
const emitter = mitt();

app.use(router);
// app.use(initVueI18n("zh_cn"));
app.use(pinia);
app.use(VueKinesis);
app.use(VuePrlx);
app.use(ElementPlus);
app.provide("emitter", emitter);
app.mount("#app");
app.config.globalProperties.$axios = service;
// app.config.globalProperties.$axios = service;


import Axios from "axios"; //引入service
import qs from "qs"; //引入service数据处理
import { ElMessage } from "element-plus";

const service = Axios.create({
  timeout: 10000,
  // baseURL: "http://127.0.0.1:8000/",
   withCredentials: true
});

// 添加一个响应拦截器
service.interceptors.request.use(
  (config) => {
    config.headers["Access-Control-Allow-Origin"] = "*";
    config.headers["Accept-Language"] = "";
    config.headers["Content-Type"] =
      "application/x-www-form-urlencoded; charset=UTF-8;application/json";
    config.headers["Accept-xsrfCookieName"] = "csrftoken";
    config.headers["xsrfHeaderName"] = "X-CSRFTOKEN";
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    const regex = /.*csrftoken=([^;.]*).*$/
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
     
    const usrdata = JSON.parse(localStorage.getItem("userData"));
    if (config.method === "post") {
      if (usrdata != null) {
        config.data = Object.assign(config.data || { token: usrdata["token"] });
      }
      config.data = qs.stringify(config.data);
    }
    if (config.method === "get") {
      if (usrdata != null) {
        config.params = Object.assign(
          config.params || { token: usrdata["token"] }
        );
      }
      config.params = Object.assign(config.params || {});
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
// 结束
// 添加返回信息验证
service.interceptors.response.use(
  function (response) {
    if (response.data.status == 201) {
      return null;
    } else if (response.data && response.data.status == 500) {
      ElMessage(response.data.msg);
    } else if (response.data && response.data.msg) {
      ElMessage(response.data.msg);
    }
    return response.data.data;
  },
  function (error) {
    console.log(error);
    return Promise.reject(error);
  }
);

export default service;

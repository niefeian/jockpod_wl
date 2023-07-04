import axios from "axios";

const login = (para: any) => {
  return axios.get(getApiUrl("login", para));
};

const verify_correct = (para: any) => {
  return axios.get(getApiUrl("verify_correct", para));
  // return axios.get("verify_correct" + getUrl(para), {});
};

const get_balances = (para) => {
  return axios.get(getApiUrl("balances",para));
  // return axios.get("balances", {});
};

const balances_no = (para) => {
  return axios.get(getApiUrl("balances_no",para));
  // return axios.get("balances", {});
};

// 
const silent_login = (para) => {
  return axios.get(getApiUrl("silent_login", para));
  // return axios.post("silent_login", {});
};

const will_betting = (para) => {
  return axios.get(getApiUrl("will_betting", para));
  // return axios.post("silent_login", {});
};

// 
const getApiUrl = (url, para: any) => {
  return "http://8.219.144.203:4999/" + url + getUrl(para);
};


const getUrl = (para: any) => {
  let url_str = "?";
  for (const key in para) {
    if (Object.prototype.hasOwnProperty.call(para, key)) {
      const element = para[key];
      url_str += key + "=" + element + "&";
    }
  }
  return url_str;
};

export { login, verify_correct, silent_login, get_balances ,will_betting,balances_no};

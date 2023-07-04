/**
 * 时间格式 普通时间戳转换时间
 * @param value 时间戳
 */

const timeStamp_day = (value: any) => {
  return new Date(value.format("YYYY-MM-DD HH:mm:ss")).getTime();
};

const formatTs = (ts: number) => {
  const date = new Date(ts);
  const y = date.getFullYear();
  const m = "0" + (date.getMonth() + 1);
  const d = "0" + date.getDate();
  const h = "0" + date.getHours();
  const min = "0" + date.getMinutes();
  const s = "0" + date.getSeconds();
  return (
    y +
    "-" +
    m.substring(m.length - 2, m.length) +
    "-" +
    d.substring(d.length - 2, d.length) +
    " " +
    h.substring(h.length - 2, h.length) +
    ":" +
    min.substring(min.length - 2, min.length) +
    ":" +
    s.substring(s.length - 2, s.length)
  );
};

const change_num = (a: number, b: number) => {
  if (a >= b) {
    return (a - b).toString;
  } else {
    return "-" + (b - a).toString;
  }
};

// const change_percent = (a, b) => {
//   if (!(a != undefined && b != undefined)) {
//     return "0%";
//   }
//   if (a >= b) {
//     return (((a - b) * 100) / b).toString() + "%";
//   } else {
//     return "-" + (((b - a) * 100) / b).toString() + "%";
//   }
// };

// const open_new_window = (url) => {
//   window.open(url, "_blank");
// };

// const open_new_eth_window = (url) => {
//   open_new_window("https://etherscan.io/address/" + url);
// };

export { timeStamp_day, formatTs, change_num };

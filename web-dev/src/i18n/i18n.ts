import { createI18n } from "vue-i18n";

import langs from "./index";

function initVueI18n(lang = "zh_cn") {
  return createI18n({
    legacy: false,
    locale: lang,
    messages: langs,
  });
}

export default initVueI18n;

<template>
  <div v-if="!is_login" class="user_icon" @click="onSubmit">Sign In</div>
  <img v-if="is_login" src="../../assets/user__easyico.png" class="user_icon_img" @click="toUserInfo" />
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { login, silent_login } from "@/api/Wallet";
import MetaMaskOnboarding from "@metamask/onboarding";
const onboarding = new MetaMaskOnboarding();
const is_login = ref(false);
const userData = ref({});
const toUserInfo = () => { };

onMounted(() => {

  var usrdata = JSON.parse(sessionStorage.getItem("userData"));
  if (usrdata != null) {
    silent_login({ token: usrdata["token"] }).then(res => {
      if (res.data['status'] == "success") {    
          userData.value = res;
          is_login.value = true;
      }
    })
  }

});

const onSubmit = () => {
  if ((window as any).ethereum && (window as any).ethereum.isMetaMask) {
    return (window as any).ethereum
      .request({ method: "eth_requestAccounts" })
      .then((res: any) => {
        initEthereum();
        return res;
      });
  } else {
    onboarding.startOnboarding();
    window.open("https://metamask.io/", "_blank");
    return Promise.resolve([]);
  }
};

const initEthereum = (wcInfo?: { chainId: number; accounts: string[] }) => {
  if ((window as any).ethereum) {
    const { ethereum } = window as any;
    Promise.all([
      ethereum.request({ method: "eth_accounts" }),
      ethereum.request({ method: "eth_chainId" }),
    ])
      .then(([accounts = [], chainId = ""]) => {
        login({ address: accounts[0], chain: chainId }).then((res) => {
          if (res != null) {
            userData.value = res.data['data'];
            is_login.value = true;
            sessionStorage.setItem("userData", JSON.stringify(res.data['data']));
          }
        });
        
      })
      .finally(() => { });
    return;
  }
};
</script>

<style>
.user_icon {
  width: 80px;
  height: 40px;
  left: 90%;
  top: 10px;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 40px;
}

.user_icon_img {
  width: 80px;
  width: 80px;
  left: 90%;
  top: 10px;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  line-height: 40px;
}
</style>

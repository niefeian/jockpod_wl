<template>
  <el-button type="primary" @click="onSubmit">链接钱包</el-button>
  <el-button type="primary" @click="onSubmit2">获取信息</el-button>
</template>

<script lang="ts" setup>
import { login } from "@/api/Wallet";
import * as AleoWalletBase from "@demox-labs/aleo-wallet-adapter-base";
import * as LeoWallet from "@demox-labs/aleo-wallet-adapter-leo";
var wallet = new LeoWallet.LeoWalletAdapter({ appName: "JockPoK" });
const onSubmit = () => {
  wallet
    .connect(
      AleoWalletBase.DecryptPermission.AutoDecrypt,
      AleoWalletBase.WalletAdapterNetwork.Testnet
    )
    .then(() => {
      let utf8Encode = new TextEncoder();
      let bytes = utf8Encode.encode("登录Leo");
      wallet.signMessage(bytes).then((res) => {
        console.log(wallet);
        const form = {
          address: wallet.publicKey,
          name: wallet.name,
          chain: AleoWalletBase.WalletAdapterNetwork.Testnet,
        };
        login(form).then((res) => {});
      });
    });
};
const onSubmit2 = () => {
  let res = wallet.requestViewKey();
  console.log(res);
};
</script>

<style lang="scss"></style>

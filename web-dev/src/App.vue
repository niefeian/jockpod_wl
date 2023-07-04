<template>
  <el-container>
    <el-container>
      <el-header>
        <head-view></head-view>
      </el-header>
      <el-main> <router-view></router-view></el-main>
    </el-container>
  </el-container>
</template>

<script lang="ts" setup>
import HeadView from "./components/head/HeadView.vue";
</script>

<style scoped>
html,
body,
#app,
.el-container {
  /*设置内部填充为0，几个布局元素之间没有间距*/
  padding: 0px;
  /*外部间距也是如此设置*/
  margin: 0px;
  /*统一设置高度为100%*/
  height: 100vh;
  background: #feecd4;
}

.el-header {
  align-content: left;
  color: rgb(186, 170, 170);
  text-align: left;
}
</style>

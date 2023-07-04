<template>
  <div style="width: 70%;text-align: center;height: 80px;font-weight: bold;">
    Jackpot {{ balances.all_balance }},
    Your Balance {{ balances.balance }}</div>
  <div class="box-view">
    <div class="slot-machine">
      <button class="start_btn" @click="wstart"></button>
      <div class="slot" v-for="(slot, index) in slots" ref="slots" :key="`${index}}`">
        <div class="slot__window">
          <div class="slot__wrap">
            <div class="slot__item" v-for="(opt, idx) in slots[0].items" :key="`${index}_${idx}`">
              <img class="slot__item_content" :src="`${opt}`" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box-view2">
      <img src="@/images/rule.png" style=" width: 400px;" />
    </div>
  </div>
</template>
<script>
import { onMounted, ref } from "vue";
import { verify_correct, get_balances, will_betting, balances_no } from "@/api/Wallet";
const next =
  window.requestAnimationFrame ||
  window.webkitRequestAnimationFrame ||
  window.mozRequestAnimationFrame ||
  window.msRequestAnimationFrame ||
  window.oRequestAnimationFrame ||
  function (cb) {
    window.setTimeout(cb, 1000 / 60);
  };
export default {
  data() {
    return {
      slots: [
        {
          title: "When",
          items: [
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
          ],
        },
        {
          title: "Where",
          items: [
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
          ],
        },
        {
          title: "How",
          items: [
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/1.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/2.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/3.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/4.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/5.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/6.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/7.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/8.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/9.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/10.png",
            "http://glinkcdn.oss-ap-southeast-1.aliyuncs.com/jokpod/11.png",
          ],
        },
      ],
      prizeNum: 3, // 可视区域每列展示的奖品数
      opts: null,
      startedAt: null,
      correctQty: 500,
      choices_: [],
      balances: { all_balance: 10000, balance: 500 }
    };
  },
  // onMounted
  mounted() {
    setTimeout(() => {
      this.getBalances()
    }, 1000);

  },

  methods: {

    getBalances: function () {
      var usrdata = JSON.parse(sessionStorage.getItem("userData"));
      if (usrdata != null) {
        get_balances({ token: usrdata["token"] }).then(res => {
          if (res.data['status'] == "success") {
            this.balances = res.data['data']
          }
        })
      } else {
        // balances_no({}).then(res => {
        //   if (res.data['status'] == "success") {
        //     this.balances = res.data['data']
        //   }
        // })
      }

    },
    wstart: function () {
      // if (this.data.balances['balance'] >= 10){
      var usrdata = JSON.parse(localStorage.getItem("userData"));
      if (usrdata == null) {
        this.start([1, 2, 3])
      } else {
        will_betting({ token: usrdata["token"] }).then(res => {
          if (res.data['status'] == "success") {
            this.start(res.data['data'])
          }
        })
      }

    },
    start: function (arr) {
      if (this.correctQty < 10) {
        return;
      }
      if (this.opts) {
        // 增加动画过程中，再次点击开始，立即结束动画，且置为对应中将位置
        this.opts.forEach((opt) => {
          opt.isFinished = true;
          const pos = -opt.finalPos;
          opt.el.style.transform = "translateY(" + pos + "px)";
        });
        return;
      }
      var choices = [Math.random() * 15 + 5, Math.random() * 15 + 5, Math.random() * 15 + 5];

      this.opts = this.slots.map((data, i) => {
        const slot = this.$refs.slots[i]; // map(function(){})利用map便利slots的每一个选项组,最终得到return的返回值
        const itemHeight =
          document.getElementsByClassName("slot__item")[0].offsetHeight;
        const choice = arr[i]; // 随机生成一个[0,data.items.length]的整数(floor向下取整)
        const opts = {
          el: slot.querySelector(".slot__wrap"), //指向奖项元素的父级
          finalPos: choice * itemHeight, // itemHeight 为每一个奖品滚动标签的高度
          startOffset: 1000 + Math.random() * 500 + i * 500, // 影响转的圈数
          height: data.items.length * itemHeight,
          duration: 3000 + i * 700, // milliseconds
          isFinished: false,
        };
        choices[i] = choice % 11;
        return opts;
      });

      this.choices_ = choices;
      next(this.animate); // 开启动画
    },
    animate: function (timestamp) {
      if (!this.opts) return;
      // timestamp当前的方法持续的毫秒数
      if (this.startedAt == null) {
        this.startedAt = timestamp; // 动画初始时间
      }
      const timeDiff = timestamp - this.startedAt; //动画持续的时间
      // console.log(timestamp, this.opts);
      this.opts.forEach((opt) => {
        if (opt.isFinished) {
          return;
        }
        const timeRemaining = Math.max(opt.duration - timeDiff, 0); // 总的持续时间 - 动画持续时间 = 剩下的时间,0表示结束
        const power = 3;
        const offset =
          (Math.pow(timeRemaining, power) / Math.pow(opt.duration, power)) *
          opt.startOffset; // Math.pow(timeRemaining, power)表示: timeRemaining 的3 次幂; // negative, such that slots move from top to bottom
        const pos = -1 * Math.floor((offset + opt.finalPos) % opt.height);
        opt.el.style.transform = "translateY(" + pos + "px)";
        if (timeDiff > opt.duration) {
          opt.isFinished = true;
        }
      });
      if (this.opts.every((o) => o.isFinished)) {
        if (
          this.choices_[0] == this.choices_[1] &&
          this.choices_[1] == this.choices_[2]
        ) {
          this.correctQty = this.correctQty + 1000 - 10;
        } else {
          this.correctQty = this.correctQty - 10;
        }
        var usrdata = JSON.parse(localStorage.getItem("userData"));
        if (usrdata != null) {
          verify_correct({
            num1: this.choices_[0],
            num2: this.choices_[1],
            num3: this.choices_[2],
            amount: this.correctQty,
            token: usrdata["token"]
          }).then(res => {
            this.getBalances()
          });
        } else {
          let rate = [30, 20, 100, 30, 10, 50, 20, 50, 10, 5, 5]
          let ix = this.choices_[0] % 11
          let ix1 = this.choices_[1] % 11
          let ix2 = this.choices_[2] % 11
          if (ix == ix1 && ix1 == ix2) {
            this.balance.all_balance = this.balance.all_balance - 10 * rate
            this.balances.balance = this.balances.balance + 10 * rate
          } else {
            this.balance.all_balance = this.balance.all_balance + 10 
            this.balances.balance = this.balances.balance - 10
          }
          this.opts = null;
          this.startedAt = null;
        }
       } else {
        next(this.animate);
      }
    },
  },
};
</script>
<style scoped>
.slot-machine {
  background: url("../../images/main2.png") no-repeat;
  height: 689px;
  width: 1200px;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}

.slot {
  float: left;
  margin: 0.4em;
}

.slot__window {
  left: 50px;
  top: 55px;
  width: 140px;
  height: 190px;
  overflow: hidden;
}

.slot__item {
  padding-top: 40px;
  width: 130px;
  height: 100px;
  left: 10px;
}

.slot__item_content {
  width: 120px;
  height: 100px;
  text-align: center;
  color: white;
  top: -100px;
}

.start_btn {
  width: 300px;
  height: 100px;
  top: 300px;
  left: -330px;
  opacity: 0;
  /* background: red; */
}

.box-view2 {
  width: 400px;
  padding-right: 50px;
}

.box-view {
  /* width: 100vw; */
  display: flex;
  flex-direction: row;
  padding-left: 50px;

}

.main2-text2 {
  font-size: 23px;
  font-weight: bold;
}

.main2-text4 {
  color: #000000;
  font-size: 18px;
}

.main2 {
  color: red;
  font-size: 28px;
  font-weight: bold;
  text-align: center;
  width: 300px;
}
</style>

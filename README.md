# jockpod_wl.aleo

## Build Guide

To compile this Aleo program, run:
```bash
aleo build
```

 token => {
    owner: address,
    gates: u64,
    amount: u64,
}

 Lottery   => {
    owner: address,
    gates: u64,
    amount: u64,
    lottery_money:u64,
    c1: u64,
    c2: u64,
    c3: u64,
}

  Transfer  => {
    owner: address,
    gates: u64,
    from_address: address,
    to_address: address,
    money: u64,
}

<!-- 增加筹码 -->
leo run increase_public 'address' 'amount'
<!-- 扣除投注金额 减少筹码 -->
leo run reduce_public 'address' 'amount'
<!-- 校验开奖信息  -->
leo run transfer_lottery 'from_address' 'dealer' 'money' 'lottery_money' 'c1' 'c2' 'c3'
<!-- 完成游戏，进行转账 -->
leo run transfer_accounts

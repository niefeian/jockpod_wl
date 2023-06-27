// The 'jockpod_wl' program.
program jockpod_wl.aleo {

    mapping balances: address => u64;

    record token {
        owner: address,
        gates: u64,
        amount: u64,
    }

    record Lottery {
        owner: address,
        gates: u64,
        amount: u64,
        lottery_money:u64,
        c1: u64,
        c2: u64,
        c3: u64,
    }

     record Transfer {
        owner: address,
        gates: u64,
        from_address: address,
        to_address: address,
        money: u64,
    }

   transition main(public a: u32, b: u32) -> u32 {
        let c: u32 = a + b;
        return c;
    }

    transition increase_public(
        public receiver: address,
        public amount: u64,
    ) -> token {
        return token {
            owner: receiver,
            gates: 0u64,
            amount,
        } then finalize(receiver, amount);
    }

    finalize increase_public(
        public receiver: address,
        public amount: u64,
    ) {
        let current_amount: u64 = Mapping::get_or_use(balances, receiver, 0u64);
        Mapping::set(balances, receiver, current_amount + amount);
    }

    transition reduce_public(
        public receiver: address,
        public amount: u64,
    ) -> token {
        return token {
            owner: receiver,
            gates: 0u64,
            amount,
        } then finalize(receiver, amount);
    }


    finalize reduce_public(
        public receiver: address,
        public amount: u64,
    ) {
        let current_amount: u64 = Mapping::get_or_use(balances, receiver, 0u64);
        Mapping::set(balances, receiver, current_amount - amount);
   }

    // 校验开奖信息
    transition transfer_lottery(from_address: address ,dealer:address , money:u64 ,lottery_money: u64 , c1: u64 , c2 : u64 , c3: u64 ) -> Lottery {
        return Lottery {
            owner: from_address,
            gates: 0u64,
            amount: money,
            lottery_money:lottery_money,
            c1: c1,
            c2: c2,
            c3: c3,
        };
    }


// 谁转给谁
    transition transfer_accounts(public from_address: address, public to_address: address ,public money:u64) -> Transfer {
        // transfer(from_address,to_address,money);
        return Transfer {
            owner:from_address,
            gates:0u64,
            from_address: from_address,
            to_address: to_address,
            money: money,
        } then finalize(from_address, to_address , money);
    }
    
    finalize transfer_accounts(
        public from_address: address, 
        public to_address: address ,
        public money:u64
    ) {
        let current_amount: u64 = Mapping::get_or_use(balances, from_address, 0u64);
        Mapping::set(balances, from_address, current_amount - money);

        let current_amount2: u64 = Mapping::get_or_use(balances, to_address, 0u64);
        Mapping::set(balances, to_address, current_amount2 + money);
   }




}

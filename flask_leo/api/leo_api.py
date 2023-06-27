import os

from fastapi import FastAPI,Request
from utils.n_string import md5
from utils.n_time import get_time_stamp
from utils.sql.sql_tools import sql_table_one, install_table, update_table,del_table_
from run_leo import import_leo_program, Account
import random




balances = ''

# 获取一个账户
def getAccount(path):
    if os.path.exists(path):
        acc2 = Account.load(path)
        if acc2:
            return acc2
    acc = Account.new()
    install_table('jok_conis', [acc.address,0], ['address','blance'])
    acc.save(path)
    return acc
# ./../address/
def getAccountBy(name):
    return getAccount('./address/' + name + '.txt')

def run_leo_program(acc_path,program_path):
    # Import the Leo program from a specific directory
    leo_program = import_leo_program(program_path)()
    # set the account use for leo program
    acc = getAccount(acc_path)
    return  [leo_program,acc]

def get_leo_program():
    return import_leo_program('./../leo_program/jockpod_wl')()

# 转币
def transfer_accounts(from_address, to_address,money):
    leo_program = get_leo_program()
    return leo_program.transfer_accounts(from_address,to_address,money)

# 下注
def transfer_betting(from_address,money):
    leo_program = get_leo_program()
    return leo_program.transfer_accounts(from_address,getAccountBy('main').address,money)

# 是否中奖
def transfer_lottery(from_address,money,c1,c2,c3):
    leo_program = get_leo_program()
    return leo_program.transfer_lottery(from_address, money, c1,c2,c3)

def getBalancemain():
    row = sql_table_one('jok_conis', [getAccountBy('main')], ['address'])
    if not row:
        return 0
    return row['blance']

def login_success(data,request):
    token = md5(data['m_address'])
    data['token']  = token
    update_logs(token,data,request)
    if data['private_key']:
        data['private_key'] = None
    if data['view_key']:
        data['view_key'] = None
    return OK(data,"登录成功")
        # {"status":200,"msg":"登录成功","data":data}

def OK(data,msg=""):
    return {'status': 'success', "msg": msg, "data": data}

def Error(msg=""):
    return {"status":201,"msg":msg}

def c_web_user(by_name,chain):
    user_id = install_table("user", [by_name, md5(by_name)], ["user_name", "user_password"])
    user_leo = getAccountBy(by_name)
    install_table("user_aleo",
                  [by_name, chain, user_id, user_leo.private_key, user_leo.view_key, user_leo.address],
                  ["m_address", "chain_id", "user_id", "private_key", "view_key", "address"])
    user_web = sql_table_one("user_aleo", [user_id], ["user_id"])
    return user_web

#  根据 ip 自动生成一个账号

def silent_login(token):
    # host = request.client.host
    # ,"order by update_time desc"
    user_logs = sql_table_one("user_logs", [token], ["token"])
    if user_logs:
        user_web = sql_table_one("user_aleo", [user_logs['user_id']], ["user_id"])
        if  user_web:
            res = sql_table_one("jok_conis", [user_web['address']], ["address"])
            user_web['blance'] = res['blance']
            return login_success(user_web, None)
    return Error("请登录")


def getAleoUser(token):
    user_logs = sql_table_one("user_logs", [token], ["token"])
    aleo_user = sql_table_one("user_aleo", [user_logs['user_id']], ["user_id"])
    return aleo_user

def deljok_pod(address:str):
    del_table_('jok_pod',[address],['address'])

# will_betting 点击下注先调用这个返回最后中奖数据
# betting 下注
# verify_correct 兑奖
def update_conis(for_address: str,to_address: str,amount: int):
    row = sql_table_one('jok_conis', [for_address], ['address'])
    if row:
        update_table('jok_conis',{'blance':  row['blance'] - amount},{'address':for_address})
    row2 = sql_table_one('jok_conis', [to_address], ['address'])
    if row2:
        update_table('jok_conis', {'blance': amount + row2['blance']}, {'address': to_address})

def getBalance(token):
    mainadd = getAccountBy('main').address
    row = sql_table_one('jok_conis', [mainadd], ['address'])
    ab = getAleoUser(token)
    a = ab['address']
    row2 = sql_table_one('jok_conis', [a], ['address'])
    if not row:
        return OK({'all_balance': 0, 'balance': row2['blance']})
    return OK({'all_balance':row['blance'],'balance':row2['blance']})


def getBalanceNo():
    mainadd = getAccountBy('main').address
    row = sql_table_one('jok_conis', [mainadd], ['address'])
    if not row:
        return OK({'all_balance': 0, 'balance': 0})
    return OK({'all_balance':row['blance'],'balance':0})

def login(address,chain,request):
    user_web = sql_table_one("user_aleo", [address,chain], ["m_address","chain_id"])
    if not user_web:
        user_web = c_web_user(address,chain)
    # res  = sql_table_one("jok_conis", [user_web['address']], ["address"])
    # user_web['blance'] = res['blance']
    return login_success(user_web,request)



def will_betting(token: str,amount: int):
    deljok_pod(getAleoUser(token)['address'])
    arr = calculate_numbers(amount,0)
    arr1 = arr[0]
    first_num = arr1[0]
    tow_num = arr1[1]
    three_num = arr1[2]
    lottery_money = arr[1]
    install_table('jok_pod',[getAleoUser(token)['address'],amount,first_num,tow_num,three_num,lottery_money],['address','amount','first_num','tow_num','three_num','lottery_money'])
    return OK(arr1)

# 下注
def betting(token: str,
    amount: int):
    update_table("user_aleo",{"u_integral":amount},{"m_address":'"' + bidder + '"'})
    update_conis(getAleoUser(token)['address'],getAccountBy('main').address,amount);
    transfer_betting(getAleoUser(token)['address'],amount)
    # execute("leo_api_wlyz"," verify_correct ",str(amount) + "u64  " ,
    #         "APrivateKey1zkp1xUzL8FgxFjs6yWAopHFbk4tn6Uz7Qc6sDSDq1DUggQJ","0",record_plaintext)
    return OK({"address": getAleoUser(token)['address'], "amount": amount})

# 校验结果

def verify_correct(token: str,amount: int):
    bidder = getAleoUser(token)['address']
    row = sql_table_one('jok_pod',[bidder],['address'])
    if row :
        # num1 = row['first_num']
        # num2 = row['tow_num']
        # num3 = row['three_num']
        lottery_money = row['lottery_money']
        if lottery_money > 0:
            update_conis(getAccountBy('main').address,bidder,  lottery_money);
        else:
            update_conis( bidder,getAccountBy('main').address, 10);
    else:
        will_betting(token,amount)
        return verify_correct(token,amount)

    # update_table("user_aleo", {"u_integral": amount}, {"m_address": '"' + bidder + '"'})
    # transfer_lottery(bidder,amount,lottery_money,num1,num2,num3)
    # execute("leo_api_wlyz"," verify_correct ",str(amount) + "u64  " ,
    #         "APrivateKey1zkp1xUzL8FgxFjs6yWAopHFbk4tn6Uz7Qc6sDSDq1DUggQJ","0",record_plaintext)
    return OK({"address": bidder, "amount": amount})


def update_logs(token,user, request):
    user_logs = sql_table_one("user_logs", [token], ["token"])
    if user_logs:
        update_table("user_logs", {'update_time': get_time_stamp(), 'login_num': user_logs['login_num'] + 1},
                     {'token': token})
    else:
        # if request:
        #     install_table("user_logs",
        #               [user["user_id"], get_time_stamp(), get_time_stamp(), request.client.host, token, 0], ["user_id", "create_time", "update_time", "ip", "token", "login_type"])
        # else:
        install_table("user_logs",
                      [user["user_id"], get_time_stamp(), get_time_stamp(), "127.0.0.1", token, 0]
                      , ["user_id", "create_time", "update_time", "ip", "token", "login_type"]
                      )

def calculate_numbers(amount,i):
    arr = []
    for i  in range(3):
        arr.append(random.randint(0, 11));
    b =  getBalancemain()
    if get_rate(arr) * amount > b:
        return calculate_numbers(amount,i+1)
    elif get_rate(arr) * amount > b *0.6 and i < 10:
        return calculate_numbers(amount,i+1)
    elif get_rate(arr) * amount > b *0.4 and i < 5:
        return calculate_numbers(amount,i+1)
    else:
        return [arr,get_rate(arr) * amount]

rate = [30,20,100,30,10,50,20,50,10,5,5]
def get_rate(arr):
    if arr[0] == arr[1] and arr[2] == arr[1]:
       return rate[arr[0]%11]
    return 0

#
# getAccountBy('main')
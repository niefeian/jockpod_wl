from config.aleo_config import get_leo_bin, get_snarkos_bin, get_aleo_bin
from utils.shell_utils import os_popen, subprocess_popen


def execute(app_name,api_name,para,private_key , fee , record):
    leo_shell = get_snarkos_bin() + ' developer execute "' + app_name \
              +'.aleo"  ' + api_name  + para + ' --private-key "'+ private_key \
              +'" --query "https://vm.aleo.org/api" --broadcast "https://vm.aleo.org/api/testnet3/transaction/broadcast" --fee '\
              + str(fee) +' --record "' +record +'"'
    res = subprocess_popen(leo_shell)
    return  res


def account_new():
    leo_shell = get_aleo_bin() + ' account new '
    return os_popen(leo_shell)

def account_new_json():
    res = account_new()
    print(res)
    for i in range(len(res)):
        striing = res[i]
        if "Private" in striing:
            private_key = res[i].split(" ")[4]
        elif "View" in striing:
            view_key = res[i].split(" ")[4]
        elif "Address" in striing:
            address = res[i].split(" ")[3]
    print([private_key,view_key,address])
    return  [private_key,view_key,address]

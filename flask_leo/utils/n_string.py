import string
import time
import base64
import hmac
import hashlib
from random import random


def md5(key):
    return hashlib.md5(key.encode(encoding='utf-8')).hexdigest()

def md5_list(list):
    m = hashlib.md5()
    for i in range(len(list)):
        key = str(list[i])
        m.update(key.encode('utf-8'))
    return m.hexdigest()

def string_type(string):
    if isinstance(string, int):
        return str(string)
    else:
        return str(string)

def map_str(map,sp=',',eq='='):
    string = ''
    for k,v in map.items():
        if string != '':
            string += sp
        string += k + eq + string_type(v)
    return  string

def str_map(string,sp=',',eq='='):
    if not string:
        return
    arr = string.split(sp)
    return  {i.split(eq)[0]: i.split(eq)[1] for i in arr}

def str_list(string,sp=','):
    return  string.split(sp)

def list_str(list,sp=','):
    return  sp.join(list)

# 生成32位随机字符串
def randomStr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 32))



def generate_token(key, expire=360000):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")

def certify_token(key, token):
 token_str = base64.urlsafe_b64decode(token).decode('utf-8')
 token_list = token_str.split(':')
 if len(token_list) != 2:
    return False
 ts_str = token_list[0]
 if float(ts_str) < time.time():
     return False
 known_sha1_tsstr = token_list[1]
 sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
 calc_sha1_tsstr = sha1.hexdigest()
 if calc_sha1_tsstr != known_sha1_tsstr:
    return False
 return True

def test():
    key = "JD98Dskw=23njQndW9D"
    token = generate_token(key, 3600)
    certify_token(key, token)


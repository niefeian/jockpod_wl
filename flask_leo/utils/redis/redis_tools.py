import numpy as np
import redis   # 导入redis 模块


# ex - 过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
from utils.n_string import str_map , map_str ,str_list , list_str

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def get_map(key):
    return str_map(r.get(key))

def set_map(key,map,ex=360000):
    r.set(key, map_str(map), ex=ex)

def get_list(key):
    return str_list(r.get(key))

def set_list(key, list,ex=360000):
    r.set(key, list_str(list), ex)

def get(key):
    return r.get(key)

def set(key, v,ex=360000):
    r.set(key, v, ex)


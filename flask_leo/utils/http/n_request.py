
# 发送xml请求
import xmltodict
import requests   #导包


def send_post(url, param):
    r = requests.post(url=url, json=param)
    res = r.json()
    return res['data']

def send_get(url,by_key = ''):
    r = requests.get(url=url)
    res = r.json()
    if by_key != '':
        return res[by_key]
    return res

def send_xml_request(url, param):
    xml = "<xml>{0}</xml>".format("".join(["<{0}>{1}</{0}>".format(k, v) for k, v in param.items()]))
    response = requests.post(url, data=xml.encode('utf-8'))
    msg = response.text
    xmlmsg = xmltodict.parse(msg)
    return xmlmsg

def success_data(data):
    return {"code":200,"data":data}

def error_msg(msg):
    return {"code":202,"msg":msg}

def error_():
    return {"code":201}


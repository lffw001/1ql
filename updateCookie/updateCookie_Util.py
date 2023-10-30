import json
import pprint
import time
from functools import wraps

import requests


def time_counts(fn):
    @wraps(fn)
    def mesasure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print('<-- ' + fn.__name__ + ' _执行耗时: ' + str(round((t2 - t1), 3)) + ' seconds -->')
        return result

    return mesasure_time


def login_file():
    with open('config.json', 'r') as f:
        config = json.load(f)
    token = login_ql(config['client_id'], config['client_secret'])
    config['token'] = token
    with open('config.json', 'w') as f:
        f.write(json.dumps(config, ensure_ascii=False))
    return token


def getToken():
    with open('config.json', 'r') as f:
        config = json.load(f)
    if config['token'] == '':
        return login_file()
    else:
        return config['token']


def login_ql(client_id, client_secret):
    url = f"http://120.77.63.151:3041/open/auth/token?client_id={client_id}&client_secret={client_secret}"
    headers = {
        'Content-Type': 'application/json'
    }

    rj = requests.request("GET", url, headers=headers).json()
    if rj['code'] == 200:
        return 'Bearer ' + rj['data']['token']
    else:
        return None


@time_counts
def searchEnvs(name):
    data = []
    url = f"http://120.77.63.151:3041/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    rj = requests.request("GET", url, headers=headers).json()
    if rj['code'] == 200:
        for i in rj['data']:
            if i['name'] == name:
                data.append(i)
        return data
    else:
        return None


def updateEnvByid(id, name, value, remark=''):
    deleteEnv(id)
    postEnv(name, value, remark)
    pass


def deleteEnv(id):
    url = f"http://120.77.63.151:3041/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    rj = requests.request("DELETE", url, headers=headers, data=json.dumps([id], ensure_ascii=False)).json()
    if rj['code'] == 200:
        print("删除环境变量成功")
        return True
    else:
        print("删除环境变量失败\n" + json.dumps(rj, ensure_ascii=False))
        return False


def postEnv(name, value, remark=''):
    url = f"http://120.77.63.151:3041/open/envs"
    headers = {
        'Authorization': getToken(),
        'Content-Type': 'application/json'
    }
    rj = requests.request("POST", url, headers=headers,
                          data=json.dumps([{'value': value, 'name': name, 'remarks': remark}])).json()
    if rj['code'] == 200:
        print("新增环境变量成功")
        return True
    else:
        print("新增环境变量失败\n" + json.dumps(rj, ensure_ascii=False))
        return False


if __name__ == '__main__':
    print(getToken())
    pass
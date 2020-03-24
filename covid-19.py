# https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=158504888761
import json

import requests
import prettytable as pt

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}

resp = requests.session().get(url="https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=158504888761",
                              headers=headers).content

jsonObj = json.loads(resp)

world = jsonObj['data']['areaTree']

map = {}
for d in world:
    if d['total']['confirm'] > 5000:
        map[d['name']] = d['total']

ret = sorted(map.items(), key=lambda x: x[1]['dead'] / x[1]['confirm'], reverse=True)

tb = pt.PrettyTable()
tb.field_names = ['国家', '确诊数', '死亡数', '病死率']


for d in ret:
    tb.add_row([d[0], d[1]['confirm'], d[1]['dead'], '%.2f%%' % ((d[1]['dead'] / d[1]['confirm']) * 100)])

print(tb)

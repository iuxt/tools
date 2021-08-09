import requests
import json

bilibili_uid = {'vmid': '165330963', 'jsonp': 'jsonp'}
r =requests.get("https://api.bilibili.com/x/relation/stat", params=bilibili_uid)
fans = json.loads(r.text)['data']['follower']
print("今天我的B站粉丝数: %s" % fans)
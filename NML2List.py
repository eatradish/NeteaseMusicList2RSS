import rfeed
import requests
import json
import datetime

def get_dic(id):
    url = 'http://music.163.com/api/playlist/detail?id={}'.format(id)
    r = requests.get(url)
    j = json.loads(r.text)
    return j['result']['tracks']

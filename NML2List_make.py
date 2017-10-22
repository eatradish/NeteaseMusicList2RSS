from rfeed import *
import requests
import json
import datetime

def get_dic(playlist_id):
    url = 'http://music.163.com/api/playlist/detail?id={}'.format(playlist_id)
    r = requests.get(url)
    j = json.loads(r.text)
    return j['result']

def test(playlist_id):
    url = 'http://music.163.com/api/playlist/detail?id={}'.format(playlist_id)
    r = requests.get(url)
    j = json.loads(r.text)
    return j['result']

def make_rss(lst, playlist_id):
    item = []
    j = 0
    for i in lst['tracks']:
        item.append(Item(title = i['name'] + '-'+ i['artists'][0]['name'],
                         link = "https://music.163.com/#/song?id={}".format(i['id']),
                         description = """
                                       name: {0}
                                       artist: {1}
                                       """.format(i['name'], i['artists'][0]['name']),
                         author = i['name'],
                         guid = Guid("https://api.sakiiily.moe/NML2List/{}".format(playlist_id)),
                         pubDate = datetime.datetime.fromtimestamp(int(str(lst['createTime'])[:10]))))
        j += 1
    feed = Feed(
	title = "网易云音乐歌单 {} 的订阅".format(playlist_id),
        link = "https://api.sakiiily.moe/NML2List/{}".format(playlist_id),
	description = "网易云音乐歌单 {} 的订阅".format(playlist_id),
	language = "zh_CN",
	lastBuildDate = datetime.datetime.now(),
	items = item)
    return feed.rss()

# import requests
# import execjs

# 测试代码faile
# node = execjs.get()
# # print(node)

# #
# query = "java"


# js_file = 'baidu_sign.js'

# ctx = node.compile(open(js_file).read)

# # js = "get_sign('{}')".format('java')
# js = 'get_sign("java")'
# sign = ctx.eval(js)
# print(sign)

# 测试代码-->success
# with open('baidu_sign.js', 'r') as f:
#     ctx = execjs.compile(f.read())

# a = ctx.call('e', 'python')
# print(a)

import json
import requests
import execjs


# from = input("")

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cache-control': 'no-cache',
    # 'content-length': '121',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'BAIDUID=CACFCC95C7F1418D46273ADF1F8DF0E9:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1575390423; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; yjs_js_security_passport=a0fa00e9c27219f8044b6f99e3b4440978529d67_1575390426_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1575394432; __yjsv5_shitong=1.0_7_4b23a4e762bb804a783fd39a79cd8a30b655_300_1575394433309_120.231.182.149_0ba71bf4',
    'origin': 'https://fanyi.baidu.com',
    'pragma': 'no-cache',
    'referer': 'https://fanyi.baidu.com/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    # 'x-requested-with': 'XMLHttpRequest',
}

query = input("输入查询的单词：")

with open('baidu_sign.js', 'r') as f:
    ctx = execjs.compile(f.read())

sign = ctx.call('e', query)

form_data = {
    'from': 'en',
    'to': 'zh',
    'query': query,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': sign,
    # 'token': '9b8bb341109338ba7e875bd9a9dd88ba',
    'token': 'e856877c1e4da155873b354ad1accad6',
}

result = requests.post('https://fanyi.baidu.com/v2transapi?from=en&to=zh', headers=headers, data=form_data)

print(json.loads(result.text)['trans_result'])
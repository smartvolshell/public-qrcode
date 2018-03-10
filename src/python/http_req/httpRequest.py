# __author__ = 'love stone'
# -*- coding: utf-8 -*-
import json
import random

import certifi
import re

import time
import urllib3

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

url = 'https://data.wxb.com/rank'

user_agents = [
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'  
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
]

header = {
    'User-Agent': user_agents[random.randint(0, 6)],
    'cookie': 'visit-wxb-id=73b325eddc23e6d5d4795b2ffb548cf6; wxb_fp_id=3384828578; PHPSESSID=l6m6efqlbl5o8hur7lu50cnqe2; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1520180287; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1520349471'
}


def request_category():
    return request(1, 1)['categories']


def request_sources(category, page):
    return request(category, page)['sources']


def request_pagesize(category):
    page_data = 20
    total = request(category, 1)
    return int(total['total'] / page_data)+1


def request(category, page):

    data = {
        'category': category,
        'page': page
    }

    result = http.request('GET', url, data,  headers=header)
    print('request url:{} , params:{}'.format(str(url), data))

    while result.status == 503:
        time.sleep(30)
        result = http.request('GET', url, data, headers=header)

    if result.status != 200 and result.status != 503:
        print('http request failed, result:', end='')
        print(result.data)
        return
    # 暂停30秒

    content = result.data.decode('utf-8')
    final = re.findall('<script type="text/javascript">(.*?)</script>', content, re.S | re.M)
    jsonOrg = re.search('(.*?) = (.*?$)', final[0], re.M | re.I)
    jsonData = json.loads(jsonOrg.group(2))

    categories = jsonData['app']['category']
    sources = jsonData['rank']['tableSource']
    total = jsonData['rank']['totalCount']

    return {'categories': categories, 'sources': sources, 'total':total}


if __name__ == '__main__':
    print(request_pagesize(1))
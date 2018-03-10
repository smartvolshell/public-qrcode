# __author__ = 'love stone'
# -*- coding: utf-8 -*-
import threading
import time

import QREntity
import httpRequest
import operation

category_max = 2
page_num_max = 51


def spider_category():
    categories = []
    result = httpRequest.request_category()
    for category in result:
        categories.append(QREntity.Category.from_dict(category))
    return categories


# cate_max 类目
# page_max 页码
def spider_data(category):
    pagesize = httpRequest.request_pagesize(category)
    if pagesize < 1:
        return

    for page in range(1, pagesize+1):
        insert_task = threading.Thread(target=run(append_data(category, page)))
        insert_task.start()
        print('handle category:{} pageSize:{} total page:{}'.format(category, page, pagesize))


def run(qrs):
    try:
        operation.insert_pub_codes(qrs)
    except Exception as ex:
        print(ex)


def append_data(category, page):
    qrs = []
    try:
        every_page_data = httpRequest.request(category, page)
    except Exception as ex:
        print(ex)
        return qrs

    if every_page_data is None:
        return qrs

    for item in every_page_data['sources']:
        if item is None:
            continue
        qr = QREntity.QrEntity.from_dict(dict(item))
        qrs.append(qr)
    return qrs


def back_door(category, page):
    operation.insert_pub_codes(append_data(category, page))


if __name__ == '__main__':
    back_door(11, 36)
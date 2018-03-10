# __author__ = 'love stone'
# -*- coding: utf-8 -*-

import operation
from QrParser import spider_category, spider_data


def insert_all_category():
    categories = spider_category()
    for category in categories:
        if category.id < 0:
            continue
        operation.insert_cate(category)


def insert_qr_code(category):

   qrs = spider_data(category)
   for qr in qrs:
       operation.insert_pub_code(qr)


def insert_qr_codes(category):
    spider_data(category)


if __name__ == '__main__':
    insert_all_category()
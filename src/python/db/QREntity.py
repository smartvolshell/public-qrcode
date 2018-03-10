# __author__ = 'love stone'
# -*- coding: utf-8 -*-


class QrEntity:

    def __init__(self, name, wx_alias, wx_origin_id, avatar, qrcode, fans_num_estimate, desc, rank, cate_id):
        self.name = name
        self.wx_alias = wx_alias
        self.wx_origin_id = wx_origin_id
        self.avatar = avatar
        self.qr_code = qrcode
        self.fans_num_estimate = fans_num_estimate
        self.desc = desc
        self.rank = rank
        self.cate_id = cate_id

    def __str__(self):
        return self.name, self.wx_alias, self.wx_origin_id, self.avatar, self.qr_code, self.fans_num_estimate, self.desc, self.rank, self.cate_id

    @classmethod
    def from_dict(cls, dicts):
        return cls(dicts['name'], dicts['wx_alias'], dicts['wx_origin_id'], dicts['avatar'], dicts['qrcode'], dicts['fans_num_estimate'], dicts['desc'], dicts['rank'], dicts['cate_id'])


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id, self.name

    @classmethod
    def from_dict(cls, dicts):
        return cls(dicts['id'], dicts['name'])
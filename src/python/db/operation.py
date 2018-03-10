# __author__ = 'love stone'
# -*- coding: utf-8 -*-
import pymysql

from QREntity import QrEntity, Category

host = 'localhost'
user = 'volshell'
password = 'volshell'
db = 'qr_code'
charset = 'utf8mb4'
cursorclass = pymysql.cursors.DictCursor

# Connect to the database
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,
    charset=charset,
    cursorclass=cursorclass
)

# Create category
create_cate = """
    CREATE TABLE if not EXISTS  category(
          id TINYINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
          cate_id INT NOT NULL,
          name varchar(32) NOT NULL,
          key idx_cate_id(cate_id)
        )   
    """
create_pub_code = """
    CREATE TABLE if not EXISTS pub_code(
        id bigint not null PRIMARY KEY auto_increment,
        name varchar(64) not null comment '微信公众号昵称',
        wx_alias varchar(100) not null comment '微信号',
        wx_origin_id VARCHAR(32) not null comment '内部id',
        avatar VARCHAR(300) not null comment '公众号头像',
        qr_code VARCHAR(300) not null comment '公众号二维码',
        fans_num_estimate VARCHAR(32) not null comment '预估粉丝数量',
        qr_desc varchar(2000)  comment '公众号功能介绍',
        rank INT comment '同类排名',
        cate_id INT not null comment '类目',
        KEY idx_wx_code(wx_alias)
        )
    """

sql_insert_cate = "INSERT INTO category (cate_id, name) VALUES (%s, %s)"

sql_insert_pub_code = """
        insert into pub_code(
          name,
          wx_alias,
          wx_origin_id,
          avatar,
          qr_code,
          fans_num_estimate,
          qr_desc,
          rank,
          cate_id
        ) values(
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )     
"""


def init():
    try:
        cursor = connection.cursor()
        # create category
        cursor.execute(create_cate)
        connection.commit()
    except Exception as e:
        print('create table category has error,error:{}'.format(e))
        connection.rollback()

    try:
        cursor = connection.cursor()
        # create pub_code
        cursor.execute(create_pub_code)
        connection.commit()
    except Exception as e:
        print('create table pub_code has error,error:{}'.format(e))
        connection.rollback()


def insert_cate(category):
    if category is None:
        return
    if not category.name.strip():
        return
    if category.id is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(create_cate)
        cursor.execute(sql_insert_cate, (category.id, category.name))
        connection.commit()
    except Exception as e:
        print("insert category has error,params:{%s},error:{%s}" % (category.__str__(), e))
        connection.rollback()


def insert_pub_code(qr):
    if qr is None:
        return
    if not qr.name.strip():
        return
    if not qr.wx_alias.strip():
        return

    try:
        cursor = connection.cursor()
        cursor.execute(create_pub_code)
        cursor.execute(sql_insert_pub_code, (qr.name, qr.wx_alias, qr.wx_origin_id, qr.avatar, qr. qr_code, qr.fans_num_estimate, qr.desc, qr.rank, qr.cate_id))
        connection.commit()
    except Exception as e:
        print('insert pub_code has error,params:{},error:{}'.format(qr.__str__(), e))
        connection.rollback()


def insert_pub_codes(qrs):
    if qrs is None:
        return
    if qrs.__len__() == 0:
        return
    entities = []
    for qr in qrs:
        if qr.name is None:
            continue
        entity = QrEntity(qr.name, qr.wx_alias, qr.wx_origin_id, qr.avatar, qr. qr_code, qr.fans_num_estimate, qr.desc, qr.rank, qr.cate_id)
        entities.append(entity.__str__())
    try:
        cursor = connection.cursor()
        cursor.execute(create_pub_code)
        cursor.executemany(sql_insert_pub_code, entities)
        connection.commit()
    except Exception as e:
        print('insert pub_codes has error,params:{},error:{}'.format(entities, e))
        connection.rollback()

# public-qrcode
这是一个使用Python爬取公众号二维码的项目，爬取https://data.wxb.com(微信公众号推广平台) 下的所有公众号。同时记录一下整个过程中遇到的问题。

## 工具

* http: urllib3
* db: pymysql
* parser: beautifulsoup，

## 过程
### 单页面分析
* 请求 https://data.wxb.com/rank?category=1&page=1 （第一个类目下面的第一页，每页有20条数据）。
查看请求过程以及response发现，返回数据都是在<script>中
```javascript

<script type="text/javascript">window.__INITIAL_STATE__ = 
{"app":{"userInfo":{"id":"","nickname":"","email":"","mobile":""},"favoritesList":[],"analyseUsedTimes":{},"category":[{"id":-1,"name":"总榜"},{"id":1,"name":"时事资讯"},{"id":2,"name":"数码科技"},{"id":3,"name":"汽车"},{"id":4,"name":"房产家居"},{"id":5,"name":"职场招聘"},{"id":6,"name":"财经理财"},{"id":7,"name":"生活"},{"id":8,"name":"情感励志"},{"id":9,"name":"女性时尚"},{"id":10,"name":"旅行"},{"id":11,"name":"运动健康"},{"id":12,"name":"餐饮美食"},{"id":13,"name":"搞笑娱乐"},{"id":14,"name":"明星影视"},{"id":15,"name":"母婴"},{"id":16,"name":"文化教育"},{"id":17,"name":"创业管理"},{"id":18,"name":"政务"},{"id":19,"name":"企业"},{"id":20,"name":"地方"},{"id":21,"name":"其他"}],"finishTag":{"yesterday":false,"lastWeek":true,"lastMonth":true}},"rank":{"tableSource":[{"name":"人民日报","wx_alias":"rmrbwx","wx_origin_id":"gh_363b924965e9","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM5Dlw4H8vWoicXPXccEVkWYgFE1pNUvX7uaHmafPODGIEA/64","qrcode":"https://open.weixin.qq.com/qr/code?username=rmrbwx","fans_num_estimate":"146万","desc":"参与、沟通、记录时代。","rank":1,"cate_id":1,"cate_rank":1,"push_total":10,"articles_total":18,"avg_read_num":"10万+","top_read_num_avg":"10万+","top_like_num_avg":14894,"read_num_max":"10万+","avg_like_num":10842,"index_scores":1021.12,"stat_time":"2018-03-09 12:11:06"},{"name":"占豪","wx_alias":"zhanhao668","wx_origin_id":"gh_05d833e54446","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM4vCVnWl4qurNWlHyahyxJXzBveeBRQ1shanNYicic8vvMg/64","qrcode":"https://open.weixin.qq.com/qr/code?username=zhanhao668","fans_num_estimate":"145万","desc":"国际局势·财经投资·国学哲学丨连续4年新媒体百大人物/自媒体最佳表现大奖/最受中国企业关注的自媒体账号丨我们一起同行，我们一起进步！","rank":4,"cate_id":1,"cate_rank":2,"push_total":1,"articles_total":8,"avg_read_num":98004,"top_read_num_avg":"10万+","top_like_num_avg":25262,"read_num_max":"10万+","avg_like_num":7705,"index_scores":994.72,"stat_time":"2018-03-09 12:12:13"},{"name":"新华社","wx_alias":"xinhuashefabu1","wx_origin_id":"gh_6651e07e4b2d","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM6CRL0IbOnOf9n66mYHko2JJvQOSwdzg8o2XicspBbVTkg/64","qrcode":"https://open.weixin.qq.com/qr/code?username=xinhuashefabu1","fans_num_estimate":"145万","desc":"“新华社发布·全国两会”由新华社新媒体中心负责管理和运营，以展示厅形式集纳了新华社旗下十余个法人微信公众号，第一时间在微信发出新华社声音。“新华社发布”腾讯微博：http://e.t.qq.com/xinhuashefabu","rank":8,"cate_id":1,"cate_rank":3,"push_total":9,"articles_total":17,"avg_read_num":94421,"top_read_num_avg":98517,"top_like_num_avg":4425,"read_num_max":"10万+","avg_like_num":3557,"index_scores":944.77,"stat_time":"2018-03-09 12:09:05"},{"name":"新闻哥","wx_alias":"newsbro","wx_origin_id":"gh_faa35168f414","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM4dd8gzRSRMib8jeHl3w6lXdibibr7ibNJ5uBKpeLpw1ghWow/64","qrcode":"https://open.weixin.qq.com/qr/code?username=newsbro","fans_num_estimate":"500万+","desc":"轻幽默，爱搞怪的新闻哥，希望你们喜欢我提供的新闻。","rank":11,"cate_id":1,"cate_rank":4,"push_total":1,"articles_total":3,"avg_read_num":"10万+","top_read_num_avg":"10万+","top_like_num_avg":4509,"read_num_max":"10万+","avg_like_num":3510,"index_scores":917.32,"stat_time":"2018-03-09 12:10:04"},{"name":"冯站长之家","wx_alias":"fgzadmin","wx_origin_id":"gh_ba6105d7c051","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM6Qkhp05icEFzv1WnPsOicpqdT1Tmtq69879xALicHshX8AA/64","qrcode":"https://open.weixin.qq.com/qr/code?username=fgzadmin","fans_num_estimate":"500万+","desc":"每天新闻资讯类公众号单篇阅读量排名经常第一！每天提供人工精选最新鲜、最全面、最有价值的新闻早餐，每天三分钟，知晓天下事。还有最新财经早餐、医疗晨报、历史上的今天、一日一诗等等站长精选推荐的精彩内容，精彩不容错过！","rank":14,"cate_id":1,"cate_rank":5,"push_total":1,"articles_total":8,"avg_read_num":47313,"top_read_num_avg":"10万+","top_like_num_avg":14527,"read_num_max":"10万+","avg_like_num":4318,"index_scores":911.29,"stat_time":"2018-03-09 12:07:39"},{"name":"央视新闻","wx_alias":"cctvnewscenter","wx_origin_id":"wxid_pzhf43hmwizd11","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM7K1jDqNGenoK7DmzRhYy9KqAXmqMNS8c99Yfy1cfHw9Q/64","qrcode":"https://open.weixin.qq.com/qr/code?username=cctvnewscenter","fans_num_estimate":"140万","desc":"中央电视台新闻中心公众号，提供时政、社会、财经、体育、突发等新闻信息以及天气、路况、视频直播等服务信息。","rank":16,"cate_id":1,"cate_rank":6,"push_total":9,"articles_total":15,"avg_read_num":63647,"top_read_num_avg":77371,"top_like_num_avg":3922,"read_num_max":"10万+","avg_like_num":2762,"index_scores":899.72,"stat_time":"2018-03-09 12:08:00"},{"name":"人民网","wx_alias":"people_rmw","wx_origin_id":"gh_d62474859d61","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM7fyU4GApMpvWanVpMHA15f30wAAIpDYd3mQeyuVtywEQ/64","qrcode":"https://open.weixin.qq.com/qr/code?username=people_rmw","fans_num_estimate":"134万","desc":"人民网官方公众号，每天为您提供最权威、最及时、最好看的新闻报道和热点解读。权威、实力，源自人民。","rank":29,"cate_id":1,"cate_rank":7,"push_total":8,"articles_total":13,"avg_read_num":78624,"top_read_num_avg":94768,"top_like_num_avg":1879,"read_num_max":"10万+","avg_like_num":1422,"index_scores":875.72,"stat_time":"2018-03-09 12:07:10"},{"name":"侠客岛","wx_alias":"xiake_island","wx_origin_id":"gh_572b3506a44f","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM4wLaVNe0QukS1KDFKesyxbZB8cOMTkTWexnOmTGMibhrQ/64","qrcode":"https://open.weixin.qq.com/qr/code?username=xiake_island","fans_num_estimate":"134万","desc":"但凭侠者仁心，拆解时政迷局。","rank":41,"cate_id":1,"cate_rank":8,"push_total":2,"articles_total":3,"avg_read_num":69092,"top_read_num_avg":"10万+","top_like_num_avg":2134,"read_num_max":"10万+","avg_like_num":1451,"index_scores":849.96,"stat_time":"2018-03-09 12:06:03"},{"name":"局座召忠","wx_alias":"zhangzhaozhong45","wx_origin_id":"gh_48345b7a0f3c","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM5dCwiaictkODYruTptxHbXaLzDKNYpDJTO9cxGmQR9ZuxA/64","qrcode":"https://open.weixin.qq.com/qr/code?username=zhangzhaozhong45","fans_num_estimate":"146万","desc":"著名军事专家张召忠在公众平台上进行内容发布的自媒体，包含视频、专栏和新节目的预告等。","rank":59,"cate_id":1,"cate_rank":9,"push_total":1,"articles_total":5,"avg_read_num":50381,"top_read_num_avg":"10万+","top_like_num_avg":2451,"read_num_max":"10万+","avg_like_num":1325,"index_scores":825.86,"stat_time":"2018-03-09 12:08:18"},{"name":"环球时报","wx_alias":"hqsbwx","wx_origin_id":"gh_95b0feda9646","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM5YzxFRdja0Uw5fP7gNmZLEdcTzfMpCAaK8thIo32ick7g/64","qrcode":"https://open.weixin.qq.com/qr/code?username=hqsbwx","fans_num_estimate":"91万","desc":"报道多元世界 解读复杂中国","rank":68,"cate_id":1,"cate_rank":10,"push_total":4,"articles_total":16,"avg_read_num":45040,"top_read_num_avg":79828,"top_like_num_avg":1838,"read_num_max":"10万+","avg_like_num":951,"index_scores":816.16,"stat_time":"2018-03-09 12:05:30"},{"name":"参考消息","wx_alias":"ckxxwx","wx_origin_id":"gh_2837b93c1976","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM5XkdUib86HfGNkWicmdjRWY9MiawrcJIOOBQce7wI8Dicz0A/64","qrcode":"https://open.weixin.qq.com/qr/code?username=ckxxwx","fans_num_estimate":"75万","desc":"纵览外国媒体每日报道精选","rank":81,"cate_id":1,"cate_rank":11,"push_total":5,"articles_total":14,"avg_read_num":45908,"top_read_num_avg":63562,"top_like_num_avg":1064,"read_num_max":83464,"avg_like_num":846,"index_scores":799.37,"stat_time":"2018-03-09 12:08:01"},{"name":"新闻早餐","wx_alias":"xinwenzaocan","wx_origin_id":"gh_11d6ef0dd9d4","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM7TeBnFzyJN0DYUxRQNicl0biasCcPzJ2Ir8tjt2qLsJl3g/64","qrcode":"https://open.weixin.qq.com/qr/code?username=xinwenzaocan","fans_num_estimate":"141万","desc":"新闻大事早知道，每天人工筛选各大新闻源的价值内容，分分钟让您通览时事要闻、财经体育、人文健康、社会生活、历史上的今天等快讯，阅读精美文章，传播正能量，尽在新闻早餐，每天清晨，不见不散！","rank":82,"cate_id":1,"cate_rank":12,"push_total":1,"articles_total":8,"avg_read_num":46767,"top_read_num_avg":"10万+","top_like_num_avg":2924,"read_num_max":"10万+","avg_like_num":672,"index_scores":799.04,"stat_time":"2018-03-09 12:07:28"},{"name":"新华网","wx_alias":"newsxinhua","wx_origin_id":"gh_68b976f584b5","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM6xR5PibDCiaxVyClkw1uibQ4S9Vcr31YrWMeRhfCzicCmWkQ/64","qrcode":"https://open.weixin.qq.com/qr/code?username=newsxinhua","fans_num_estimate":"84万","desc":"新闻有深度  思想有温度","rank":103,"cate_id":1,"cate_rank":13,"push_total":8,"articles_total":16,"avg_read_num":36557,"top_read_num_avg":50323,"top_like_num_avg":1282,"read_num_max":"10万+","avg_like_num":864,"index_scores":784.76,"stat_time":"2018-03-09 12:04:48"},{"name":"军武次位面","wx_alias":"junwu233","wx_origin_id":"gh_771635949f86","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM613p98vqPRmaicllMM95LfaWpiaPHqkoDmH7SJzk4FdEeQ/64","qrcode":"https://open.weixin.qq.com/qr/code?username=junwu233","fans_num_estimate":"144万","desc":"《军武次位面》节目官方公众号，军事文化的推动者，军迷每周的节日","rank":111,"cate_id":1,"cate_rank":14,"push_total":1,"articles_total":8,"avg_read_num":54095,"top_read_num_avg":90193,"top_like_num_avg":744,"read_num_max":90193,"avg_like_num":513,"index_scores":778.62,"stat_time":"2018-03-09 12:05:47"},{"name":"中国搜索","wx_alias":"chinaso_com","wx_origin_id":"gh_c01450c997fa","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM54IiciczSUrrBN3TpyGIvhd9ct119zyG3GNBDJxxefN6eQ/64","qrcode":"https://open.weixin.qq.com/qr/code?username=chinaso_com","fans_num_estimate":"64万","desc":"中国搜索（www.chinaso.com）是由人民日报社、新华通讯社、中央电视台、光明日报社、经济日报社、中国日报社、中国新闻社联合设立的互联网企业。","rank":132,"cate_id":1,"cate_rank":15,"push_total":4,"articles_total":12,"avg_read_num":31728,"top_read_num_avg":60398,"top_like_num_avg":1323,"read_num_max":83856,"avg_like_num":588,"index_scores":759.85,"stat_time":"2018-03-09 12:07:58"},{"name":"南方周末","wx_alias":"southernweekly","wx_origin_id":"nanfangzhoumo","avatar":"http://wavatar.wxb.com/mmhead/Jszx49YbsxRfeb75zAHCrJ4jvLPyVbW5fEBnDsSqcS0/64","qrcode":"https://open.weixin.qq.com/qr/code?username=southernweekly","fans_num_estimate":"90万","desc":"在这里，读懂中国！infzm.com","rank":173,"cate_id":1,"cate_rank":16,"push_total":2,"articles_total":2,"avg_read_num":67168,"top_read_num_avg":67168,"top_like_num_avg":240,"read_num_max":89063,"avg_like_num":240,"index_scores":729.23,"stat_time":"2018-03-09 12:09:05"},{"name":"瞭望智库","wx_alias":"zhczyj","wx_origin_id":"gh_0008713c31f5","avatar":"http://wavatar.wxb.com/mmhead/Q3auHgzwzM4wNOTNGy6GJmNXoRTFnUUfOibX94nkOyRzlkFJ0SazQ9g/64","qrcode":"https://open.weixin.qq.com/qr/code?username=zhczyj","fans_…</script>

```
数据解析就非常简单了，使用正则匹配到对应的json就好了，显得非常完美了，但是意想不到的事情还在后面。

* 发送请求
```python 
    result = http.request('GET', url, data,  headers=header)
    print('request url:{} , params:{}'.format(str(url), data))
    content = result.data.decode('utf-8')
    final = re.findall('<script type="text/javascript">(.*?)</script>', content, re.S | re.M)
    jsonOrg = re.search('(.*?) = (.*?$)', final[0], re.M | re.I)
    jsonData = json.loads(jsonOrg.group(2))
```
  * 设置header
  ``` python
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
    'cookie': 'your cookie'
  }
 ```python
 
* 数据解析
  * 从上面过程中,最终获取到了对应的json数据，json中包含了对应的category/source，以及每一个category下面的source的数量 totalCount
  
  ```python
    categories = jsonData['app']['category']
    sources = jsonData['rank']['tableSource']
    total = jsonData['rank']['totalCount']
    
  ```
  * 通过json数据，抽象出三个基本的方法，
  ```python 
  # 获取所有的类目列表
  def request_category():
    return request(1, 1)['categories']

  # 获取公众号信息
  def request_sources(category, page):
    return request(category, page)['sources']
  # 获取每个类目下面的公众号的数量
  def request_pagesize(category):
    page_data = 20
    total = request(category, 1)
    return int(total['total'] / page_data)+1
    
  ```
 *  json 2 object
  * 定义实体
  ```python
  # 公众号
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
  # 类目实体
  class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
         return self.id, self.name
  ```
  * 对象转换
  ```python
    qrs = []
      for item in every_page_data['sources']:
        if item is None:
            continue
        # 通过类方法from_dict来转换为实体
        qr = QREntity.QrEntity.from_dict(dict(item))
        qrs.append(qr)
    return qrs
    
  ```
* 数据持久化
  数据批量插入，在刚开始做批量的时候，数据库的完整性约束，导致一些数据插入失败，整个批量回滚。后来放宽数据库完整性约束，批量处理完毕后，在对数据进行二次清洗。

  ```python
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
        entities.append(entity.__str__()) #注意对executemany 的使用方法，通过自定义的__str__()将数据转换为元组。
    try:
        cursor = connection.cursor()
        cursor.execute(create_pub_code)
        cursor.executemany(sql_insert_pub_code, entities)
        connection.commit()
    except Exception as e:
        print('insert pub_codes has error,params:{},error:{}'.format(entities, e))
        connection.rollback()
  ```
  
  ### 批量爬取
  > 单个页面的爬取数据，分析数据，持久化完成之后。对于批量，直接for循环即可实现。但是现实并非如此完美，被爬取数据的网站做了限流控制，访问的时候出现 503 拒绝服务。
  
  * 应对策略1
      模拟浏览器，设置不同代理，如上代码中设置了7种不同的代理，随机使用其中一个，这样效果提升了不少。
  * 应对策略2
      header添加cookies,因为网站做了限制，当访问第二页的时候，需要让你登录，随便注册个账号，拿到对应的cookie，添加到header里面，完美。
  
  > 当爬取差不多7-8页数据的时候，会出现一直报错(503)，刷新页面发现，及时注册账号，添加cookie，网站也做了访问限制，需要输入验证码。
  
   * 应对策略
    这个比较low了，当出现503的时候，会直接将请求sleep住，人肉输入验证码，重复上次sleep的请求。大家有什么好的方法，可以讨论一下。
    
    
  ## 总结
  
	1. 使用urllib3,完成http请求。
	2. bytes to str : bytes.decode('utf-8')解码即可
	3. InsecureRequestWarning: Unverified HTTPS request is being made. https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings。https需要添加证书。
	4.被爬网站存在反爬限制，需要设置代理。   
		 result = http.request('GET', url, headers={'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
	5. 携带cookie模拟登陆
		header ={
			'user-agent':'agent',
			'cookie':'your cookie'
		}
		http = urllib3.PoolManager()
		result = http.request(url,header=header)
	6. insert category has error,params:{None},error:{unsupported operand type(s) for %: 'function' and 'tuple'}
		sql :insert_cate = "INSERT INTO category (cate_id, name) VALUES (%d, %s)"
		exe:cursor.execute(insert_cate % (category.id, category.name))
		更正为：
		cursor.execute(insert_cate, (category.id, category.name))
	7. {%d format: a number is required, not str}
		在数据表中id使用的类型是int, 传参的时候使用%d。导致上面报错，其实pymysql在执行的时候，会自动转换类型。所以%d可以改成%s。



  
  

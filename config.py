'''
Date:2019-08-14 10:34
User:ChenXi
E-mail:15091630326@163.com
'''

from fake_useragent import UserAgent

Host = 'www.lagou.com'
Origin = 'https://www.lagou.com'
Referer = 'https://www.lagou.com/jobs/list_python'
Connection = 'keep-alive'
Accept = 'application/json, text/javascript, */*; q=0.01'
ua = UserAgent(verify_ssl=False)
# 爬取线程数
threadCount = 50
pages = 50
CsvFileName = 'lagou.csv'
# 筛选代理IP的线程数
FilterthreadCount = 100
# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies_2'

# 代理分数
MAX_SCORE = 3
MIN_SCORE = 0
INITIAL_SCORE = 1

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 200

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5005

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

PORT = 7777
# 最大批测试量
BATCH_TEST_SIZE = 10
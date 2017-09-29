# using Django 1.11.5.
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 设置生产环境和部署环境自动切换：---------------------------------------------------------------------
# DEBUG = True
# ALLOWED_HOSTS = []
import socket
# 得到主机名
def hostname():
    sys = os.name
    if sys == 'nt':
        hostname = os.getenv('computername')
        return hostname

    elif sys == 'posix':
        host = os.popen('echo $HOSTNAME')
        try:
            hostname = host.read()
            return hostname
        finally:
            host.close()
    else:
        raise RuntimeError('Unkwon hostname')

# 调试和模板调试配置
# 主机名相同则为开发环境，不同则为部署环境
# ALLOWED_HOSTS只在调试环境中才能为空
if socket.gethostname().lower() == hostname().lower():
    DEBUG = TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []
else:
    # ALLOWED_HOSTS 是允许访问的域名列表，域名前加一个点表示允许访问该域名下的子域名，比如 www.zmrenwu.com、test.zmrenwu.com 等二级域名同样允许访问。如果不加前面的点则只允许访问 zmrenwu.com。
    ALLOWED_HOSTS = [
        '.277127311.top',
        '127.0.0.1',
        'localhost ',
    ]
    DEBUG = TEMPLATE_DEBUG = False


# 增加一些app----------------------------------------------------------------------------------------
INSTALLED_APPS = [
    'haystack',# 将haystack放在最后，提供搜索功能的 django 第三方应用，http://www.jb51.net/article/122155.htm
]


# 在主目录下增加templates文件夹后改成如下：-----------------------------------------------------------
TEMPLATES = [
    {
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]


# Django 多数据库联用，每个app都可以单独设置一个数据库；-----------------------------------------------
# http://code.ziqiangxuetang.com/django/django-multi-database.html
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# 如果不是defalut(默认数据库）要在命令后边加 --database=数据库对应的settings.py中的名称；
# 如：python manage.py migrate --database=db1（makemigrations不需要这样写）
# 导出：python manage.py dumpdata app1 --database=db1 > app1_fixture.json
# 导入：python manage.py loaddata app1_fixture.json --database=db1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app1',# 数据库app1需提前创建；
        'USER': 'root',# 数据库用户名
        'PASSWORD': '654321',
        'HOST': 'localhost',#数据库主机，留空默认为localhost
        'PORT': '3306',
    },
}
# 在project_name文件夹中存放 database_router.py 文件
DATABASE_ROUTERS = ['project_name.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    'app1': 'db1',
}
# No module named 'MySQLdb'的解决办法：
# MySQLdb不支持py3，所以py3环境下用PyMySQL代替，先 pip install PyMySQL；
# 然后在 自己的项目 的__init__.py文件下 输入：
# import pymysql
# pymysql.install_as_MySQLdb()


# 默认语言及时区调整--------------------------------------------------------------------------------
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'




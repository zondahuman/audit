#检测Django安装是否正确
C:\Users\thinkpad>python
Python 2.7.1 (r271:86832, Nov 27 2010, 17:19:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.VERSION
(1, 6, 11, 'final', 0)
>>>

#创建工程
Django-admin.py startproject audit
#创建app
manage.py startapp verify


采用 python manage.py validate 检查模型的语法和逻辑是否正确。
没有错误则执行 python manage.py syncdb创建数据表。

python manage.py makemigrations
python manage.py migrate
python manage.py syncdb


检查与数据库的链接
C:\python\Django\strip>python manage.py shell

In [2]: from django.db import connection as conn

In [3]: print conn
<django.db.DefaultConnectionProxy object at 0x0000000002D90EF0>

启动命令：
manage.py runserver


pycharm 断点调试
  1. pip install django-pdb
  2. Add 'django_pdb' to your INSTALLED_APPS
You can now run: manage.py runserver --pdb to break into pdb at the start of every view...
And run: manage.py test --pdb to break into pdb on test failures/errors...
http://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way









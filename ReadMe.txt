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







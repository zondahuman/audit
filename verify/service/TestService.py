# encoding:utf-8
from verify import models
import json
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'audit.settings'


def insertTest(request):
    print 'post start'
    jsonObject = json.loads(request.body)
    print 'post jsonObject',jsonObject
     # 获得表单数据
    username = jsonObject['username']
    print 'post username=',username
    password = jsonObject['pword']
    print 'post password=',password
    email = jsonObject['email']
    print 'post email=',email
    mysite = jsonObject['mysite']
    print 'post mysite=',mysite
    sex = jsonObject['sex']
    print 'post sex=',sex
    intro = jsonObject['intro']
    print 'post intro=',intro
     # 添加到数据库
    instanceTest = models.test.objects.create(email=email,username=username, pword=password,mysite=mysite,sex=sex,intro=intro)
    print 'instanceTest.id=',instanceTest.id

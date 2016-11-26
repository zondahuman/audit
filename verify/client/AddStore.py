#!/usr/bin/env python
#coding=utf8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'audit.settings'
from verify import models
username = "abin"
password = "123456"
email = "abin"
mysite = "abin"
sex = 23
intro = "abin"
models.test.objects.create(email=email,username=username, pword=password,mysite=mysite,sex=sex,intro=intro)
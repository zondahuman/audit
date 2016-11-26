#!/usr/bin/env python
#coding=utf8

import os

from verify.service import ApplicationService

os.environ['DJANGO_SETTINGS_MODULE'] = 'audit.settings'

if __name__ == '__main__':
    # print ApplicationStatusResponse.success()

    result = ApplicationService.checkParams("aaa",1,2,0,"zhiwen",'ios')
    print 'result=',result
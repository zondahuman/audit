#!/usr/bin/env python
#coding=utf8

import json, urllib2

httpClient = None
post_server='http://127.0.0.1:8000/verify/submit/'
def http_post(values):
    json_data = json.dumps(values)
    print "json_data: ",json_data
    try:
        req = urllib2.Request(post_server,json_data)   #生成页面请求的完整数据
        print "req: ",req
        response = urllib2.urlopen(req)    # 发送页面请求
        print "response: ",response
        content = response.read()
        print 'content=',content
    except urllib2.HTTPError,error:
        print "ERROR: ",error.read()


if __name__ == '__main__':
    data = {}
    data['userKey'] = 'abin@gmail.com'
    data['productType'] = 111
    data['channelId'] = 234
    data['isSelfRegister'] = 1
    data['blackBoxId'] = "zhiwen"
    data['platform'] = 'IOS'
    http_post(data)
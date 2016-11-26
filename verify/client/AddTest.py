#!/usr/bin/env python
#coding=utf8

import httplib, urllib

httpClient = None
try:
    params = urllib.urlencode({'email':'abin@heika.com','username':'lee','pword':'123456','mysite':'mysite11111','sex':13,'intro':'i am donald trump'})
    # headers = {"Content-type": "application/x-www-form-urlencoded"}
    headers = {"Content-type": "application/x-www-form-urlencoded" , "Accept": "text/plain"}
    # headers = {"Content-type": "text/plain" , "Accept": "text/plain"}
    # headers = { "Accept": "text/plain"}
    # headers = {}

    httpClient = httplib.HTTPConnection("127.0.0.1", 8000, timeout=30000)
    # httpClient.request("POST", "/verify/plus", params, headers)
    # httpClient.request("POST", "/audit/plus", params, headers)
    # httpClient.request("POST", "/plus", params, headers)
    httpClient.request("POST", "/verify/add", params)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
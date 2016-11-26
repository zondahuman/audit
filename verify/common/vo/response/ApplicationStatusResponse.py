# encoding:utf-8
import json
# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'audit.settings'

SUCCESS_STATUS = "0"
FAILURE_STATUS = "-1"


def success():
    response={}
    response['status'] = SUCCESS_STATUS
    response['message'] = "SUCCESS"
    response['data'] = ''
    return json.dumps(response)

def failure():
    response={}
    response['status'] = FAILURE_STATUS
    response['message'] = "FAILURE"
    response['data'] = ''
    return json.dumps(response)

def failurem(message):
    response={}
    response['status'] = FAILURE_STATUS
    response['message'] = message
    response['data'] = ''
    return json.dumps(response)

def successmd(message,data):
    response={}
    response['status'] = SUCCESS_STATUS
    response['message'] = message
    response['data'] = data
    return json.dumps(response)

def failuremd(message,data):
    response={}
    response['status'] = FAILURE_STATUS
    response['message'] = message
    response['data'] = data
    return json.dumps(response)

def successmds(status,message,data):
    response={}
    response['status'] = SUCCESS_STATUS
    response['message'] = "SUCCESS"
    response['data'] = data
    return json.dumps(response)

def failuresmd(status,message,data):
    response={}
    response['status'] = FAILURE_STATUS
    response['message'] = "SUCCESS"
    response['response'] = data
    return json.dumps(response)
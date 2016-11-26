# encoding:utf-8
#/usr/bin/python

import ConfigParser
import os

def read(env, section, key):
    BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
    PRE_DIR = os.path.dirname(BASE_DIR)
    conf_name = "setting-"+env+".conf"
    CONF_DIR = os.path.join(PRE_DIR,"conf")
    config = ConfigParser.ConfigParser()
    file_path = os.path.join(CONF_DIR,conf_name)
    config.read(file_path)
    # sections = config.sections()
    # print 'sections:', sections
    # options = config.options(section)
    # print 'options:', options
    value = config.get(section, key)
    return value


def readxxx(env, key):
    BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
    PRE_DIR = os.path.dirname(BASE_DIR)
    conf_name = "setting-"+env+".conf"
    CONF_DIR = os.path.join(PRE_DIR,"conf")
    config = ConfigParser.ConfigParser()
    file_path = os.path.join(CONF_DIR,conf_name)
    config.read(file_path)
    # sections = config.sections()
    SECTION = "xxx"
    # options = config.options(SECTION)
    # print 'options:', options
    value = config.get(SECTION, key)
    return value

if __name__ == '__main__':
    environment = 'dev'
    key = 'xxx.mysql.host'
    result = readxxx(environment, key)
    print 'result=',result

    section = 'xxx'
    result1 = read(environment, section, key)
    print 'result1=',result1




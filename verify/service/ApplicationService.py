# encoding:utf-8
import json

from django.db import transaction
from verify import models
from verify.common.vo.response import ApplicationStatusResponse
from verify.common.constant import ApplicationConstant
from verify.service import RedisService
# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'audit.settings'



@transaction.commit_on_success
def submitApplication(request):
    application = json.loads(request.body)
    print 'application=',application
    userKey = application['userKey']
    print 'userKey=',userKey
    productType = application['productType']
    print 'productType=',productType
    channelId = application['channelId']
    print 'channelId=',channelId
    isSelfRegister = application['isSelfRegister']
    print 'isSelfRegister=',isSelfRegister
    blackBoxId = application['blackBoxId']
    print 'blackBoxId=',blackBoxId
    platform = application['platform']
    print 'platform=',platform
    try:
        checkParams(userKey, productType, channelId, isSelfRegister, blackBoxId, platform)
        print 'application_status create start'
        num = RedisService.get(ApplicationConstant.APPLICATION_REDIS_TOTAL_NUM)
        print 'num=',num
        if num == None:
            raise Exception(ApplicationStatusResponse.failurem("num为空"))

        lockKey = ApplicationConstant.APPLICATION_REDIS_LOCK_KEY.format(key=userKey);
        print 'lockKey=',lockKey
        lockStatus = RedisService.acquireLock(lockKey, 60)
        if lockStatus == 0:
            raise Exception(ApplicationStatusResponse.failurem("进件正在处理中，返回"))

        applicationStatus = models.application_status.objects.create(user_key=userKey,application_id='aaaaa',current_verify_status='ORIGINAL', appl_user_info_sync_status=0, version=1)
        print 'application_status create end, applicationStatus.getId=',applicationStatus.id
        models.application_submit_info.objects.create(user_key=userKey,product_type=productType,channel_id=channelId,is_self_register=isSelfRegister, black_box_id=blackBoxId, platform=platform,verify_appl_status_id=applicationStatus.id)
        RedisService.releaseLock(lockKey)
    except Exception, e:
        print e
        raise Exception(ApplicationStatusResponse.failurem("进件入库失败"))



def checkParams(userKey, productType, channelId, isSelfRegister, blackBoxId, platform):
    print 'checkParams start'
    if (userKey == None or productType == None or channelId == None or isSelfRegister == None or blackBoxId == None or platform == None):
        print 'checkParams before exception'
        raise Exception("抛出一个异常")("参数不能为空")
        print 'checkParams after exception'
    print 'checkParams end'




if __name__ == '__main__':
    result = checkParams("aaa",1,2,0,"zhiwen",'ios')
    print 'result=',result




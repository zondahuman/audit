# encoding:utf-8
import os

from django.http import HttpResponse

from verify import models
from verify.common.vo.response import ApplicationStatusResponse

os.environ['DJANGO_SETTINGS_MODULE'] = 'audit.settings'
from service import ApplicationService,TestService
# Create your views here.


# 表单


#  http://127.0.0.1:8000/verify/add
def add(request):
    # pdb.set_trace()
    print 'add start'
    if request.method == 'POST':
        print 'post start'
        uf = models.test(request.POST)
        # print 'uf',json.dump(uf)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['pword']
            email = uf.cleaned_data['email']
            mysite = uf.cleaned_data['mysite']
            sex = uf.cleaned_data['sex']
            intro = uf.cleaned_data['intro']
            # 添加到数据库
            test = models.test.objects.create(email=email,username=username, password=password,mysite=mysite,sex=sex,intro=intro)
            print 'test.id=',test.id
            return HttpResponse('post record success!!')
    else:
        return HttpResponse("get record failure")
    return HttpResponse("add record")

def insert(request):
    # pdb.set_trace()
    print 'add insert'
    if request.method == 'POST':
        TestService.insertTest(request)
        return HttpResponse('recv_data--post record success!!')
    else:
        return HttpResponse('recv_data--get record success!!')

#进件申请
def submit(request):
    # pdb.set_trace()
    print 'add submit'
    if request.method == 'POST':
        try:
            ApplicationService.submitApplication(request)
            return HttpResponse(ApplicationStatusResponse.success())
        except Exception, e:
            print e
            return HttpResponse(ApplicationStatusResponse.failurem("进件入库失败"))

    else:
        return HttpResponse(ApplicationStatusResponse.failurem("进件入库失败"))




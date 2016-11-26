#encoding:utf-8

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from verify import models
import pdb
# Create your views here.


# http://127.0.0.1:8000/verify/index
def index(request):
    # pdb.set_trace()
    print 'aaaaa'
    return HttpResponse("Job Index View")


def plus(request):
    if request.method == 'POST':
        uf = models.test(request.POST)
        # if uf.is_valid():
            # 获得表单数据
        username = uf.cleaned_data['username']
        password = uf.cleaned_data['pword']
        email = uf.cleaned_data['email']
        mysite = uf.cleaned_data['mysite']
        sex = uf.cleaned_data['sex']
        intro = uf.cleaned_data['intro']
        # 添加到数据库
        models.test.objects.create(email=email,username=username, password=password,mysite=mysite,sex=sex,intro=intro)
        return HttpResponse('post record success!!')
    else:
        return HttpResponse('get record failure!!')
    return HttpResponse("add record")

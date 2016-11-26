# encoding:utf-8
from django.db import models
from django.utils import timezone


# Create your models here.
class test(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='')
    username = models.CharField(max_length=40)
    # username = models.CharField(max_length=40,unique=True)
    pword = models.CharField(max_length=20)
    cdate = models.DateField(default=timezone.now)
    birth = models.DateField(default=timezone.now)
    mysite = models.URLField(default='')
    sex = models.IntegerField(default=0)
    intro = models.TextField(default='')
    class Meta:
        # app_label = ''
        app_label = 'verify'
        #自定义表名
        # db_table = 'Test'


#进件审核表
class application_status(models.Model):
    id = models.AutoField(primary_key=True)
    user_key = models.CharField(max_length=64)
    application_id = models.CharField(max_length=64,unique=True)
    # username = models.CharField(max_length=40,unique=True)
    credit_limit = models.DecimalField(max_digits=19,decimal_places=2)
    cash_draw_ratio = models.DecimalField(max_digits=19,decimal_places=2)
    card_product_id = models.IntegerField(default=0)
    current_verify_status = models.CharField(max_length=64)
    system_reason_code = models.CharField(max_length=256)
    manual_reason_code = models.CharField(max_length=256)
    remark = models.CharField(max_length=1024)
    final_status_verify_date = models.DateField(default=timezone.now)
    appl_user_info_sync_status = models.BooleanField(default=0)
    manual_verify_user_id = models.IntegerField(default=0)
    manual_verify_date = models.DateField(default=timezone.now)
    manual_verify_result = models.CharField(max_length=255, default='')
    system_verify_result = models.CharField(max_length=255, default='')
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)
    version = models.IntegerField(default=0)
    class Meta:
        # app_label = ''
        app_label = 'verify'
        #自定义表名
        # db_table = 'Test'

#进件提交信息保存表
class application_submit_info(models.Model):
    id = models.AutoField(primary_key=True)
    verify_appl_status_id = models.IntegerField(default=0)
    user_key = models.CharField(max_length=255)
    channel_id = models.IntegerField(default=0)
    product_type = models.IntegerField(default=0)
    is_self_register = models.BooleanField(default=0)
    black_box_id = models.TextField(default='')
    platform = models.CharField(max_length=255)
    id_no = models.CharField(max_length=255)
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)
    version = models.IntegerField(default=0)
    class Meta:
        # app_label = ''
        app_label = 'verify'
        #自定义表名
        # db_table = 'Test'


#进件提交信息保存表
class application_submit_info(models.Model):
    id = models.AutoField(primary_key=True)
    verify_appl_status_id = models.IntegerField(default=0)
    user_key = models.CharField(max_length=255)
    channel_id = models.IntegerField(default=0)
    product_type = models.IntegerField(default=0)
    is_self_register = models.BooleanField(default=0)
    black_box_id = models.TextField(default='')
    platform = models.CharField(max_length=255)
    id_no = models.CharField(max_length=255)
    create_time = models.DateField(default=timezone.now)
    update_time = models.DateField(default=timezone.now)
    version = models.IntegerField(default=0)


















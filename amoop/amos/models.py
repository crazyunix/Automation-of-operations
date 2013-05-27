#coding=utf-8
from django.db import models
import datetime

class Users(models.Model):
    username = models.CharField(u'用户名',max_length=10)
    passwd = models.CharField(u'密码',max_length=16)
    email = models.EmailField(u'E-mail')
    phone = models.CharField(u'电话',max_length=11)
    ctime = models.DateField(u'创建时间',default=datetime.datetime.now())
    lasttime = models.DateField(u'最后登录',default=datetime.datetime.now())
    ip = models.IPAddressField()
    failure = models.DateField(u'失效时间')
    ltime = models.DateField(u'离开系统时间',default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

class Group(models.Model):
    groupname = models.CharField(u'组名',max_length=10)
    groupemail = models.EmailField(u'组邮件',max_length=30)
    user_id = models.ManyToManyField(Users)

    def __unicode__(self):
        return self.groupname

class Resources(models.Model):
    dev_choice = (
            ('A',u'R710'),
            ('B',u'R410'),
            )
    os_choice = (
            ('a',u'Centos 5.x'),
            ('b',u'Centos 6.x'),
            ('c',u'Ubuntu 12.x'),
            ('d',u'Unknow'),)
    idc_choice = (
            ('a',u'蓝汛'),
            ('b',u'森华'),
            )
    app_choice = (
            ('a',u'web'),
            ('b',u'DB'),
            ('c',u'ha'),
            ('d',u'Unknow'),)
    device = models.CharField(u'设备型号',choices = dev_choice,max_length=10)
    hostname = models.CharField(u'主机名',max_length=20)
    ip = models.IPAddressField()
    hardware = models.CharField(u'设备信息',max_length=256)
    idc = models.CharField(u'IDC',choices = idc_choice,max_length = 8)
    start = models.DateField(u'上架时间',max_length=20)
    services = models.CharField(u'服务',choices=app_choice,max_length=20)
    otime = models.CharField(u'过保时间',max_length=20)
    user_name = models.ManyToManyField(Users)

    def __unicode__(self):
        return u'%s %s' % (self.hostname,self.ip)



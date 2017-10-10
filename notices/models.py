# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Notice(models.Model):
    	#author = models.ForeignKey('auth.User')
	#id = models.AutoField(primary_key=True)
	subject = models.CharField(max_length=250)
	content = models.TextField(blank=True,null=True)
	created_at = models.DateTimeField(default=timezone.now)
	post_at = models.DateTimeField(blank=True, null=True)
	schoolid = models.CharField(max_length=250,blank=True,null=True)
	subjectid = models.CharField(max_length=50,blank=True,null=True)
	studentid = models.CharField(max_length=50,blank=True,null=True)
	def publish(self):
		self.created_at = timezone.now()
		self.save()
	def __str__(self):
		return self.subject



# Create your models here.

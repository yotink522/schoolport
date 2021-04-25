from http.client import CannotSendHeader
from django.contrib.auth.models import AbstractUser
from django.core.validators import BaseValidator
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from schoolport.users.models import User

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# 학교테이블 : TB_School
class TB_School(models.Model):
    #school_no = models.BigAutoField(help_text="School No", primary_key=True)    # Primary Key
    name = models.CharField(_("Name of School"), max_length=255)                #학교이름
    address = models.CharField(_("Name of School"), max_length=255)             #학교주소

    def __str__(self):
        pass

# 강좌테이블 : TB_Course
# e,g) 수학강좌, 물리강좌, 화학강좌, ...
class TB_Course(models.Model):
    #course_no = models.BigAutoField(help_text="School No", primary_key=True)    # Primary Key
    course_name = models.CharField(_("Name of Course"), max_length=255)        # 강좌이름
    
    school_no = models.ForeignKey(TB_School, related_name="fcourse_schoolno", on_delete=models.DO_NOTHING) # 학교테이블의 Primary Key

    def __str__(self):
        pass

# 학급테이블 : TB_Class
# e,g) 1학년 1반, 2학년 2반, ...
class TB_Class(models.Model):
    #class_no = models.BigAutoField(help_text="Class No", primary_key=True)     # Primary Key
    class_grade = models.IntegerField()                                         # 학년
    class_index = models.IntegerField()                                         # 반
    student_nums = models.IntegerField()                                        # 재적인원
    
    teacher_no = models.ForeignKey(User, related_name="fclass_userno", on_delete=models.DO_NOTHING)        # 담임교원
    school_no = models.ForeignKey(TB_School, related_name="fclass_schoolno", on_delete=models.DO_NOTHING)  # 학교테이블의 Primary Key

    def __str__(self):
        pass

# 학생테이블 : TB_Student
# e,g) 1학년 1반, 2학년 2반, ...
class TB_Student(models.Model):
    #student_no = models.BigAutoField(help_text="Student No", primary_key=True)                          # Primary Key
    name = models.CharField(_("Student Name"), max_length=255)                                          # 학생이름
    gender = models.CharField(_("Student Gender"), blank=True, choices=GENDER_CHOICES, max_length=20)   # 성별
    age = models.IntegerField()                                                                         # 나이
    address = models.CharField(_("Home Address"), max_length=255)                                       # 집주소
    birthday = models.DateField(null=True, blank=True)                                                  # 생일
    
    class_no = models.ForeignKey(TB_Class, related_name="fstudent_classno", on_delete=models.DO_NOTHING)    # 학급
    parent_no = models.ForeignKey(User, related_name="fstudent_userno", on_delete=models.DO_NOTHING)        # 부모
    def __str__(self):
        pass


# 학교운수기재테이블 : TB_School_Vehicle
# e,g) 
class TB_Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=255)                                          # 차종류, (소형뻐스, 중형뻐스,...)
    vehicle_number = models.CharField(max_length=255)                                        # 차량번호
    size = models.IntegerField()                                                             # 좌석수
    purchase_price = models.IntegerField()                                                   # 구입가격

    school_no = models.ForeignKey(TB_School, related_name="fvehicle_schoolno", on_delete=models.DO_NOTHING)  # 학교테이블의 Primary Key
    def __str__(self):
        pass

# 학교물품테이블 : TB_School_Goods
# e,g) 
class TB_School_Goods(models.Model):
    goods_type = models.CharField(max_length=255)                                          # 물품형태, (교과서, 학용품, ...)
    goods_name = models.CharField(max_length=255)                                          # 물품이름 

    school_no = models.ForeignKey(TB_School, related_name="fgoods_schoolno", on_delete=models.DO_NOTHING)  # 학교테이블의 Primary Key
    def __str__(self):
        pass


# 광고테이블 : TB_Advertise
# e,g) 
class TB_Advertise(models.Model):
    title = models.CharField(max_length=255)                                          # 광고이름
    url = models.CharField(max_length=1024)                                          # 광고URL

    def __str__(self):
        pass


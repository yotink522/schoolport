from http.client import CannotSendHeader
from django.contrib.auth.models import AbstractUser
from django.core.validators import BaseValidator, EMPTY_VALUES
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
from schoolport.app_core.models_baseparams import *

GENDER_CHOICES = [
    ('M', 'Boy'),
    ('F', 'Girl'),
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
    course_name = models.CharField(_("Name of Course"), max_length=255)         # 강좌이름
    course_type = models.CharField(_("Course Type"), max_length=50, null=True, default=EMPTY_VALUES)            # 강좌이름
    price = models.FloatField(null=True)                                       # 가격
    price_unit = models.CharField(null=True, max_length=50)                    # per day, Month, Year
    price_currency = models.CharField(null=True, max_length=20)                # Yuan, USD, ...

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
    name = models.CharField(_("Student Name"), max_length=255, null=True)                                          # 학생이름
    #gender = models.CharField(_("Student Gender"), blank=True, choices=GENDER_CHOICES, max_length=20)   # 성별
    gender = models.CharField(_("Student Gender"), blank=True, max_length=20)   # 성별
    age = models.IntegerField(null=True)                                                                         # 나이
    address = models.CharField(_("Home Address"), max_length=255, null=True)                                       # 집주소
    birthday = models.DateField(null=True, blank=True)                                                  # 생일
    schoolname = models.CharField(_("School Name"), max_length=255, null=True)                          # 학교이름
    parent_type = models.CharField(_("Parent Type"), max_length=20, null=True)                          # 부모종류 1
    parent_phone_no = models.CharField(_("Parent Phone No"), max_length=20, null=True)                  # 부모전화번호 1
    alt_parent_type = models.CharField(_("Alt Parent Type"), max_length=20, null=True)                      # 부모종류 2
    alt_parent_phone_no = models.CharField(_("Alt Parent Phone No"), max_length=20, null=True)              # 부모전화번호 2
    remarks = models.CharField(_("Remarks"), max_length=255, null=True)

    class_no = models.ForeignKey(TB_Class, related_name="fstudent_classno", on_delete=models.DO_NOTHING, db_column="class_no", null=True)    # 학급
    parent_no = models.ForeignKey(User, related_name="fstudent_userno", on_delete=models.DO_NOTHING, db_column="parent_no", null=True)        # 부모
    sourceofstudent_no = models.ForeignKey(TB_Param_SourceOfStudent, related_name="fstudent_sourceofstudentno", on_delete=models.DO_NOTHING, db_column="sourceofstudent_no", null=True)  # TB_Param_SourceOfStudent ForeignKey
    grade_no = models.ForeignKey(TB_Param_Grade, related_name="fstudent_gradeno", on_delete=models.DO_NOTHING, db_column="grade_no", null=True)        # 학년 TB_Param_Grade ForeignKey

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


# 아이템테이블 : TB_Items
class TB_Items(models.Model):
    item_name = models.CharField(max_length=255)
    unit_price = models.FloatField()
    currency = models.CharField(max_length=10, default='CNY')
    stock_amount = models.IntegerField()
    status = models.IntegerField()  #0: disabled, 1: enabled
    
    def __str__(self):
        return self.item_name

#아이템 ChangeLog 테이블:
class TB_Items_Changelogs(models.Model):
    adjust_username = models.CharField(max_length=50)
    adjust_detail = models.CharField(max_length=512)
    entry_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    item_no = models.ForeignKey(TB_Items, related_name="f_itemno", on_delete=models.DO_NOTHING, null=True, db_column="item_no")  
    
    def __str__(self):
        return self.adjust_username + ':' + str(self.entry_date)

# 아이템테이블 : TB_Items
class TB_Fees(models.Model):
    fee_name = models.CharField(max_length=255)
    unit_price = models.FloatField()
    currency = models.CharField(max_length=10, default='CNY')
    status = models.IntegerField()  #0: disabled, 1: enabled
    
    def __str__(self):
        return self.fee_name
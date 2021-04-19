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
    
    school_no = models.ForeignKey(TB_School, related_name="p_school_no", on_delete=models.DO_NOTHING) # 학교테이블의 Primary Key

    def __str__(self):
        pass

# 학급테이블 : TB_Class
# e,g) 1학년 1반, 2학년 2반, ...
class TB_Class(models.Model):
    #class_no = models.BigAutoField(help_text="Class No", primary_key=True)     # Primary Key
    class_grade = models.IntegerField()                                         # 학년
    class_index = models.IntegerField()                                         # 반
    student_nums = models.IntegerField()                                        # 재적인원
    #teacher_no =                                                                  # 담임교원

    school_no = models.ForeignKey(TB_School, related_name="a_school_no", on_delete=models.DO_NOTHING)  # 학교테이블의 Primary Key

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
    
    class_no = models.ForeignKey(TB_Class, related_name="class_no", on_delete=models.DO_NOTHING)    # 학급

    def __str__(self):
        pass


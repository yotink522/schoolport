from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# 어떤 경로를 통하여 이체계에 가입하게 되였는지를 가지고있는 기초파라메터 테이블
class TB_Param_SourceOfStudent(models.Model):
    source_name_en = models.CharField(_("Student Name EN"), max_length=255, null=True)
    source_name_zh = models.CharField(_("Student Name ZH"), max_length=255, null=True)
    source_name_ko = models.CharField(_("Student Name KO"), max_length=255, null=True)

    def __str__(self):
        return self.source_name_en

# 부모타입정보 기초파라메터테이블
class TB_Param_ParentType(models.Model):
    parent_type = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.parent_type

# 학년정보 기초파라메터테이블
class TB_Param_Grade(models.Model):
    grade_desc = models.CharField(_("Grade Name"), max_length=255, null=True)
    def __str__(self):
        return self.grade_desc


# 강좌정보 기초파라메터테이블
class TB_Param_Course(models.Model):
    course_name = models.CharField(_("Name of Course"), max_length=255)                   # 강좌이름
    course_type = models.CharField(_("Course Type"), max_length=50, null=True)            # 강좌이름
    price = models.FloatField(null=True)                                                  # 가격
    price_unit = models.CharField(null=True, max_length=50)                               # per day, Month, Year
    price_currency = models.CharField(null=True, max_length=20)                           # Yuan, USD, ...

    def __str__(self):
        return self.course_name


# 가격종류테이블 실례) 100USD/Month, 1000USD/Year, ...
class TB_Price_Standards(models.Model):
    price = models.IntegerField(null=True)
    price_currency = models.CharField(null=True, max_length=20)         # Yuan, USD, ...
    price_unit = models.CharField(null=True, max_length=50)             # Month, Year, Day

    course_id = models.ForeignKey(TB_Param_Course, null=True, related_name="fk_param_course_id", on_delete=models.DO_NOTHING, db_column="course_id")
    
    def __str__(self):
        return str(self.price) + '/' + self.price_unit

# 아이템정보 기초파라메터테이블
class TB_Param_Items(models.Model):
    item_name = models.CharField(max_length=255)                        # 비품이름
    item_quantity = models.IntegerField(null=True)                      # 수량
    price = models.FloatField(null=True)                                # 가격
    price_unit = models.CharField(null=True, max_length=50)             # per day, Month, Year
    price_currency = models.CharField(null=True, max_length=20)         # Yuan, USD, ...

    def __str__(self):
        return self.item_name

# Fee정보 기초파라메터테이블
class TB_Param_Fees(models.Model):
    fee_name = models.CharField(max_length=255)                        # FeeName
    price = models.FloatField(null=True)                                # 가격
    price_currency = models.CharField(null=True, max_length=20)         # Yuan, USD, ...

    def __str__(self):
        return self.fee_name




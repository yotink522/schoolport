from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from schoolport.app_core.models import *


class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TB_Student
        fields = (
            'name',
            'gender',
            'birthday',
            'schoolname',
            'parent_type',
            'parent_phone_no',
            'address',
            'alt_parent_type',
            'alt_parent_phone_no',

            'grade_no',
            'sourceofstudent_no',
        )

class AddItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TB_Items
        fields = (
            'item_name',
            'unit_price',
            'currency',
            'stock_amount',
            'status',
        )

class AddFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TB_Fees
        fields = (
            'fee_name',
            'unit_price',
            'currency',
            'status',
        )

class AddCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TB_Course
        fields = (
            'course_name',
            'type',
            'course_type',
            'class_schedule_color',
            'price_hour',
            'price_hour_status',
            'price_month',
            'price_month_status',
            'currency',
            'course_status',
            'number_of_students',
            'pricing_standard_nos',
            'deduction_rule1',
            'deduction_rule2',
            'remarks',
        )

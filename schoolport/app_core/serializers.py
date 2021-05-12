from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from schoolport.app_core.models import *
from schoolport.app_core.models_baseparams import *

class TB_Price_Standards_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TB_Price_Standards
        #fields = ("param_course_no", "price", "price_currency", "price_unit")
        fields = '__all__'

class TB_Param_Course_Serializer(serializers.ModelSerializer):
    price_standards = TB_Price_Standards_Serializer(many=True, read_only=True)

    class Meta:
        model = TB_Param_Course
        fields = ("course_name", "course_type", "price", "price_unit", "price_standards", "price_currency")


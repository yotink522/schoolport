from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from django.views.generic.base import TemplateResponseMixin
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.core import serializers as core_serializers
from rest_framework import serializers as rest_serializers

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json, datetime
from rest_framework.parsers import JSONParser

from schoolport.app_core.models_baseparams import *
from schoolport.app_core.serializers import * 
from schoolport.app_billing.serializers import *

# Create your views here.
class BillingCenter_Index_View(View):
    template_name = "app_billing/index.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)
        
# Register Student View
class BillingCenter_RegisterStudent_View(View):
    template_name = "app_billing/registerstudent.html"
    data = dict()
    
    def get(self, request):
        parent_type_list = TB_Param_ParentType.objects.all()
        source_of_student_list = TB_Param_SourceOfStudent.objects.all()
        grade_list = TB_Param_Grade.objects.all()
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'registerstudent',

            'parent_type_list': parent_type_list,
            'source_of_student_list' : source_of_student_list,
            "grade_list" : grade_list
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {"parent_type_list": parent_type_list, 
                                                                            "source_of_student_list": source_of_student_list,
                                                                            "grade_list" : grade_list })
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Courses and Fee Index View
class BillingCenter_CoursesFee_View(View):
    template_name = "app_billing/courses_fee.html"
    data = dict()

    def get(self, request):

        course_list = TB_Course.objects.all().order_by('id')
        item_list = TB_Items.objects.all().order_by('id')
        fee_list = TB_Fees.objects.all().order_by('id')

        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'coursesfee',
            
            'course_list' : course_list,
            'item_list' : item_list,
            'fee_list' : fee_list
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {'course_list': course_list, 'item_list':item_list, 'fee_list': fee_list})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Courses and Fee Edit View
class BillingCenter_CoursesFeeEdit_View(View):
    template_name = "app_billing/courses_fee_edit.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'coursesfeeedit',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Courses and Fee Edit View
class BillingCenter_CoursesFeeGeneralEdit_View(View):
    template_name = "app_billing/courses_fee_generaledit.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'coursesfeegeneraledit',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Charge per Notice View
class BillingCenter_ChargePerNoticeIndex_View(View):
    template_name = "app_billing/charge_per_notice.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'chargepernotice',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)


# Scancode Index View
class BillingCenter_ScanCodeIndex_View(View):
    template_name = "app_billing/pay_charge.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'scancodetocharge',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Scancode Index View
class BillingCenter_ScanCodeAddChargeQRCode_View(View):
    template_name = "app_billing/pay_charge_add.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'scancodetocharge_addchgqrcode',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Scancode Index View
class BillingCenter_ScanCodeConsolidate(View):
    template_name = "app_billing/pay_charge_consolidate.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'scancodetocharge_consolidate',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_ScanCodeProjectDetail(View):
    template_name = "app_billing/pay_charge_projectdetail.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'scancodetocharge_projectdetail',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_PaymentTransactions(View):
    template_name = "app_billing/pay_breakeven.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'payment_transactionlog',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_ClassManagement(View):
    template_name = "app_billing/pay_classM.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'classmanagement',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_ClassManagement_Add(View):
    template_name = "app_billing/pay_classM_add.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'classmanagement_add',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)            

class BillingCenter_ClassManagement_Edit(View):
    template_name = "app_billing/pay_classM_editBatch.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'classmanagement_edit',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_PaymentReceipt(View):
    template_name = "app_billing/pay_electronicReceipts.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'payment_receipt',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)


class BillingCenter_StudentManagement(View):
    template_name = "app_billing/pay_studentM.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'student_management',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_StudentManagement_AddStudent(View):
    template_name = "app_billing/pay_studentM_add.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'student_management_add',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_FacultyManagement(View):
    template_name = "app_billing/pay_facultyM.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'faculty_management',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_FacultyManagement_AddFaculty(View):
    template_name = "app_billing/pay_facultyM_add.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'faculty_management_add',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_PayRefundRequestIndex(View):
    template_name = "app_billing/pay_refund_request.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'pay_refund_request_index',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_PayRefundRequest_AddBatch(View):
    template_name = "app_billing/pay_refund_request_addBatch.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'pay_refund_request_addbatch',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_PayRefundTransactionLogs(View):
    template_name = "app_billing/pay_refund_viewDetail.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'pay_refund_transaction_logs',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class BillingCenter_PayRevenue(View):
    template_name = "app_billing/pay_revenue_statstics.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'pay_revenue',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)



# AJAX Get Course List View
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_GetCourseList(View):
    datas = dict()
    def get(self, request):
        course_list = TB_Param_Course.objects.all()
        datas = []
        for row in course_list:
            data = {
                "id" : row.id,
                "course_name" : row.course_name,
                "course_type" : row.course_type,
                "price" : row.price
            }
            datas.append(data)    

        #print(json.dumps(datas))
        #self.data['result'] = serializers.serialize('json',object_list)
        resp = {
            "data": datas
        }
        return JsonResponse(resp, safe=False)

    def post(self, request):
        course_ids = json.loads(request.body)
        course_infos = TB_Param_Course.objects.filter(id__in=course_ids) # Select * from TB_Param_Course WHERE id in course_ids
        
        resp_result = list()
        for info in course_infos:
            #print(info.id, info.course_name, info.course_type, info.price, info.price_unit)
            course = dict()
            course['id'] = info.id
            course['course_name'] = info.course_name
            course['course_type'] = info.course_type
            course['price'] = info.price
            course['price_unit'] = info.price_unit

            price_standards = TB_Price_Standards.objects.select_related('course_id').filter(course_id=info.id)
            course['pricing_standards'] = core_serializers.serialize('json', price_standards)
            
            resp_result.append(course)

        return JsonResponse(json.dumps(resp_result), safe=False)
            

# AJAX Get Item List View
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_GetItemList(View):
    datas = dict()
    def get(self, request):
        item_list = TB_Param_Items.objects.all()
        datas = []
        for row in item_list:
            data = {
                "id" : row.id,
                "item_name" : row.item_name,
                "item_quantity" : row.item_quantity,
                "price" : row.price
            }
            datas.append(data)    

        resp = {
            "data": datas
        }
        return JsonResponse(resp, safe=False)

    def post(self, request):
        item_ids = json.loads(request.body)
        item_infos = TB_Param_Items.objects.filter(id__in=item_ids) # Select * from TB_Param_Items WHERE id in item_ids
        
        resp = core_serializers.serialize('json', item_infos) # 모델로부터 쿼리한 오브젝트를 JSON객체로 변환하기 
        return JsonResponse(resp, safe=False)

# AJAX Get Fee List View
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_GetFeeList(View):
    datas = dict()
    def get(self, request):
        fee_list = TB_Param_Fees.objects.all()
        datas = []
        for row in fee_list:
            data = {
                "id" : row.id,
                "fee_name" : row.fee_name,
                "price" : row.price
            }
            datas.append(data)    

        resp = {
            "data": datas
        }
        return JsonResponse(resp, safe=False)

    def post(self, request):
        fee_ids = json.loads(request.body)
        fee_infos = TB_Param_Fees.objects.filter(id__in=fee_ids) # Select * from TB_Param_Items WHERE id in item_ids
        
        resp = core_serializers.serialize('json', fee_infos) # 모델로부터 쿼리한 오브젝트를 JSON객체로 변환하기 
        return JsonResponse(resp, safe=False)

# AJAX Get Fee List View
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_AddStudent(View):
    def get(self, request):
        pass

    def post(self, request):
        student_serializer = AddStudentSerializer(data = json.loads(request.body))
        if student_serializer.is_valid(raise_exception=True):
            resp = "OK";    
            student_serializer.save()
        else:
            resp = "Fail";
        return JsonResponse(resp, safe=False)


# AJAX CourseFee페지에서 NewItem처리부분
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_AddItem(View):
    def get(self, request):
        pass

    def post(self, request):
        item_serializer = AddItemSerializer(data = json.loads(request.body))
        if item_serializer.is_valid(raise_exception=True):
            item_serializer.save()
        
        item_list = TB_Items.objects.all().order_by('id')
        resp = core_serializers.serialize('json', item_list)
        return JsonResponse(resp, safe=False)
        #return JsonResponse(json.dumps(resp), safe=False)

# AJAX CourseFee페지에서 EditItem처리부분
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_EditItem(View):
    def get(self, request):
        pass

    def post(self, request):
        print(request.user)
        post_data = json.loads(request.body)
        
        #------------ item_id로 아이템정보를 TB_Items로부터 얻어와서 POST로 들어온 값으로 갱신하기------------#
        item = TB_Items.objects.get(id=post_data['item_id'])
        adjust_detail = "Changed infos: Unit Price " + str(item.unit_price) + "->" + str(post_data['item_unitprice'] ) + ",Quantity " + str(item.stock_amount) + "->" + str(post_data['item_quantity']) + ",Item Name '" + str(item.item_name) +"'->'" + str(post_data['item_name'])+"'"
        item.item_name =post_data['item_name'] 
        item.unit_price =post_data['item_unitprice'] 
        item.stock_amount =post_data['item_quantity'] 
        item.save()
        
        
        #--------------TB_Items_Changelogs에 log자료 추가하기 --------------------------#
        TB_Items_Changelogs.objects.create(
            adjust_username = request.user, #현재 로그인된 사용자이름
            adjust_detail = adjust_detail,
            item_no=item 
        )

        item_list = TB_Items.objects.all().order_by('id')
        resp = core_serializers.serialize('json', item_list)
        return JsonResponse(resp, safe=False)

# AJAX CourseFee페지에서 DeleteItem처리부분
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_DeleteItem(View):
    def get(self, request):
        pass

    def post(self, request):
        post_data = json.loads(request.body)
        item_id = post_data['item_id']
        item = TB_Items.objects.get(id=item_id)
        item.delete()

        return JsonResponse("Okay", safe=False)
        #return JsonResponse(json.dumps(resp), safe=False)


# AJAX CourseFee페지에서 NewFee처리부분
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_AddFee(View):
    def post(self, request):
        fee_serializer = AddFeeSerializer(data = json.loads(request.body))
        if fee_serializer.is_valid(raise_exception=True):
            fee_serializer.save()
        
        fee_list = TB_Fees.objects.all().order_by('id')
        resp = core_serializers.serialize('json', fee_list)
        return JsonResponse(resp, safe=False)

# AJAX CourseFee페지에서 DeleteItem처리부분
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_DeleteFee(View):
    def get(self, request):
        pass

    def post(self, request):
        post_data = json.loads(request.body)
        fee_id = post_data['fee_id']
        fee = TB_Fees.objects.get(id=fee_id)
        fee.delete()

        return JsonResponse("Okay", safe=False)

# AJAX CourseFee페지에서 EditFee처리부분
@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_EditFee(View):
    def post(self, request):
        post_data = json.loads(request.body)
        
        #------------ fee_id로 아이템정보를 TB_Fees로부터 얻어와서 POST로 들어온 값으로 갱신하기------------#
        fee = TB_Fees.objects.get(id=post_data['fee_id'])
        fee.fee_name =post_data['fee_name'] 
        fee.unit_price =post_data['fee_unitprice'] 
        fee.save()
        
        fee_list = TB_Fees.objects.all().order_by('id')
        resp = core_serializers.serialize('json', fee_list)
        return JsonResponse(resp, safe=False)

@method_decorator(csrf_exempt, name='dispatch') 
class Ajax_CourseFee_AddCourse(View):
    def post(self, request):
        course_serializer = AddCourseSerializer(data = json.loads(request.body))
        if course_serializer.is_valid(raise_exception=True):
            course_serializer.save()

        return JsonResponse("OK", safe=False)

from django.urls import path
from schoolport.app_billing import views
#from schoolport.app_billing.views import ajax_get_courselist

from django.contrib.auth.decorators import login_required

app_name = "app_billing"
urlpatterns = [
    path('billingcenter/', login_required(views.BillingCenter_Index_View.as_view()), name='billingcenter-index'),
    path('billingcenter/registerstudent', login_required(views.BillingCenter_RegisterStudent_View.as_view()), name='billingcenter-register-student'),
    path('billingcenter/coursesfee', login_required(views.BillingCenter_CoursesFee_View.as_view()), name='billingcenter-courses-fee'),
    path('billingcenter/coursesfee_edit', login_required(views.BillingCenter_CoursesFeeEdit_View.as_view()), name='billingcenter-courses-fee-edit'),
    path('billingcenter/coursesfee_general_edit', login_required(views.BillingCenter_CoursesFeeGeneralEdit_View.as_view()), name='billingcenter-courses-fee-general-edit'),
    path('billingcenter/charge_per_notice', login_required(views.BillingCenter_ChargePerNoticeIndex_View.as_view()), name='billingcenter-charge-per-notice-index'),
    
    path('billingcenter/scancode', login_required(views.BillingCenter_ScanCodeIndex_View.as_view()), name='billingcenter-scancode-index'),
    path('billingcenter/scancode/add_chg_qrcode', login_required(views.BillingCenter_ScanCodeAddChargeQRCode_View.as_view()), name='billingcenter-scancode-addchargeQRCode'),
    path('billingcenter/scancode/consolidate', login_required(views.BillingCenter_ScanCodeConsolidate.as_view()), name='billingcenter-scancode-consolidate'),
    path('billingcenter/scancode/projectdetail', login_required(views.BillingCenter_ScanCodeProjectDetail.as_view()), name='billingcenter-scancode-projectdetail'),
    path('billingcenter/payment_transactions', login_required(views.BillingCenter_PaymentTransactions.as_view()), name='billingcenter-paytransactionlogs'),
    path('billingcenter/classmanagement', login_required(views.BillingCenter_ClassManagement.as_view()), name='billingcenter-classmanagement'),
    path('billingcenter/classmanagement/add', login_required(views.BillingCenter_ClassManagement_Add.as_view()), name='billingcenter-classmanagement-add'),
    #path('billingcenter/classmanagement/import', login_required(views.BillingCenter_ClassManagement_Import.as_view()), name='billingcenter-classmanagement-import'),
    path('billingcenter/classmanagement/edit', login_required(views.BillingCenter_ClassManagement_Edit.as_view()), name='billingcenter-classmanagement-edit'),
    path('billingcenter/payment_receipt', login_required(views.BillingCenter_PaymentReceipt.as_view()), name='billingcenter-payment-receipt'),
    path('billingcenter/studentmanagement', login_required(views.BillingCenter_StudentManagement.as_view()), name='billingcenter-student-managements'),
    path('billingcenter/studentmanagement/add', login_required(views.BillingCenter_StudentManagement_AddStudent.as_view()), name='billingcenter-student-managements-addstudent'),
    path('billingcenter/facultymanagement', login_required(views.BillingCenter_FacultyManagement.as_view()), name='billingcenter-faculty-managements'),
    path('billingcenter/facultymanagement/add', login_required(views.BillingCenter_FacultyManagement_AddFaculty.as_view()), name='billingcenter-faculty-managements-addfaculty'),
    path('billingcenter/payrefundrequest', login_required(views.BillingCenter_PayRefundRequestIndex.as_view()), name='billingcenter-pay-refundrequest'),
    path('billingcenter/payrefundrequest/addBatch', login_required(views.BillingCenter_PayRefundRequest_AddBatch.as_view()), name='billingcenter-pay-refundrequest-addbatch'),
    path('billingcenter/refundlist', login_required(views.BillingCenter_PayRefundTransactionLogs.as_view()), name='billingcenter-pay-refund-details'),
    path('billingcenter/revenue', login_required(views.BillingCenter_PayRevenue.as_view()), name='billingcenter-pay-revenue'),

    #------------------AJAX REQUEST URLS 정의부---------------------#
    path('billingcenter/get_course_list', views.Ajax_GetCourseList.as_view(), name="billingcenter-ajax-getcourselist"),
    path('billingcenter/get_item_list', views.Ajax_GetItemList.as_view(), name="billingcenter-ajax-getitemlist"),
    path('billingcenter/get_fee_list', views.Ajax_GetFeeList.as_view(), name="billingcenter-ajax-getfeelist"),
    path('billingcenter/add_student', views.Ajax_AddStudent.as_view(), name="billingcenter-ajax-addstudent"),
    
    path('billingcenter/add_item', views.Ajax_CourseFee_AddItem.as_view(), name="billingcenter-ajax-coursefee-additem"),
    path('billingcenter/edit_item', views.Ajax_CourseFee_EditItem.as_view(), name="billingcenter-ajax-coursefee-edititem"),
    path('billingcenter/delete_item', views.Ajax_CourseFee_DeleteItem.as_view(), name="billingcenter-ajax-coursefee-deleteitem"),

    path('billingcenter/add_fee', views.Ajax_CourseFee_AddFee.as_view(), name="billingcenter-ajax-coursefee-addfee"),
    path('billingcenter/edit_fee', views.Ajax_CourseFee_EditFee.as_view(), name="billingcenter-ajax-coursefee-editfee"),
    path('billingcenter/delete_fee', views.Ajax_CourseFee_DeleteFee.as_view(), name="billingcenter-ajax-coursefee-deletefee"),

    path('billingcenter/add_course', views.Ajax_CourseFee_AddCourse.as_view(), name="billingcenter-ajax-coursefee-addcourse"),

]


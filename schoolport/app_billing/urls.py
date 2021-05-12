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

]


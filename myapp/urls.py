from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name='predictor'),
    path('employee_create/', views.employee_create, name='employee_create'),
    path('createcrispy/', views.createcrispy, name='createcrispy'),
    path('search_read/', views.search_read, name='search_read'),
    path('employee_search/', views.employee_search, name='employee_search'),
    
    #การแก้ไขและลบข้อมูล
    path('employee/edit/', views.employee_edit, name='emp_edit'),
    path('employee/update/<int:id>/', views.employee_update, name='emp_update'),
    path('employee/delete/<int:id>/', views.employee_delete, name='emp_delete'),
    
    #signin การลงทะเบียนยืนยันรหัสผ่าน
    path('member/signin/', views.member_signin, name='member_signin')
    
]







#re_path(r'pagination/bootstrap/(?P<pg>\d*/?)', views.pagination_bs, name='pg_bs'),
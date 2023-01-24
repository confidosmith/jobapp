from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('job_listing', views.job_listing, name='job_listing'),
    path('job_detail/<str:id>',views.job_detail, name='job_detail'),
    path('post_job',views.post_job, name='post_job'),
    path('newapply', views.newapply, name="newapply"),
    path('employer_signup',views.employer_signup, name='employer_signup'),
    path('employee_signup',views.employee_signup, name='employee_signup'),
    path('delete',views.delete, name='delete'),
    path('employeedelete',views.employeedelete, name='employeedelete'),
    path('search',views.search, name='search'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('employer_dashboard',views.employer_dashboard, name='employer_dashboard'),
    path('employee_dashboard',views.employee_dashboard, name='employee_dashboard'),
    path('applicant',views.applicant, name='applicant'),
    path('application_details',views.application_details, name='application_details'),
    path('update',views.update, name='update'),
]

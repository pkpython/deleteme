from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="helpingRecruiters-home"),
    path('recruiter/views', views.recruiterlist, name="helpingRecruiters-recruiterlist"),
    path('recruiter/add/recruitement', views.addNew, name="helpingRecruiters-addnew"),
    path('job/<int:pk>', views.jobdetail, name="helpingRecruiters-detail"),
    path('recruiter/job/update/<int:pk>', views.jobupdate, name="helpingRecruiters-update"),
    path('recruiter/job/delete/<int:pk>', views.jobdelete, name="helpingRecruiters-delete"),
    path('recruiter/job/confirm/delete/<int:pk>', views.jobdeleteconfirm, name="helpingRecruiters-confirm-delete"),
    
    path('candidate/apply/<int:pk>', views.applynow, name="helpingRecruiters-apply"),
    # path('candidate/all/recruitement', views.index, name="helpingRecruiters-all"),

]
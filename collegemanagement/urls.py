from django.conf.urls import url,include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from cms.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.shortcuts import render
from django.conf import settings

def ErrorPage(request):
    return render(request,'404.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^home$', homepage, name='homepage'),
    url(r'^error/$',ErrorPage, name='error'),
    url(r'^login$',LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^logout$',logoutuser,name='logout'),
    url(r'^accounts/login$', loginFirst, name='loginfirst'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'register$', UserFormView.as_view(), name='register'),
    url(r'index.html$', home, name='index'),
    url(r'^register/student$', StudentFormView.as_view(), name='studentform'),
    url(r'^register/faculty$', FacultyFormView.as_view(), name='teacherform'),
    url(r'^info/(?P<id>[0-9]+)$', Info.as_view(), name='info'),
    url(r'^profile$', myprofile, name='profile'),
    url(r'^list/faculty$', FacultyList.as_view(), name='facultylist'),
    url(r'^list/students$', StudentList.as_view(), name='studentlist'),
    url(r'^student/update/(?P<pk>[\-\d]+)$', StudentUpdate.as_view(), name='studentupdate'),
    url(r'^faculty/update/(?P<pk>[\-\d]+)$', FacultyUpdate.as_view(), name='facultyupdate'),
    url(r'^update/(?P<slug>[\-\w]+)$', UserUpdate.as_view(), name='userupdate'),
    url(r'^request$', LeaveFormView.as_view(), name='newLeave'),
    url(r'^addsubject$', newSubject, name='newSubject'),
    url(r'^selectsubject/(?P<id>[\-\d]+)$', newSelectedSubject, name='selectSubject'),
    url(r'^response$', requestverdict, name='request_verdict'),
    url(r'^RequestList$', RequestList.as_view(), name='RequestList'),
    url(r'^timesheet/(?P<id>[\-\d]+)$', PublicTimesheet, name='publicTimesheet'),
    url(r'^timesheet$', Timesheet, name='timesheet'),
    url(r'^attendance/(?P<subject>[\-\w]+)$', fillAttendance, name='fillAttendance'),
    url(r'^attendance/list/(?P<subject>[\-\w]+)$', viewAttendance , name='viewAttendance'),
    url(r'^(?P<slug>[a-z0-9]+)$', Detail.as_view(), name='detail'),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


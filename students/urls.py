from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'students'

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),
    #re_path(r'^courses/$',views.StudentCourseListView.as_view(), name='student_course_list'),
    re_path(r'^course/(?P<pk>\d+)/$', cache_page(60 *15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    re_path(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$', cache_page(60 *15)(views.StudentCourseDetailView.as_view()),
            name='student_course_detail_module'),
    # path('course/<int:id>/', views.StudentCourseDetailView.as_view(), name='student_course_detail'),
    # path('course/<int:id>/<int:id>/', views.StudentCourseDetailView, name='student_course_detail_module'),
]
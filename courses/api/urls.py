from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('courses/<int:pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
]
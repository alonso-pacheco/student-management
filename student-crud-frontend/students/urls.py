from django.urls import include, re_path, path
from .views import Index, Student

app_name = 'students'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('students/', Student.as_view(), name='student'),
    path('students/<int:id>/', Student.as_view(), name='student_form'),
]
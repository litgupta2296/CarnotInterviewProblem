from django.contrib import admin
from django.urls import path,include
from student_details.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/form/',load_search_form,name='search-form'),
    path('student_details/',get_student_data_from_form,name='get-data'),
    path('students/<student_id>/',get_student_data,name='student-data'),
    path('add-student',csrf_exempt(add_student_data),name="student_data")
]

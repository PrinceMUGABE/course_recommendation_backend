from django.urls import path
from .views import (
    add_student,
    update_student,
    delete_student,
    find_all_students,
    find_student_by_id,
    find_student_by_rol_no,
    find_students_by_course,
    find_students_by_marks,
    download_all_students_pdf,
    download_all_students_excel,
    download_student_pdf,
    download_student_excel
)

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('update/<int:pk>/', update_student, name='update_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
    path('find_all/', find_all_students, name='find_all_students'),
    path('find_by_id/<int:pk>/', find_student_by_id, name='find_student_by_id'),
    path('find_by_rol_no/<str:rol_no>/', find_student_by_rol_no, name='find_student_by_rol_no'),
    path('find_by_course/<str:course_code>/', find_students_by_course, name='find_students_by_course'),
    path('find_by_marks/<str:marks>/', find_students_by_marks, name='find_students_by_marks'),
    path('download_all_pdf/', download_all_students_pdf, name='download_all_students_pdf'),
    path('download_all_excel/', download_all_students_excel, name='download_all_students_excel'),
    path('download_pdf/<str:rol_no>/', download_student_pdf, name='download_student_pdf'),
    path('download_excel/<int:pk>/', download_student_excel, name='download_student_excel'),
]

from django.urls import path
from .views import download_selected_courses_excel
from .views import download_selected_courses_pdf

from .views import (
    add_course,
    display_all_courses,
    update_course,
    delete_course,
    total_course_count,
    search_course_by_code,
    search_course_by_name,
    list_course_by_level,
    display_courses_by_total_marks,
    download_all_courses_pdf,
    download_all_courses_excel,
    generate_random_course,
)

urlpatterns = [
    path('add/', add_course, name='add-course'),
    path('courses/', display_all_courses, name='display-all-courses'),
    path('update/<int:pk>/', update_course, name='update-course'),
    path('delete/<int:pk>/', delete_course, name='delete-course'),
    path('total-count/', total_course_count, name='total-course-count'),
    path('search/code/<str:course_code>/', search_course_by_code, name='search-course-by-code'),
    path('search/name/<str:course_name>/', search_course_by_name, name='search-course-by-name'),
    path('list/level/<str:level>/', list_course_by_level, name='list-course-by-level'),
    path('display-by-marks/', display_courses_by_total_marks, name='display-courses-by-marks'),
    path('download-pdf/', download_all_courses_pdf, name='download-all-courses-pdf'),
    path('download-excel/', download_all_courses_excel, name='download-all-courses-excel'),
    path('generate-random-course/', generate_random_course, name='generate-random-course'),
     path('download-selected-excel/', download_selected_courses_excel, name='download-selected-courses-excel'),
     path('download-selected-pdf/', download_selected_courses_pdf, name='download-selected-courses-pdf'),
]

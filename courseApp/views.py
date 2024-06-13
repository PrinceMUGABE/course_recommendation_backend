import random
import string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def display_all_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return Response(status=204)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def total_course_count(request):
    count = Course.objects.count()
    return Response({"count": count})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_course_by_code(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    serializer = CourseSerializer(course)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_course_by_name(request, course_name):
    courses = Course.objects.filter(course_name__icontains=course_name)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_course_by_level(request, level):
    courses = Course.objects.filter(level=level)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_courses_by_total_marks(request):
    courses = Course.objects.order_by('-total_marks')
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)



from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_selected_courses_excel(request):
    selected_courses = request.GET.getlist('course_ids')
    courses = Course.objects.filter(id__in=selected_courses)

    # Generate Excel
    df = pd.DataFrame(list(courses.values()))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="selected_courses.xlsx"'
    df.to_excel(response, index=False)
    
    return response



@api_view(['GET'])
def generate_random_course(request):
    # Generate random course code
    random_course_code = ''.join(random.choices(string.ascii_uppercase, k=3)) + str(random.randint(1, 999)).zfill(3)

    # Choose a random level
    levels = ['A', 'B', 'C', 'D']
    random_level = random.choice(levels)

    # Generate random total marks
    random_total_marks = random.randint(50, 100)

    # Create the course
    course = Course.objects.create(
        course_name="Random Course",
        course_code=random_course_code,
        level=random_level,
        total_marks=random_total_marks
    )

    # Serialize and return the generated course
    serializer = CourseSerializer(course)
    return Response(serializer.data)



from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import pandas as pd

@api_view(['GET'])
@permission_classes([IsAdminUser])
def download_all_courses_pdf(request):
    courses = Course.objects.all()
    
    # Generate PDF
    response_pdf = HttpResponse(content_type='application/pdf')
    response_pdf['Content-Disposition'] = 'attachment; filename="all_courses.pdf"'

    doc = SimpleDocTemplate(response_pdf, pagesize=letter)
    elements = []

    data = [['Course Name', 'Course Code', 'Level', 'Total Marks', 'Created Date']]
    for course in courses:
        data.append([
            course.course_name,
            course.course_code,
            course.get_level_display(),
            course.total_marks,
            course.created_date.strftime("%Y-%m-%d %H:%M:%S")
        ])

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    doc.build(elements)
    
    return response_pdf

@api_view(['GET'])
@permission_classes([IsAdminUser])
def download_all_courses_excel(request):
    courses = Course.objects.all()
    
    # Generate Excel
    df = pd.DataFrame(list(courses.values()))
    response_excel = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response_excel['Content-Disposition'] = 'attachment; filename="all_courses.xlsx"'
    df.to_excel(response_excel, index=False)
    
    return response_excel


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_selected_courses_pdf(request):
    selected_courses = request.GET.getlist('course_ids')
    courses = Course.objects.filter(id__in=selected_courses)

    # Generate PDF
    response_pdf = HttpResponse(content_type='application/pdf')
    response_pdf['Content-Disposition'] = 'attachment; filename="selected_courses.pdf"'

    doc = SimpleDocTemplate(response_pdf, pagesize=letter)
    elements = []

    data = [['Course Name', 'Course Code', 'Level', 'Total Marks', 'Created Date']]
    for course in courses:
        data.append([
            course.course_name,
            course.course_code,
            course.get_level_display(),
            course.total_marks,
            course.created_date.strftime("%Y-%m-%d %H:%M:%S")
        ])

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    doc.build(elements)
    
    return response_pdf

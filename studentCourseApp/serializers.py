# from rest_framework import serializers
# from .models import StudentRegistration as Student

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'



# studentCourseApp/serializers.py
from rest_framework import serializers
from userApp.models import User
from .models import StudentRegistration
from courseApp.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'total_marks']



class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = StudentRegistration
        fields = ['id','course', 'marks', 'created_date']


class UserSerializer(serializers.ModelSerializer):
    registrations = StudentSerializer(source='studentregistration_set', many=True)

    class Meta:
        model = User
        fields = ['id', 'rol_no', 'registrations']
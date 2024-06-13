
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userApp.urls')),
    path('course/', include('courseApp.urls')),
    # path('student/', include('studentApp.urls')),
    path('student/', include('studentCourseApp.urls')),
]

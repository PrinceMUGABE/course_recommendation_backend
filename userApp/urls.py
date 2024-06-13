from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    index, signup, login, logout, list_users, get_user_by_id, get_user_by_email,
    get_user_by_rol_no, update_user, delete_user, get_users_by_first_name,
    get_users_by_last_name, get_user_count, download_users_pdf, download_users_excel,
    user_increase_statistics
)

urlpatterns = [
    path('', index, name='welcome'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', list_users, name='list-users'),
    path('users/<int:user_id>/', get_user_by_id, name='get-user-by-id'),
    path('users/email/<str:email>/', get_user_by_email, name='get-user-by-email'),
    path('users/rol_no/<str:rol_no>/', get_user_by_rol_no, name='get-user-by-rol-no'),
    path('users/update/<int:user_id>/', update_user, name='update-user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete-user'),
    path('users/firstname/<str:first_name>/', get_users_by_first_name, name='get-users-by-first-name'),
    path('users/lastname/<str:last_name>/', get_users_by_last_name, name='get-users-by-last-name'),
    path('users/count/', get_user_count, name='get-user-count'),
    path('users/download/pdf/', download_users_pdf, name='download-users-pdf'),
    path('users/download/excel/', download_users_excel, name='download-users-excel'),
    path('users/increase-statistics/', user_increase_statistics, name='user-increase-statistics'),
]

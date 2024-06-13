from datetime import timedelta
from time import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import random
import string
from django.core.mail import send_mail

@api_view(['GET'])
def index(request):
    return Response({"message": "Welcome to the User Management System"}, status=status.HTTP_200_OK)



from django.core.mail import send_mail, BadHeaderError

@api_view(['POST'])
def signup(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    
    last_user = User.objects.all().order_by('id').last()
    new_rol_no = str(last_user.id + 1).zfill(5) if last_user else '00001'
    password = ''.join(random.choices(string.digits, k=6))
    
    user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, rol_no=new_rol_no, password=password)
    
    try:
        send_mail(
            'Your Account Details',
            f'Hello {first_name},\nYour Account Details are:\nRol_No: {new_rol_no},\nPassword: {password}\nYou can use these details to access your courses.\nRegards.',
            'admin@example.com',
            [email],
            fail_silently=False,
        )
    except BadHeaderError:
        return Response({"message": "Invalid header found."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({"rol_no": new_rol_no, "password": password}, status=status.HTTP_201_CREATED)



from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def login(request):
    rol_no = request.data.get('rol_no')
    password = request.data.get('password')
    
    if rol_no and password:
        user = authenticate(request, rol_no=rol_no, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
    
    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_email(request, email):
    user = get_object_or_404(User, email=email)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_rol_no(request, rol_no):
    user = get_object_or_404(User, id=rol_no)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users_by_first_name(request, first_name):
    users = User.objects.filter(first_name=first_name)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users_by_last_name(request, last_name):
    users = User.objects.filter(last_name=last_name)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_count(request):
    count = User.objects.count()
    return Response({"count": count})





import pandas as pd
from django.http import HttpResponse
from django.db.models import Count
from .models import User


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import io
import pandas as pd
from django.http import HttpResponse

@api_view(['GET'])
@permission_classes([IsAdminUser])
def download_users_pdf(request):
    users = User.objects.all()
    
    # Create a buffer to store PDF data
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Define table data
    data = [['ID', 'First Name', 'Last Name', 'Email', 'Rol No', 'Date Joined']]
    for user in users:
        data.append([user.id, user.first_name, user.last_name, user.email, user.rol_no, user.date_joined.strftime('%Y-%m-%d')])
    
    # Create a table
    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)
    
    # Add table to PDF
    elements = [table]
    pdf.build(elements)
    
    # Reset buffer for reading
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

@api_view(['GET'])
@permission_classes([IsAdminUser])
def download_users_excel(request):
    users = User.objects.all()
    
    # Create a DataFrame from user data
    data = {'ID': [], 'First Name': [], 'Last Name': [], 'Email': [], 'Rol No': [], 'Date Joined': []}
    for user in users:
        data['ID'].append(user.id)
        data['First Name'].append(user.first_name)
        data['Last Name'].append(user.last_name)
        data['Email'].append(user.email)
        data['Rol No'].append(user.rol_no)
        data['Date Joined'].append(user.date_joined.strftime('%Y-%m-%d'))
    
    df = pd.DataFrame(data)
    
    # Convert DataFrame to Excel
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Users', index=False)
    writer.save()
    excel_data = output.getvalue()
    
    # Reset buffer for reading
    output.seek(0)
    response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=users.xlsx'
    return response




from django.utils import timezone
from datetime import datetime, timedelta

@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_increase_statistics(request):
    # Define time intervals
    intervals = {
        'day': 1,
        'week': 7,
        'month': 30,
        'three_months': 90,
        'six_months': 180,
        'year': 365,
        'three_years': 3 * 365,
        'five_years': 5 * 365,
        'ten_years': 10 * 365,
    }

    # Get the current date
    today = datetime.now().date()

    # Initialize statistics dictionary
    statistics = {}

    # Calculate increase in users for each interval
    for interval, days in intervals.items():
        start_date = today - timedelta(days=days)
        user_count = User.objects.filter(date_joined__gte=start_date).count()
        statistics[interval] = user_count

    return Response(statistics)




from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def logout(request):
    refresh_token = request.data.get('refresh_token')
    if refresh_token:
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Token not provided"}, status=status.HTTP_400_BAD_REQUEST)


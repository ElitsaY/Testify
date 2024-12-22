from django.urls import path
from .views import RegisterStudentView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)

urlpatterns = [
    path('register/', RegisterStudentView.as_view(), name='register_student'),
     # JWT Login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # JWT Refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)

from .views import RegisterStudentView
from .views import RegisterTeacherView

urlpatterns = [
    path('register/', RegisterStudentView.as_view(), name='register_student'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # JWT Refresh
    path('create_teacher/', RegisterTeacherView.as_view(), name='create_teacher'),
]
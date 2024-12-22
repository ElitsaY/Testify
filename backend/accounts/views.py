from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateTeacherSerializer
from .serializers import RegisterStudentSerializer

class RegisterStudentView(APIView):
    def post(self, request):
        serializer = RegisterStudentSerializer(data = request.data)
        if serializer.is_valid():
            #save to the database
            serializer.save()
            return Response(
                {"message": "Student registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class RegisterTeacherView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # 1) Проверяваме дали request.user е admin
        if request.user.role != 'admin':
            return Response({"detail": "Only admin can create teachers."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CreateTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher created successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
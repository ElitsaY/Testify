from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
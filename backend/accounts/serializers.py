from rest_framework import serializers
from django.contrib.auth import get_user_model

#serialize registered user
User = get_user_model()

class RegisterStudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        #the serializer works with out Student model
        model = User
        #determine which fields to include in the input/output data
        fields = ['username', 'email', 'password', 'faculty_number']

    #create new student in the database
    def create(self, validated_data):
        #Django automatically hashes the password when create_user is called and imports it to the database
        # Create student
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        # Enable role='student'
        user.role = 'student'
        # If faculty number is entered
        if 'faculty_number' in validated_data:
            user.faculty_number = validated_data['faculty_number']
        user.save()
        return user
    
class CreateTeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create teacher
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.role = 'teacher'
        user.save()
        return user

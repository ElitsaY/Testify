from rest_framework import serializers
from django.contrib.auth import get_user_model

#serialize registered student
Student = get_user_model()

class RegisterStudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        #the serializer works with out Student model
        model = Student
        #determine which fields to include in the input/output data
        fields = ['username', 'email', 'password', 'faculty_number']

    #create new student in the database
    def create(self, validated_data):
        #Django automatically hashes the password when create_user is called and imports it to the database
        student = Student.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password'],
            faculty_number = validated_data['faculty_number']
        )
        return student
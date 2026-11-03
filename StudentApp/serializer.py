from rest_framework.serializers import ModelSerializer
from StudentApp.models import StudentDb,EnrollmentDb


class Student_Serializer(ModelSerializer):
    class Meta:
        model = StudentDb
        fields = "__all__"
        read_only_fields = ["id"]

class Enrollment_Serializer(ModelSerializer):
    class Meta:
        model = EnrollmentDb
        fields = "__all__"
        read_only_fields = ["id"]
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from StudentApp.models import StudentDb,EnrollmentDb
from StudentApp.serializer import Student_Serializer,Enrollment_Serializer

# Create your views here.

class StudentListCreateView(APIView):
    def get(self,request):
        qs = StudentDb.objects.all()
        serializer_instance = Student_Serializer(qs,many =True)
        return Response(data = serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = Student_Serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)


class StudentRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        student_object = get_object_or_404(StudentDb, id=pk)
        serializer_instance = Student_Serializer(student_object)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        student_object = get_object_or_404(StudentDb, id=pk)
        form_data = request.data

        serializer_instance = Student_Serializer(
            instance=student_object,
            data=form_data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors, status=400)

    def delete(self, request, pk):
        student_obj = get_object_or_404(StudentDb, id=pk)
        student_obj.delete()

        return Response(data={
            "message": "Data deleted successfully!"
        })

class EnrollmentListCreateView(APIView):
    def get(self,request):
        qs= EnrollmentDb.objects.all()
        serializer_instance = Enrollment_Serializer(qs,many=True)
        return Response(data = serializer_instance.data)

    
class EnrollmentListCreateView(APIView):

    def get(self, request):
        qs = EnrollmentDb.objects.all()
        serializer_instance = Enrollment_Serializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = Enrollment_Serializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response(
                data={
                    "Message": "Data Added..!",
                    "data": serializer_instance.data
                }
            )

        return Response(
            data=serializer_instance.errors,
           
        )

class EnrollmentRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        student_object = get_object_or_404(EnrollmentDb,id=pk)
        serializer_instance = Enrollment_Serializer(student_object)
        return Response(data = serializer_instance.data)

    def put(self, request, pk):
        enrollment_object = get_object_or_404(EnrollmentDb, id=pk)

        serializer_instance = Enrollment_Serializer(
            instance=enrollment_object,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        enrollment_object = get_object_or_404(EnrollmentDb,id=pk)
        enrollment_object.delete()

        return Response(data ={
            "Message" : "Enrollment Deleted Succesfully..!"
        })
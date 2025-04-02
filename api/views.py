from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Student

class StudentsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request , format = None):
        if request.method == 'GET':
            queryset = Student.objects.all()
            serialized_data = StudentSerializer(queryset, many=True)
            return Response(serialized_data.data)
    def post(self, request, format = None):
        de_serializer = StudentSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response( de_serializer.data )
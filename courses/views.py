
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from courses.models import CourseDb
from courses.serializers import CourseSerializer


class CourseCreateView(APIView):

    def get(self, request):
        qs = CourseDb.objects.all()
        serializer_instance = CourseSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        serializer_instance = CourseSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data
                
            )

        return Response(
            data=serializer_instance.errors
            
        )


class CourseRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(CourseDb, id=pk)
        serializer_instance = CourseSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        qs = get_object_or_404(CourseDb, id=pk)

        serializer_instance = CourseSerializer(
            qs, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(
            data=serializer_instance.errors
        )

    def delete(self, request, pk):
        qs = get_object_or_404(CourseDb, id=pk)
        qs.delete()

        return Response(
            {"message": "Course deleted successfully"}
        )


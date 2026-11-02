
from rest_framework import serializers
from courses.models import CourseDb

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDb
        fields = "__all__"

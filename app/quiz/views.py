"""
Views for quiz APIs
"""

from rest_framework import viewsets, status
from core.models import Quiz
from quiz import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class QuizViewSet(viewsets.ModelViewSet):
    """View for manage quiz APIs"""

    serializer_class = serializers.QuizSerializer
    permission_classes = [AllowAny]
    queryset = Quiz.objects.all().order_by("-id")

    def list(self, request, *args, **kwargs):
        """List all quizzes with message"""
        queryset = self.filter_queryset(self.get_queryset())
        serializers = self.get_serializer(queryset, many=True)
        return Response(
            {"message": "Quizzes retrieved successfully.", "data": serializers.data},
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single quiz with message"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"message": "Quiz retrieved successfully.", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        """Create a quiz with message"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Quiz created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        """Update a quiz with message"""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Quiz updated successfully.", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        """Delete a quiz with message"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Quiz deleted successfully."}, status=status.HTTP_200_OK
        )

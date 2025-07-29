"""
Serializers for quiz APIs
"""

from rest_framework import serializers
from core.models import Quiz, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer for quiz choices."""

    is_correct = serializers.BooleanField(default=False)

    class Meta:
        model = Choice
        fields = ["text", "is_correct"]


class QuizSerializer(serializers.ModelSerializer):
    """Serializer for quizzes."""

    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "question",
            "choices",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        choices_data = validated_data.pop("choices")
        quiz = Quiz.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(quiz=quiz, **choice_data)
        return quiz

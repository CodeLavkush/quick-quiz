"""
Tests for models.
"""

from django.test import TestCase
from core.models import Quiz, Choice


class ModelTests(TestCase):
    """Test models."""

    def setUp(self):
        self.quiz = Quiz.objects.create(question="what is the capital of india?")

        self.choice1 = Choice.objects.create(
            quiz=self.quiz,
            text="delhi",
            is_correct=True,
        )

        self.choice2 = Choice.objects.create(
            quiz=self.quiz,
            text="mumbai",
            is_correct=False,
        )

    def test_create_quiz(self):
        self.assertEqual(str(self.quiz), "what is the capital of india?")
        self.assertEqual(self.quiz.question, "what is the capital of india?")

    def test_create_choices(self):
        self.assertEqual(str(self.choice1), "delhi")
        self.assertEqual(str(self.choice2), "mumbai")
        self.assertTrue(self.choice1.is_correct)
        self.assertFalse(self.choice2.is_correct)

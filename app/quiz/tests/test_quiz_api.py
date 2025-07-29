"""
Tests for Quiz APIs
"""

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Quiz, Choice
from quiz.serializers import QuizSerializer


QUIZ_URL = reverse("quiz:quiz-list")


def create_quiz(**params):
    defaults = {"question": "what is the capital of india"}
    defaults.update(params)

    quiz = Quiz.objects.create(**defaults)
    return quiz


def create_choice(quiz, text="Default choice", is_correct=False):
    choice = Choice.objects.create(quiz=quiz, text=text, is_correct=is_correct)
    return choice


class PublicQuizApiTests(TestCase):
    """Test the publicly available quiz API"""

    def setUp(self):
        self.client = APIClient()

    def test_list_quizzes(self):
        """Test retrieving a list of quizzes"""
        create_quiz(question="Question 1?")
        create_quiz(question="Question 2?")

        res = self.client.get(QUIZ_URL)

        quizzes = Quiz.objects.all().order_by("-id")
        serializer = QuizSerializer(quizzes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["data"], serializer.data)

    def test_create_quiz(self):
        """Test creating quiz"""
        payload = {
            "question": "what is the capital of india?",
            "choices": [
                {
                    "text": "delhi",
                    "is_correct": True,
                },
                {
                    "text": "mumbai",
                    "is_correct": False,
                },
            ],
        }

        res = self.client.post(QUIZ_URL, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["data"]["question"], payload["question"])

        quiz = Quiz.objects.get(id=res.data["data"]["id"])
        choices = quiz.choices.all()
        self.assertEqual(choices.count(), 2)

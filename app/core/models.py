"""
Database models.
"""

from django.db import models


class Quiz(models.Model):
    """Quiz objects."""

    question = models.TextField()

    def __str__(self):
        return self.question


class Choice(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

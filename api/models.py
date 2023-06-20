from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models

# validate the due date


def validate_due_date(value):
    if value and value <= timezone.now():
        raise ValidationError("Due date must be in the future.")


# Task model

class Task(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "OPEN"),
        ("WORKING", "WORKING"),
        ("DONE", "DONE"),
        ("OVERDUE", "OVERDUE"),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(
        blank=True, null=True, validators=[validate_due_date])
    tags = models.ManyToManyField("Tag", blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="OPEN")

    def __str__(self):
        return self.title


# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Question(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Example(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    input = RichTextField()
    output = RichTextField()
    explanation = RichTextField()

    def __str__(self):
        return self.question.title


class Constraint(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question.title


class Testcase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    test = RichTextField()

    def __str__(self):
        return self.title

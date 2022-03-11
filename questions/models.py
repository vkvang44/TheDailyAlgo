from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Question(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField()
    method = models.TextField()
    link = models.TextField()
    example = RichTextField()
    constraint = RichTextField()
    testcase = RichTextField()
    test_file = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Date(models.Model):
    date_id = models.IntegerField()
    last_num = models.IntegerField()
    datetime = models.DateField()



from django.contrib import admin
from .models import Question, Example, Constraint, Testcase, Date

# Register your models here.
admin.site.register(Question)
admin.site.register(Example)
admin.site.register(Constraint)
admin.site.register(Testcase)
admin.site.register(Date)


from django.shortcuts import render
from .models import Question


# Create your views here.
def question(request):
    ques = Question.objects.get(number=1)
    examples = ques.example_set.all()
    constraints = ques.constraint_set.all()
    testcases = ques.testcase_set.all()

    context = {
        'question': ques,
        'examples': examples,
        'constraints': constraints,
        'testcases': testcases
    }

    return render(request, 'questions/questions.html', context)

from django.shortcuts import render
from .models import Question, Date
from datetime import date
from .utils import create_file, execute_file, change_date


# Create your views here.
def question(request):
    saved_date = Date.objects.get(date_id=1)
    num = saved_date.last_num
    curr_date = date.today()

    if curr_date != saved_date.datetime:
        num = change_date(saved_date, curr_date)

    ques = Question.objects.get(number=num)
    examples = ques.example_set.all()
    constraints = ques.constraint_set.all()
    testcases = ques.testcase_set.all()
    test_file = str(testcases[0])
    user_code = ques.method
    errors = ''
    std_output = [['Click \'Run Code\' to see if your code passes the testcases!']]
    test_output = []

    if request.method == 'POST':
        req_post = request.POST
        user_code = req_post['my-python-editor']

        create_file(user_code)
        std_output, test_output, errors, = execute_file(test_file)

    context = {
        'question': ques,
        'examples': examples,
        'constraints': constraints,
        'testcases': testcases,
        "user_code": user_code,
        'std_output': std_output,
        'test_output': test_output,
        'errors': errors
    }

    return render(request, 'questions/questions.html', context)



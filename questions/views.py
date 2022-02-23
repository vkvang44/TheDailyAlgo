from django.shortcuts import render
from .models import Question
from django.core.files import File
import os
import subprocess

module_dir = os.path.dirname(__file__)
test_path = os.path.join(module_dir, 'scripts\\')
file_path = os.path.join(module_dir, 'scripts\\program.py')


# Create your views here.
def question(request):
    ques = Question.objects.get(number=1)
    examples = ques.example_set.all()
    constraints = ques.constraint_set.all()
    testcases = ques.testcase_set.all()

    code = request.POST
    c = '# Write your code here'
    outputs = 'Click submit button to see if your code passes!'
    errors = ''



    if request.method == 'POST':
        code = request.POST
        c = code['my-python-editor']

        with open(file_path, 'w') as f:
            myfile = File(f)
            myfile.write(c)
        myfile.closed
        f.closed

        proc = subprocess.Popen(['python', 'test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=test_path)
        try:
            outs, errs = proc.communicate(timeout=10)
            outputs = outs
            errors = errs
            e_arr = errors.split(b'\r\n')
            arr = outputs.split(b'\r\n')

        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            print("output limit exceeded. Check for memory leaks or inifite loops")



    context = {
        'question': ques,
        'examples': examples,
        'constraints': constraints,
        'testcases': testcases,
        "code": code,
        "c": c,
        'outputs': arr,
        'errors': e_arr
    }

    return render(request, 'questions/questions.html', context)

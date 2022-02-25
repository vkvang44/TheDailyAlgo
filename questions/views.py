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
    print(examples)
    code = request.POST
    user_code = '# Write your code here'
    outputs = 'Click submit button to see if your code passes!'
    errors = ''
    std_output = []
    test_output = []
    temp = []



    if request.method == 'POST':
        code = request.POST
        user_code = code['my-python-editor']

        with open(file_path, 'w') as f:
            myfile = File(f)
            myfile.write(user_code)
        myfile.closed
        f.closed

        proc = subprocess.Popen(['python', 'test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=test_path)
        try:
            outs, errs = proc.communicate(timeout=10)
            outputs = outs.decode()
            errors = errs.decode()
            arr = outputs.split('\r\n')

            # get stdout
            s = False
            for word in arr:
                if word == "STDOUT:":
                    s = True
                    continue
                elif word == "RESULT:":
                    s = False
                    break
                if s == True:
                    std_output.append(word)

            # get test output
            t = False
            for word in arr:
                if word == "RESULT:":
                    t = True
                    continue
                elif word == "STDOUT:":
                    t = False
                    if temp:
                        test_output.append(temp)
                        temp = []
                if t == True:
                    temp.append(word)
            test_output.append(temp)

        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            errors = "output limit exceeded. Check for memory leaks or inifite loops"

    context = {
        'question': ques,
        'examples': examples,
        'constraints': constraints,
        'testcases': testcases,
        "code": code,
        "user_code": user_code,
        'outputs': outputs,
        'std_output': std_output,
        'test_output': test_output,
        'errors': errors
    }

    return render(request, 'questions/questions.html', context)



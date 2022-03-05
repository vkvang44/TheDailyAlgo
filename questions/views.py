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
    ques = Question.objects.get(number=2)
    examples = ques.example_set.all()
    constraints = ques.constraint_set.all()
    testcases = ques.testcase_set.all()
    test_file = str(testcases[0]) + '.py'
    user_code = ques.method
    errors = ''
    std_output = [['Click \'Run Code\' to see if your code passes the testcases!']]
    test_output = []

    if request.method == 'POST':
        code = request.POST
        user_code = code['my-python-editor']

        with open(file_path, 'w') as f:
            myfile = File(f)
            myfile.write(user_code)
        myfile.closed
        f.closed

        proc = subprocess.Popen(['python', test_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=test_path)
        try:
            outs, errs = proc.communicate(timeout=5)
            outputs = outs.decode()
            errors = errs.decode()
            outputs_arr = outputs.split('\r\n')

            # get stdout
            s = False
            std_output = []
            temp = []
            for word in outputs_arr:
                if word == "STDOUT:":
                    s = True
                    continue
                elif word == "RESULT:":
                    s = False
                    std_output.append(temp)
                    temp = []
                if s == True:
                    temp.append(word)

            # get test output
            t = False
            temp = []
            for word in outputs_arr:
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
            std_output = []
            proc.kill()
            outs, errs = proc.communicate()
            errors = "Output limit exceeded. Check for memory leaks or infinite loops"

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



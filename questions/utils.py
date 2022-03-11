from django.core.files import File
import os
import subprocess
from random import randint

module_dir = os.path.dirname(__file__)
test_path = os.path.join(module_dir, 'testfiles\\')
file_path = os.path.join(module_dir, 'testfiles\\program.py')


def change_date(saved_date, curr_date):
    num = randint(1,5)
    saved_date.datetime = curr_date
    saved_date.last_num = num
    saved_date.save()
    return num


def create_file(user_code):
    with open(file_path, 'w') as f:
        myfile = File(f)
        myfile.write(user_code)
    myfile.closed
    f.closed


def get_std_output(outputs_arr):
    # get stdout
    s = False
    temp = []
    std_output = []
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
    return std_output


def get_test_output(outputs_arr):
    # get test output
    t = False
    temp = []
    test_output = []
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
    return test_output


def execute_file(test_file):
    proc = subprocess.Popen(['python', test_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=test_path)
    try:
        outs, errs = proc.communicate(timeout=5)
        outputs = outs.decode()
        errors = errs.decode()
        outputs_arr = outputs.split('\r\n')

        std_output = get_std_output(outputs_arr)
        test_output = get_test_output(outputs_arr)

    except subprocess.TimeoutExpired:
        std_output = []
        test_output = []
        proc.kill()
        outs, errs = proc.communicate()
        errors = "Output limit exceeded. Check for memory leaks or infinite loops"

    return std_output, test_output, errors

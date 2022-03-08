import program

dict_cases = {
    1: {
        "ques": "Case 1",
        "s": "()",
        "ans": True
    },
    2: {
        "ques": "Case 2",
        "s": "([)]",
        "ans": False
    },
    3: {
        "ques": "Case 3",
        "s": "(]",
        "ans": False
    },
    4: {
        "ques": "Case 4",
        "s": "(([([])]))",
        "ans": True
    },
    5: {
        "ques": "Case 5",
        "s": "((([[)])])",
        "ans": False
    }
}

def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.isValid(case["s"])

    print('RESULT:')
    print(case["ques"])
    if type(output) == type(case['ans']) and output == case['ans']:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["s"])
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    test_program(dict_cases[case])

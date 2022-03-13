import program

dict_cases = {
    1: {
        "ques": "Case 1",
        "nums": [1,2,3,1],
        "ans": True,
    },
    2: {
        "ques": "Case 2",
        "nums": [1,2,3,4],
        "ans": False
    },
    3: {
        "ques": "Case 3",
        "nums": [1,1,1,3,3,4,3,2,4,2],
        "ans": True,
    },
    4: {
        "ques": "Case 4",
        "nums": [3, -11, 91, -1, 6, -25, 23, 3453, 3453, 122, 4, 2, 112, 1, 4],
        "ans": True,
    },
    5: {
        "ques": "Case 5",
        "nums": [11, 24, 65, 88, 64, 78, 678, 119, 23, 21, 54, 123, 765],
        "ans": False,
    }
}


def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    print(case["nums"])
    output = program.containsDuplicate(case["nums"])

    print('RESULT:')
    print(case["ques"])
    if type(output) == type(case['ans']) and output == case['ans']:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["nums"])
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    test_program(dict_cases[case])
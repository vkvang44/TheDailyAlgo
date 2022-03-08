import program

dict_cases = {
    1: {
        "ques": "Case 1",
        "prices": [7,1,5,3,6,4],
        "ans": 5,
    },
    2: {
        "ques": "Case 2",
        "prices": [2, 3, 6, 4, 2, 1, 12],
        "ans": 11,
    },
    3: {
        "ques": "Case 3",
        "prices": [7,6,4,3,1],
        "ans": 0,
    },
    4: {
        "ques": "Case 4",
        "prices": [7],
        "ans": 0,
    },
    5: {
        "ques": "Case 5",
        "prices": [920, 914, 866, 890, 1000, 999, 724, 627],
        "ans": 134,
    }
}

def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.maxProfit(case["prices"])

    print('RESULT:')
    print(case["ques"])
    if case["ans"] == output:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["prices"])
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    test_program(dict_cases[case])

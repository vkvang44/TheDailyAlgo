import program

dict_cases = {
    1: {
        "ques": "Case 1",
        "array": [3, 5, -4, 8, 11, 1, -1, 6],
        "targetSum": 10,
        "ans_1": 11,
        "ans_2": -1
    },
    2: {
        "ques": "Case 2",
        "array": [3, 5, -4],
        "targetSum": 1,
        "ans_1": 5,
        "ans_2": -4
    },
    3: {
        "ques": "Case 3",
        "array": [3, 11, 1, -1, 6],
        "targetSum": 14,
        "ans_1": 11,
        "ans_2": 3
    },
}



def test_program(case):
    print(case["ques"])
    output = program.twoNumberSum(case["array"], case["targetSum"])
    if case["ans_1"] in output and case["ans_2"] in output:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Your Answer: ", output)
        print("Correct Answer: ", [case["ans_1"], case["ans_2"]], "\n")


for case in dict_cases:
    test_program(dict_cases[case])

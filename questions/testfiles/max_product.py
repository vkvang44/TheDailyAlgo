import program

dict_cases = {
    1:
        {
        "ques": "Case 1",
        "nums": [2,3,-2,4],
        "ans": 6,
        },

    2:
        {
        "ques": "Case 2",
        "nums": [-2,0,-1],
        "ans": 0,
        },

    3:
        {
        "ques": "Case 3",
        "nums": [-10, 10],
        "ans": 10,
        },

    4:
        {
        "ques": "Case 4",
        "nums": [3, 4,-1, 9, 0, 6, -5, -5],
        "ans": 150,
        },

    5:
        {
        "ques": "Case 5",
        "nums": [1, 0, 10, -10, -1, 2, -6],
        "ans": 200,
        }
}


def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.maxProduct(case["nums"])

    print('RESULT:')
    print(case["ques"])
    if output == case["ans"]:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["nums"], )
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    test_program(dict_cases[case])

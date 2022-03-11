import program

dict_cases = {
    1:
        {
        "ques": "Case 1",
        "nums": [-1,0,1,2,-1,-4],
        "ans": [[-1,-1,2],[-1,0,1]],
        },

    2:
        {
        "ques": "Case 2",
        "nums": [0],
        "ans": [],
        },

    3:
        {
        "ques": "Case 3",
        "nums": [-1,0,3,-22,-19,41,56,77,-1,2],
        "ans": [[-22,-19,41],[-1,-1,2]],
        },

    4:
        {
        "ques": "Case 4",
        "nums": [12,2,4,6,8,68,9,8,0,5654,444,2,23242],
        "ans": [],
        },

    5:
        {
        "ques": "Case 5",
        "nums": [12,2,14,-1,8,68,9,-8,0,5654,-444,2,23242,-4,-4,-10],
        "ans": [[-10,-4,14],[-10,2,8],[-8,-4,12],[-8,-1,9],[-8,0,8],[-4,-4,8],[-4,2,2]],
        }
}


def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.threeSum(case["nums"])

    print('RESULT:')
    print(case["ques"])
    if len(output) == len(case["ans"]):
        output.sort()
        if output == case["ans"]:
            print("PASS!\n")
        else:
            print("FAIL :(")
            print("Input: ", case["nums"],)
            print("Your Answer: ", output)
            print("Correct Answer: ", case["ans"], "\n")
    else:
            print("FAIL :(")
            print("Input: ", case["nums"], )
            print("Your Answer: ", output)
            print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    test_program(dict_cases[case])

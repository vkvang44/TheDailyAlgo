import program

dict_cases = {
    1:
        {
        "ques": "Case 1",
        "nums": [[1,3],[2,6],[8,10],[15,18]],
        "ans": [[1,6],[8,10],[15,18]],
        },

    2:
        {
        "ques": "Case 2",
        "nums": [[1,4],[4,5]],
        "ans": [[1,5]],
        },

    3:
        {
        "ques": "Case 3",
        "nums": [[1,3]],
        "ans": [[1,3]]
        },

    4:
        {
        "ques": "Case 4",
        "nums": [[1,4],[12,33],[20,42],[21,50]],
        "ans": [[1,4],[12,50]],
        },

    5:
        {
        "ques": "Case 5",
        "nums": [[1,10],[12,33],[20,42],[21,50],[51,55],[54,62],[62,83]],
        "ans": [[1,10],[12,50],[51,83]],
        }
}


def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.merge(case["nums"])

    print('RESULT:')
    print(case["ques"])
    if len(output) == len(case["ans"]):
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

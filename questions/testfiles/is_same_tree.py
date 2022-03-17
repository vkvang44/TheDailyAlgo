import program
from data_structures.binary_tree import BinaryTree

dict_cases = {
    1: {
        "ques": "Case 1",
        "p": [1,2,3,None,4],
        "q": [1,2,3,4],
        "ans": False,
    },
    2: {
        "ques": "Case 2",
        "p": [1,2,3,4],
        "q": [1,2,3,4],
        "ans": True,
    },
    3: {
        "ques": "Case 3",
        "p": [1,2,3,4,5,None,6],
        "q": [1,2,3,4,5,6],
        "ans": False,
    },
    4: {
        "ques": "Case 4",
        "p": [1,2,4,-1,2,3],
        "q": [1,2,4,2,-1,3],
        "ans": False,
    },
    5: {
        "ques": "Case 5",
        "p": [1,2,3,4,7,8,12,-1],
        "q": [1,2,3,4,7,8,12,-1],
        "ans": True,
    }
}


def create_binary_tree(case):
    p = BinaryTree().insert_level_order(case["p"], None, 0, len(case["p"]))
    q = BinaryTree().insert_level_order(case["q"], None, 0, len(case["q"]))
    return p, q


def test_program(case, p, q):
    print("STDOUT:")
    print(case["ques"])
    output = program.isSameTree(p, q)

    print('RESULT:')
    print(case["ques"])
    if output == case["ans"]:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["p"], ", ", case["q"])
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    p, q = create_binary_tree(dict_cases[case])
    test_program(dict_cases[case], p, q)
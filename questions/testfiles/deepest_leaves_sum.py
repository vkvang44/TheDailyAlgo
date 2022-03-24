import program
from data_structures.binary_tree import BinaryTree
# 1, 3, 7, 15, 31
dict_cases = {
    1: {
        "ques": "Case 1",
        "root": [1,2,3,4,5,None,6,7, None,None,None,None,None,None,8],
        "ans": 15,
    },
    2: {
        "ques": "Case 2",
        "root": [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5],
        "ans": 19,
    },
    3: {
        "ques": "Case 3",
        "root": [1,2,3,4,5,None,6],
        "ans": 15,
    },
    4: {
        "ques": "Case 4",
        "root": [1,2,3],
        "ans": 5,
    },
    5: {
        "ques": "Case 5",
        "root": [1,2,None],
        "ans": 2,
    }
}


def create_binary_tree(case):
    root = BinaryTree().insert_level_order(case["root"], None, 0, len(case["root"]))
    return root


def test_program(case, root):
    print("STDOUT:")
    print(case["ques"])
    output = program.deepestLeavesSum(root)

    print('RESULT:')
    print(case["ques"])
    if output == case["ans"]:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["root"])
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    root = create_binary_tree(dict_cases[case])
    test_program(dict_cases[case], root)
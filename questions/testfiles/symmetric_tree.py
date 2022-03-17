import program
from data_structures.binary_tree import BinaryTree

dict_cases = {
    1: {
        "ques": "Case 1",
        "root": [1,2,2,3,4,4,3],
        "ans": True,
    },
    2: {
        "ques": "Case 2",
        "root": [1,2,2,None,3,None,3],
        "ans": False,
    },
    3: {
        "ques": "Case 3",
        "root": [1,2,2,3,4,4,3],
        "ans": True,
    },
    4: {
        "ques": "Case 4",
        "root": [1,2,2,3,4,4,3],
        "ans": True,
    },
    5: {
        "ques": "Case 5",
        "root": [1,2,2,3,4,4,3],
        "ans": True,
    }
}


def create_binary_tree(case):
    root = BinaryTree().insert_level_order(case["root"], None, 0, len(case["root"]))
    return root


def test_program(case, root):
    print("STDOUT:")
    print(case["ques"])
    output = program.isSymmetric(root)

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
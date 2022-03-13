import program
from data_structures.linked_lists import SinglyLinkedList

testcases = {
    1:
        {
        "ques": "Case 1",
        "head": [1,2,3,4,5],
        "ans": [5,4,3,2,1],
        },
    2:
        {
        "ques": "Case 2",
        "head": [1,2,3,4,5,6,7,8,9,10],
        "ans": [10,9,8,7,6,5,4,3,2,1],
        },
    3:
        {
        "ques": "Case 3",
        "head": [25,33,44,57,14,90],
        "ans": [90,14,57,44,33,25],
        },
    4:
        {
        "ques": "Case 4",
        "head": [0,1,0,2,0,3],
        "ans": [3,0,2,0,1,0],
        },
    5:
        {
        "ques": "Case 5",
        "head": [100,2450, 9, 1234, 4, 1],
        "ans": [1, 4, 1234, 9, 2450, 100],
        }
}


def create_linked_list(case):
    head = SinglyLinkedList().create_list(case["head"])
    return head


def test_program(case, head):
    print("STDOUT:")
    print(case["ques"])
    output = program.reverseList(head)
    output_arr = SinglyLinkedList().linked_list_to_arr(output)

    print('RESULT:')
    print(case["ques"])
    if output_arr == case["ans"]:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["head"] )
        print("Your Answer: ", output_arr)
        print("Correct Answer: ", case["ans"], "\n")


for test in testcases:
    head = create_linked_list(testcases[test])
    test_program(testcases[test], head)
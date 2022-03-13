import program
from data_structures.linked_lists import SinglyLinkedList

dict_cases = {
    1: {
        "ques": "Case 1",
        "list1": [1,2,3,4],
        "list2": [1,2,3,4],
        "ans": [1,1,2,2,3,3,4,4],
    },
    2: {
        "ques": "Case 2",
        "list1": [1,2,4],
        "list2": [1,3,4],
        "ans": [1,1,2,3,4,4],
    },
    3: {
        "ques": "Case 3",
        "list1": [1,2,3,4],
        "list2": [1,2,3,4],
        "ans": [1,1,2,3,4,4],
    },
    4: {
        "ques": "Case 4",
        "list1": [-22, -10, 0, 1, 15, 34],
        "list2": [-25,-15, 1, 3, 4, 30],
        "ans": [-25, -22, -15, -10, 0, 1, 1, 3, 4, 15, 30, 34],
    },
    5: {
        "ques": "Case 5",
        "list1": [-5, -4, -3, 0],
        "list2": [-6, -3, -2, 1],
        "ans": [-6, -5, -4, -3, -3, -2, 0, 1],
    }
}


def create_linked_list(case):
    list1 = SinglyLinkedList().create_list(case["list1"])
    list2 = SinglyLinkedList().create_list(case["list2"])
    return list1, list2


def test_program(case, list1, list2):
    print("STDOUT:")
    print(case["ques"])
    output = program.mergeTwoLists(list1, list2)
    output_arr = SinglyLinkedList().linked_list_to_arr(output)

    print('RESULT:')
    print(case["ques"])
    if output_arr == case["ans"]:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["list1"], ", ", case["list2"])
        print("Your Answer: ", output_arr)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    list1, list2 = create_linked_list(dict_cases[case])
    test_program(dict_cases[case], list1, list2)
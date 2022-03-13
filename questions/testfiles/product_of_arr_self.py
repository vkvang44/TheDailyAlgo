import program

testcases = {
    1: {
        "ques": "Case 1",
        "nums": [1,2,3,4],
        "ans": [24,12,8,6],
    },
    2: {
        "ques": "Case 2",
        "nums": [-1,1,0,-3,3],
        "ans": [0,0,9,0,0],
    },
    3: {
        "ques": "Case 3",
        "nums": [12, 13, 5, 6, 30 , 9],
        "ans": [105300, 97200, 252720, 210600, 42120, 140400],
    },
    4: {
        "ques": "Case 4",
        "nums": [-11, 4, 5, 23, -10 ,2, 24,-4],
        "ans": [883200, -2428800, -1943040, -422400, 971520, -4857600, -404800, 2428800],
    },
    5: {
        "ques": "Case 5",
        "nums": [0, 22, -30,30,14],
        "ans": [-277200, 0, 0, 0, 0],
    }
}


def failed(case, output):
    print("FAIL :(")
    print("Input: ", case["nums"])
    print("Your Answer: ", output)
    print("Correct Answer: ", case["ans"], "\n")


def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.productExceptSelf(case["nums"])

    print('RESULT:')
    print(case["ques"])
    if len(output) == len(case["nums"]):
        for num in output:
            if num not in case["ans"]:
                failed(case, output)
                return
        print("PASS!\n")
    else:
        failed(case, output)


for test in testcases:
    test_program(testcases[test])




## potential idea for generating new testcases everytime
# def ans(nums):
#     left, right = 1, 1
#     answer = []
#
#     for idx in range(0, len(nums)):
#         answer.append(left)
#         left *= nums[idx]
#
#     for idx in range(len(nums) - 1, -1, -1):
#         answer[idx] *= right
#         right *= nums[idx]
#
#     return answer
# for i in range(6, 20):
#     rand_num = random.randint(2,105)
#     nums = []
#     while rand_num > 0:
#         j = random.randint(-30, 30)
#         nums.append(j)
#         rand_num -= 1
#     answer = ans(nums)
#     dict_cases[i] = {
#         "ques": i,
#         "nums": nums,
#         "ans": answer,
#     }
#
# print(dict_cases)
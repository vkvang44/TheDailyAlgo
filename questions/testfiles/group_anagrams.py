import program

testcases = {
    1:
        {
        "ques": "Case 1",
        "strs": ["eat","tea","tan","ate","nat","bat"],
        "ans": [["bat"],["nat","tan"],["ate","eat","tea"]],
        "bat": "bat",
        "nat": "nat",
        "tan": "tan",
        "ate": "ate",
        "eat": "eat",
        "tea": "tea",
        },

    2:
        {
        "ques": "Case 2",
        "strs": ["a"],
        "ans": ["a"],
        "a":"a"
        },

    3:
        {
        "ques": "Case 3",
        "strs": ["car", "arc","elbow","below","cide","chin"],
        "ans": [["car","arc"],["elbow","below"],["cide"],["chin"]],
        "car":"car",
        "arc":"arc",
        "elbow":"elbow",
        "below":"below",
        "cide":"cide",
        "chin":"chin"
        },

    4:
        {
        "ques": "Case 4",
        "strs": ["abc", "cba", "bc", "c"],
        "ans": [["abc", "cba"],["bc"],["c"]],
        "abc":"abc",
        "cba":"cba",
        "bc":"bc",
        "c":"c"
        },
    5:
        {
        "ques": "Case 5",
        "strs": [""],
        "ans": [""],
        }
}


def failed(case, output):
    print("FAIL :(")
    print("Input: ", case["strs"], )
    print("Your Answer: ", output)
    print("Correct Answer: ", case["ans"], "\n")


def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.groupAnagrams(case["strs"])

    print('RESULT:')
    print(case["ques"])
    actual = case["ans"]
    if len(output) == len(actual):
        for arr in output:
            for word in arr:
                if len(output) == 1:
                    if word == actual[0]:
                        break
                if not case.get(word):
                    failed(case, output)
                    return None
        print("PASS!\n")
    else:
        failed(case, output)


for test in testcases:
    test_program(testcases[test])

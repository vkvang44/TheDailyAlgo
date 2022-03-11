import program

dict_cases = {
    1: {
        "ques": "Case 1",
        "s": "anagram",
        "t": "nagaram",
        "ans": True
    },
    2: {
        "ques": "Case 2",
        "s": "car",
        "t": "rat",
        "ans": False
    },
    3: {
        "ques": "Case 3",
        "s": "secure",
        "t": "rescue",
        "ans": True
    },
    4: {
        "ques": "Case 4",
        "s": "dessert",
        "t": "stressed",
        "ans": False
    },
    5: {
        "ques": "Case 5",
        "s": "videogame",
        "t": "giveademo",
        "ans": True
    }
}

def test_program(case):
    print("STDOUT:")
    print(case["ques"])
    output = program.isAnagram(case["s"], case["t"])

    print('RESULT:')
    print(case["ques"])
    if type(output) == type(case['ans']) and output == case['ans']:
        print("PASS!\n")
    else:
        print("FAIL :(")
        print("Input: ", case["s"], ",", case["t"])
        print("Your Answer: ", output)
        print("Correct Answer: ", case["ans"], "\n")


for case in dict_cases:
    test_program(dict_cases[case])

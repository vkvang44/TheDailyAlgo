def containsDuplicate(nums):
    #write your code here
    num_set = set()
    for num in nums:
        print(num)
        if num in num_set:
            return False
        num_set.add(num)
    return False
def twoNumberSum(arr, target):
    # write your code here
    seen = {}
    for num in arr:
        asda
        diff = target - num
        if diff in seen:
            print([seen[diff], num])
            return [seen[diff], num]
        else:
            seen[num] = num
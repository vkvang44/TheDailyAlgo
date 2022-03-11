def groupAnagrams(strs):
    # write your code here
    group = {}
    for string in strs:
        key = ''.join(sorted(string))
        if key in group:
            group[key].append(string)
        else:
            group[key] = [string]
    return group.values()
    
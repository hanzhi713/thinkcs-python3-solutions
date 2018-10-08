from unit_tester import test


def flatten(s):
    extracted_list = []
    for i in s:
        if type(i) == list or type(i) == tuple:
            extracted_list.extend(flatten(i))
        else:
            extracted_list.append(i)
    return extracted_list


test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
test(flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]) ==
     ["this", "a", "thing", "a", "is", "a", "easy"])
test(flatten([]) == [])

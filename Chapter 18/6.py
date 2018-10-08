from unit_tester import test


def extract(s):
    extracted_list = []
    for i in s:
        if type(i) == list or type(i) == tuple:
            extracted_list.extend(extract(i))
        else:
            extracted_list.append(i)
    return extracted_list


def count(target, nxs):
    return extract(nxs).count(target)


test(count(2, []) == 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a",
           [["this", ["a", ["thing", "a"], "a"], "is"], ["a", "easy"]]) == 4)

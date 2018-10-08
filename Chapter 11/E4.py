import copy

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
# this and that have the same value but do not refer to the same object.
print("Test 1: {0}".format(this is that))
that = this
# if we assign one variable to another, both variables refer to the same object
# therefore this is that
print("Test 2: {0}".format(this is that))

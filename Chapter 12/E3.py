import copy

# the following example comes from http://greybeard.iteye.com/blog/1442259
arm = [1, 2, 3, 4, ['a', 'b']]

b = arm
c = copy.copy(arm)  # shallow copy
d = copy.deepcopy(arm)  # deep copy

arm.append(5)
arm[4].append('c')

print('a = ', arm)
print('b = ', b)
print('c = ', c)
print('d = ', d)

# the result should be:
'''a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c = [1, 2, 3, 4, ['a', 'b', 'c']]
d = [1, 2, 3, 4, ['a', 'b']]'''

# In exercise 4, though I am not sure.
# Using "that = copy.deepcopy(this)" rather than "that = this" will return a false in "this is that".

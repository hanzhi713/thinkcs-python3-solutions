import sys, time


def recursion_depth(a):
    recursion_depth(int(a))


print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
time.sleep(2)
recursion_depth(1)

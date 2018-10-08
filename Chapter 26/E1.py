class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


class ListQueue:
    def __init__(self):
        self.items = []
        self.head = None
        self.last = None

    def insert(self, cargo):
        self.items = [cargo] + self.items

    def remove(self):
        self.items.pop()


import random
import time
import matplotlib.pyplot as plt


def performance_test(start, end, step, num_times):
    time_linked_priqueue = []
    time_list_priqueue = []
    for i in range(start, end + step, step):
        sample = list(range(i))
        random.shuffle(sample)
        listp = []
        linkedp = []
        for x in range(num_times):
            list_priqueue = ListQueue()
            linked_priqueue = ImprovedQueue()

            t0 = time.clock()
            for item in sample:
                list_priqueue.insert(item)
            for iii in range(len(sample)):
                list_priqueue.remove()
            listp.append(time.clock() - t0)

            t0 = time.clock()
            for item in sample:
                linked_priqueue.insert(item)
            for iii in range(len(sample)):
                linked_priqueue.remove()
            linkedp.append(time.clock() - t0)

        t1 = round(sum(listp) / num_times, 5)
        time_list_priqueue.append(t1)
        print("Time taken by 'Python List Queue' in average is {0} when the length is {1}".format(t1, i))
        t1 = round(sum(linkedp) / num_times, 5)
        time_linked_priqueue.append(t1)
        print("Time taken by 'Improved Queue' in average is {0} when the length is {1}".format(t1, i))

    plt.figure()
    plt.hold(True)
    plt.plot(list(range(start, end + step, step)), time_list_priqueue, "b")
    plt.plot(list(range(start, end + step, step)), time_linked_priqueue, "r")
    plt.show()


performance_test(1000, 10000, 500, 5)

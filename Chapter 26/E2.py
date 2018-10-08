class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class LinkedListPriQueue:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.is_empty():
            self.head = self.last = node
            self.length += 1
        else:
            item = self.head
            if node.cargo >= self.head.cargo:
                self.head = node
                self.head.next = item
                return
            while item.next is not None:
                if node.cargo >= item.next.cargo:
                    node.next = item.next
                    item.next = node
                    self.length += 1
                    return
                item = item.next
            last = self.last
            last.next = node
            self.last = node
            self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


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
            list_priqueue = PriorityQueue()
            linked_priqueue = LinkedListPriQueue()

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
        print("Time taken by 'Python List Priority Queue' in average is {0} when the length is {1}".format(t1, i))
        t1 = round(sum(linkedp) / num_times, 5)
        time_linked_priqueue.append(t1)
        print("Time taken by 'Linked List Priority Queue' in average is {0} when the length is {1}".format(t1, i))

    plt.figure()
    plt.hold(True)
    plt.plot(list(range(start, end + step, step)), time_list_priqueue, "b")
    plt.plot(list(range(start, end + step, step)), time_linked_priqueue, "r")
    plt.show()


performance_test(1000, 5000, 500, 3)

import re


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


def eval_postfix(expr):
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == "-":
            sub = stack.pop() - stack.pop()
            stack.push(sub)
        elif token == "/":
            quotient = stack.pop() / stack.pop()
            stack.push(quotient)
        else:
            stack.push(int(token))
    return stack.pop()


print(eval_postfix("1 2 + 3 *"))


class Stack:

    list_stack = [6, 5, 4]

    def is_empty(self):
        if self.list_stack:
            return True
        else:
            return False

    def push(self, item):
        self.list_stack.insert(0, item)
        # print(self.list_stack)


    def pop(self):
        item = self.list_stack[0]
        self.list_stack.pop(0)
        # print(self.list_stack)
        return item

    def peek(self):
        item = self.list_stack[0]
        return item

    def size(self):
        return len(self.list_stack)

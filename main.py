class stack():
    def __init__(self):
        self.last_value = 0
        self.value = {}

    def isEmpty(self):
        if not self.value:
            return False
        else:
            return True

    def push(self, value):
        self.last_value += 1
        self.value[self.last_value] = value


    def pop(self):
        del self.value[self.last_value]
        self.last_value -= 1

    def peek(self):
        return self.value[self.last_value]

    def size(self):
        return self.last_value


def check_balance(value):
    myStack = stack()
    for elem in value:
        if myStack.size() > 0:
            if (elem == ')' and myStack.peek() == '(') or (elem == ']' and myStack.peek() == '[') or (elem == '}' and myStack.peek() == '{'):
                myStack.pop()
            else:
                myStack.push(elem)
        else:
            myStack.push(elem)
    if myStack.size() > 0:
        print('Строка не сбалансирована')
    else:
        print('Строка сбалансирована')

if __name__ == '__main__':
    check_balance('[([])((([[[]]])))]{()}')
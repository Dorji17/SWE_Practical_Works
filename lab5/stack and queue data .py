1#evalutate postfix expression

def evaluate_postfix(expression):
    stack = stack()
    operators =set[{'+', '-', '*', '/'}]

    for token in expression.split():
        if token not in operators:
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '_':
                stack.push(a - b) 
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)

    return stack.pop()

1#implementating a queue with two stacks
class twostacksqueue:
    def __init__(self) -> None:
        self.items_in = items()
        self.items_out = itemse()

    def is_empty(self):
        return len(self.item) == 0    

    def enqueue(self, item):
        self.items_in.push(item)

    def dequeue(self): 
        if self.items_out.is_empty():
            while not self.items_in.is_empty():
                self.items_out.push(self.items_in.pop())
        if self.items_out.is_empty():
            raise IndexError("Quenue is empty")
        return self.items_out.pop()

def size(self):
    return len(self.items)

#Test the twostackqueue

two_items_queue =   twostacksqueue()
two_items_queue.enqueue(1)
two_items_queue.enqueue(2)
two_items_queue.enqueue(3)
print(two_items_queue.dequeue())

3#task scheduler using a queue

class taskscheduler:
    def __init__(self) -> None:
        self.queue = Queue()

    def add_task(self, task):
        self.queue.enqueue(task)

    def process_tasks(self):
        while not self.queue.is_empty():
            task = self.queue.dequeue():
            print(f"Processing task: {task}")


#Test the taskscheduler
scheduler = taskscheduler()
scheduler.add_task("task 1")
scheduler.add_task("task 2")
scheduler.add_task("task 3")
scheduler.process_tasks()    

#converting infix to ostfix

def infix_t0_postfix(expression):
    precedence = {'+': 1, '_': 1, '-':2, '/':2}
    stack = stack()
    output = []

for token in expression.split():
    if token.isnumeric():
        output.appen(token)
    elif token in precedence: 
        while(not stack.is_empty() and stack.peek) in precedence and precedence[stack.peek()] >= precedence[token]:
            output,apppend(stack.pop())
            stack.push(token)
    elif token == '(':  
            stack.push(token)
    elif token == ')':  
        while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
        stack.pop()  
    while not stack.is_empty():
        output.append(stack.pop())

return ''.join(output)        



# Test the infix_to_postfix function
print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  
    

    

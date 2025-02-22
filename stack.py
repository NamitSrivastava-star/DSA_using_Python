class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty')
            return
        return self.stack.pop()  

    def top(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty')
            return
        return self.stack[-1]      
    

if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(9)
    stack1.push(2)
    stack1.push(7)
    stack1.push(3)
    stack1.push(8)  
    print("Top Or Peak item of Stack",stack1.top()) 
    print("Poped item of Stack",stack1.pop()) 
    print("Top Or Peak item of Stack",stack1.top()) 
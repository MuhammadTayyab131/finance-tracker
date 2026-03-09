class Stack:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top =-1
    
    def push(self, value):
        if self.top == self.capacity -1:
            print("Stack overflow")
            return
        else:
            self.top +=1
            self.items[self.top] = value
    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            value = self.items[self.top]
            self.items[self.top]= None
            self.top -=1
            return value
    def peek(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            return self.items[self.top]
    
    def is_empty(self):
        return self.top == -1
    def size(self):
        return self.top +1

# stack = Stack(5)
# stack.push(10)
# stack.push(20)
# stack.push(30)

# print("stack ", stack.items)
# print("Size of stack:", stack.size())
# print("Top Element: ", stack.peek())
# print("Removing top Element: ", stack.pop())
# print("stack after removing top element", stack.items)
# print("size of stack after removing : ", stack.size())


class Queue:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0
    def enqueue(self, value):
        if self.count == self.capacity:
            print("Queue overflow")
            return
        self.rear +=1
        self.items[self.rear] = value
        self.count +=1
    
    def dequeue(self):
        if self.count == 0:
            print("Queue underflow")
            return
        value = self.items[self.front]
        self.items[self.front] = None
        self.front +=1
        self.count -=1
        return value
    
    def peek(self):
        if self.count == 0:
            print("queue underflow")
            return
        return self.items[self.front]
    def is_empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    
# queue = Queue(5)

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)

# print("Queue: ",queue.items)
# print("Size of queue: ", queue.size())
# print("Front Element: ", queue.peek())
# print("Removing front element:", queue.dequeue())
# print("Queue after removing front element: ", queue.items)
# print("Size of queue after removing front element: ", queue.size())



class HashMap:
    def __init__(self,capacity = 5):
        self.capacity = capacity
        self.bucket = [[] for _ in range(capacity)]
    
    def hash_function(self,key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.capacity
    
    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.bucket[index]
        
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
            
        bucket.append([key,value])

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.bucket[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
        
    def remove(self,key):
        index = self.hash_function(key)
        bucket = self.bucket[index]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return

# students = HashMap(5)

# students.put("Tayyab", 67)
# students.put("Kaleem Ullah", 89)
# students.put("Abrar", 91)
# students.put("Shafaqat Ali",98)

# print("Students HashMap: ",students.bucket)
# print("Get tayyab's marks: ", students.get("Tayyab"))

# print("Removing Kaleem Ullah's marks", students.remove("Kaleem Ullah"))
# print("Students HashMap after removing Kaleem Ullah: ", students.bucket)

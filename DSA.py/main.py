from my_structure import Stack, Queue, HashMap

# --------------stack---------------

text = "HELLO"

stack = Stack(10)

for char in text:
    stack.push(char)

reversed_text = ""

while not stack.is_empty():
    reversed_text += stack.pop()

print("Original:", text)
print("Reversed:", reversed_text)



# --------------queue---------------


printer_queue = Queue(5)

printer_queue.enqueue("Document1")
printer_queue.enqueue("Document2")
printer_queue.enqueue("Document3")

print("\nPrinting:", printer_queue.dequeue())
print("Printing:", printer_queue.dequeue())


# --------------hashmap---------------

students = HashMap(5)

students.put("Tayyab", 90)
students.put("Kaleem", 85)
students.put("Abrar", 95)

print("\nTayyab's Marks:", students.get("Tayyab"))
print("Abrar's Marks:", students.get("Abrar"))
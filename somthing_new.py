# import sys

# numbers = list(range(1, 201))
# print(numbers)
# print(sys.getsizeof(numbers))


# def count():
#     list = []
#     i = 1
#     while i <= 200:
#         list.append(i)
#         i += 1
#     return list
# print(count())
# z = sys.getsizeof(count())
# print(z)



# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst

# print(add_item(1))
# print(add_item(2))
# print(add_item(3))


city = ["lahore", "karachi", "islamabad", "peshawar", "quetta"]
# def length(city):
#     return len(city)
# sort = sorted(city, key=length)
# print("sorted list is: ",sort)
sort = sorted(city, key= lambda x: len(x))
print("sorted words of list are: ", sort)

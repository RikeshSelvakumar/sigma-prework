#Input tests
num = [2, 4, 1, 0, 2, -1]
# num = [20, 50, 12, 6, 14, 8]
# num = [100, -100]
# num = []
# num = ["hello", "goodbye"]
# num = [1]

def validate_list(numbers):
    if not numbers:
        print("The list is empty")
        return False
    for i in numbers:
        if not isinstance(i, (int,float)): # Checks for if list contains strings
            print(f"Invalid item: {i} is not a number")
            return False
    return True

#Improved functionality code
def find_min_max(numbers):
    if not validate_list(numbers):
        return [None, None]
    lowest = numbers[0]
    highest = numbers[0]
    for i in numbers:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
    return [lowest, highest]

result = find_min_max(num)
print(result)

# Initial code 
# def find_max(numbers):
#     valid = validate_list(numbers)
#     if not valid:
#         return None
#     highest = numbers[0]
#     for i in numbers:
#         if i > highest:
#             highest = i
#     return highest

# def find_min(numbers):
#     valid = validate_list(numbers)
#     if not valid:
#         return None
#     lowest = numbers[0]
#     for i in numbers:
#         if i < lowest:
#             lowest = i
#     return lowest
# max = find_max(num)
# min = find_min(num)
# print(f"{[min,max]}")






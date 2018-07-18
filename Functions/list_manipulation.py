'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list, command, location, value = None):
    if (command == "add" and location == "end"):
        list.append(value)
        return list
    elif (command == "add" and location == "beginning"):
        list.insert(0, value)
        return list
    elif (command == "remove" and location == "end"):
        return  list.pop()
    elif (command == "remove" and location == "beginning"):
        return  list.pop(0)


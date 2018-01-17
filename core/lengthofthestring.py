def length_of_string(s):
    if type(s) == int:
        return "Sorry integers don't have length"
    elif type(s) == float:
        return "Sorry floats don't have length"
    else:
        return len(s)



print(length_of_string("aaaaaaaaaaa"))
print(length_of_string("   "))
print(length_of_string(5.0))
print(length_of_string(""))
print(length_of_string("Hello"))
print(length_of_string(5))

def age_foo(age):
    new_age = age + 50
    return new_age

age = float(input("Enter your age: "))
if age < 150:
    print(age_foo(age))
else:
    print("How is that possible?")

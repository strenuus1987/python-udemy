def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Temperature cannot be lower than -273.15!"
    else:
        return celsius * 9 / 5 + 32


temperatures=[10,-20,-289,100]

with open("temperatures.txt", 'w') as file:
    for i in temperatures:
        res = celsius_to_fahrenheit(i)
        if type(res) == float:
            file.write(str(res) + "\n")

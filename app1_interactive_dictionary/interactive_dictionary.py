import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_value(key):

    key = key.lower()

    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    elif len(get_close_matches(key, data.keys())) > 0:
        yn = input("Maybe you mean %s? Enter Y if yes, or anything if no. " % get_close_matches(key, data.keys())[0]).lower()
        if yn == "y":
            return data[get_close_matches(key, data.keys())[0]]
        else:
            return "So, there is no such word in our dictionary! Try again."
    else:
        return "There is no such word! Try again."

res = get_value(input("Enter a word: "))

if type(res) == list:
    for item in res:
        print(item)
else:
    print(res)

import json
from difflib import get_close_matches

data = json.load(open("C:/Users/Tariq Ali\Desktop\Python - Sumurai/Dictionary Application/data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        x = input("Did you mean %s instead? If Yes enter 'Y' or if not enter 'N': " % get_close_matches(word, data.keys())[0])
        if x == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif x == "N":
            return "The word does not exist"
        else:
            return "Please select correct option"
    else:
        return "The word doesn't exist."


enter_word = input("Please enter the word: ")
optimize = translate(enter_word)

if type(optimize) == list:
    for output in optimize:
        print(output)
else:
    print(optimize)

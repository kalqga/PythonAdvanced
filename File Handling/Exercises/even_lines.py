import re


def replace_function(text):
    return re.sub(r"[-.\!?,]", "@", text)


with open("text.txt", "r") as file:
    sentence = file.readlines()

    for i in range(len(sentence)):
        if i % 2 == 0:
            replaced = replace_function(sentence[i]).split()

            print(" ".join(replaced[::-1]))

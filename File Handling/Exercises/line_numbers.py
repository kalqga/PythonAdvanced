import re

text_regex = r"[a-zA-Z]"
symbols_regex = r"['-.\!?,]"


def count_stuff(line, pattern):
    return len(re.findall(pattern, line))


counter = 1
with open("text.txt", "r") as file:
    text = file.readlines()

    for sentence in text:
        text_num = count_stuff(sentence, text_regex)
        symb_num = count_stuff(sentence, symbols_regex)
        print(f"Line {counter}: {sentence[:-1]} ({text_num})({symb_num})")

        counter += 1

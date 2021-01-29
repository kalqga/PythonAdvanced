import re


def write_file(name_of_file, info):
    with open(name_of_file, "w") as file:
        file.writelines([f"{key} - {value}""\n" for key, value in info.items()])


def read_file(name_of_file):
    with open(name_of_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-zA-Z']+", text.lower())


first_file = read_file("words.txt")
second_file = read_file("text.txt")

words_counter = {}

for word in first_file:
    if word in second_file:
        words_counter[word] = second_file.count(word)

words_counter = dict(sorted(words_counter.items(), key=lambda x: -x[1]))

write_file("results.txt", words_counter)

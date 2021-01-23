string = input().split(', ')

string_list = [print(f"{word} -> {len(word)}") if word == string[-1] else print(f"{word} -> {len(word)}", end=', ') for word in string]

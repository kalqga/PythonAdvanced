def repeat_text(text, times):
    return text * int(times)


text = input()
times = input()

try:
    print(repeat_text(text, times))
except ValueError:
    print("Variable must be an integer")

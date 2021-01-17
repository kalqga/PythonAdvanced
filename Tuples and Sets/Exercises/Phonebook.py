phonebook = {}

while True:
    data = input().split('-')

    if data[0].isdigit():
        b = int(data[0])
        for _ in range(b):
            name = input()
            if name in phonebook.keys():
                print(f'{name} -> {phonebook[name]}')
            else:
                print(f"Contact {name} does not exist.")
        break
    else:
        phonebook[data[0]] = data[1]

from Modules.Lab.Fibonacci_Sequence.fibonacci import create, locate

while True:

    command = input().split()

    if command[0] == "Stop":
        break
    elif command[0] == "Create":
        print(" ".join(map(str, create(int(command[2])))))
    elif command[0] == "Locate":
        print(locate(int(command[1])))

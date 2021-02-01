from Modules.Lab.Math_Operations.mathematical_operations import add, subtract, divide, multiply, power

data = input().split()

first_number = float(data[0])
sign = data[1]
second_number = int(data[2])

if sign == '+':
    print(f"{add(first_number, second_number):.2f}")
elif sign == '-':
    print(f"{subtract(first_number, second_number):.2f}")
elif sign == '*':
    print(f"{multiply(first_number, second_number):.2f}")
elif sign == '/':
    print(f"{divide(first_number, second_number):.2f}")
elif sign == '^':
    print(f"{power(first_number, second_number):.2f}")
else:
    print(SyntaxError)

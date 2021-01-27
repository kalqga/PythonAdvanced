def age_assignment(*args, **kwargs):
    dic = {}
    for name in args:
        dic[name] = ""
        for n, age in kwargs.items():
            if n == name[0]:
                dic[name] = age
    return dic


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
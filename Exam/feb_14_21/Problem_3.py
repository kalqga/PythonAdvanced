def stock_availability(inventory, parameter, *args):
    if inventory:
        if parameter == 'delivery':
            for arg in args:
                inventory.append(arg)

        elif parameter == 'sell':
            if args:
                for arg in args:
                    if isinstance(arg, int):
                        for _ in range(arg):
                            inventory.pop(0)

                    elif isinstance(arg, str):
                        if arg in inventory:
                            inventory = list(filter(lambda a: a != arg, inventory))

            else:
                inventory.pop(0)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

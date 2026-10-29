#print(type(7/2), 7/2)
#тип - float(оператор / - обычное деление, результат 3.5)
#print(type(7//2), 7//2)
#тип - int(опреатор // - целочисельное деление, результат 3)
#print(type(-7//2), -7//2)
#тип - int(результат минус четыре, округление к меньшему, не к нулю)
#print(type(0.1 + 0.2 == 0.3), 0.1 + 0.2 == 0.3)
#ТИП - bool(результат False, потому что 0.1 + 0.2 == 0.3000000004, десетинные числа работают плохо)
#print(type("3" * 5), "3" * 5)
#тип - string( из за умножения на 5 код напечатает три пятерки)
#print(type(int(3.99)), int(3.99))
#тип - int(результат 3, int всегда округляет в меньшую сторону)
#print(type(bool("False")), bool("False"))
#тип - bool(ответ правддивый поскольку строка не пустая)
#print(type("5" + 5), "5" + 5)(ошибка поскольку int и string нельзя складывать между собой...)


prodname = input("Ener product name: ")
price = float(input("Enter price per piece: "))
amount = int(input("Enter product quantity: "))

total = price * amount
print(f"{prodname}: {price} Kč * {amount} = {total} Kč")

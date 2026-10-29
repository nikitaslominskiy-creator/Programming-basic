count = 0
largest = None

while True:
    line = input("Číslo (Enter = konec): ")
    if line == "":
        break

    number = int(line)
    count += 1
    if largest is None or number > largest:
        largest = number

if count == 0:
    print("Nebylo zadáno žádné číslo.")
else:
    print("Počet:", count)
    print("Maximum:", largest)
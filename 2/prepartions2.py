numbers = [5, 2, 8, 1, 6, 3]

i = 0
count = 0
total = 0

while i < len(numbers):
    n = numbers[i]

    if n == 1:
        break

    if n % 2 == 0:
        total += n
        count += 1

    i += 1

print("Count:", count)
print("Total:", total)
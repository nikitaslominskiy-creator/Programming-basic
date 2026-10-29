largest = float(input("Value #1: "))
smalller = 0
count = 0
first_pos = 1
is_set = False

for i in range(2, 6):
    count = count + 1
    value = float(input(f"Value #{i}: "))
    if value > largest:
        largest = value
        if not is_set:
            first_pos = count
            is_set = True
    elif value < largest:
         smalller = value  
    
print("Largest value:", largest)
print("Smallest value: ", smalller)
print("First appearence of the largest number was on position: ", first_pos)
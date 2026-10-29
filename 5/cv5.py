import math
import datetime

#1-------------------------------------------------
# def circle_area(d):
#     return (math.pi * d**2) / 4

# def tube_cross_section(d_out, d_in):
#     return circle_area(d_out) - circle_area(d_in)

# def tube_mass(d_out, d_in, length, density=7850):
#     volume = tube_cross_section(d_out, d_in) * length
#     return volume * density


# print(f"{tube_mass(0.060, 0.050, 6):.2f}")                
# print(f"{tube_mass(0.060, 0.050, 6, density=2700):.2f}")
#2-------------------------------------------------
# def convert_temperature(value, temp1, temp2):
#     valid_units = {"C", "F", "K"}
#     if temp1 not in valid_units or temp2 not in valid_units:
#         return None

#     if temp1 == "C":
#         celsius = value
#     elif temp1 == "F":
#         celsius = (value - 32) * 5/9
#     else:
#         celsius = value - 273.15


#     if temp2 == "C":
#         return celsius
#     elif temp2 == "F":
#         return celsius * 9/5 + 32
#     else:
#         return celsius + 273.15


# print(f"{convert_temperature(100, "C", "F"):.2f}")   
# print(f"{convert_temperature(0, "K", "C"):.2f}")     
# print(f"{convert_temperature(-40, "C", "F"):.2f}")   
# print(convert_temperature(20, "C", "X")) 
#3-------------------------------------------------
# def mean(values):
#     if not values:
#         return 0.0
#     return sum(values) / len(values)

# def median(values):
#     if not values:
#         return None
#     sortedValues = sorted(values)
#     n = len(sortedValues)
#     mid = n // 2 

#     if n % 2 == 1:
#         return float(sortedValues[mid])
#     else:
#         return(sortedValues[mid - 1] + sortedValues[mid]) / 2

# def std_dev(values):
#     if not values:
#         return 0.0

#     m = mean(values)
#     var = sum((x - m) ** 2 for x in values) / len(values)
#     return math.sqrt(var)

# def min_max(values):
#     if not values:
#         return None, None

#     min = values[0]
#     max= values[0]
#     for val in values[1:]:
#         if val < min:
#             min = val
#         if val > max:
#             max = val

#     return(min, max)

# def summary(values):
#     print(f"'mean': {mean(values)}, 'median': {median((values))}, 'std_dev': {std_dev(values)}, 'min_max': {min_max(values)}")

# data = [2, 4, 4, 4, 5, 5, 7, 9]
# print(summary(data))
#4-------------------------------------------------
# def normalize(birth_number):
#     if not isinstance(birth_number, str):
#         return None
#     clean = birth_number.replace("/", "").replace(" ", "")
#     if len(clean) == 10:    
#         return clean
#     return None

# def per_partes(norm):
#     yy = int(norm[0:2])
#     mm = int(norm[2:4])
#     dd = int(norm[4:6])

#     if 0 <= yy <= 53:
#         year = 2000 + yy
#     else:
#         year = 1900 + yy

#     if 51 <= mm <= 60:
#         month = mm - 50
#         gender = "female"
#     elif 1 <= mm <= 12:
#         month = mm
#         gender = "male"
#     else: 
#         return None

#     return year, month, dd, gender

# def is_Valid(birth_number):
#     norm = normalize(birth_number)
#     if not norm:
#         return False

#     if int(norm) % 11 != 0:
#         return False

#     parts = per_partes(norm)
#     if not parts:
#         return False

#     year, month, dd, _ = parts

#     try:
#         datetime.date(year, month, dd)
#     except ValueError:
#         return False

#     return True

# def gender(birth_number):
#     norm = normalize(birth_number)
#     if not norm or not is_Valid(birth_number):
#         return None
#     return per_partes(norm)[3]

# def birth_date(birth_number):
#     norm = normalize(birth_number)
#     if not norm or not is_Valid(birth_number):
#             return None

#     parts = per_partes(norm)
#     year, month, dd, _ = parts
#     return f"{dd}.{month}.{year}"

# test_cases = ["736028/5163", "990101/1230", "736028/5164"]

# for it in test_cases:
#     valid = is_Valid(it)
#     print(f"Personl num: {it}")
#     print(f" Valid: {valid}")
#     if valid:
#         print(f"Gender: {gender(it)}")
#         print(f"Birth date: {birth_date(it)}")
#     print(("-"*25))
#6-------------------------------------------------
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# def fib(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1

#     return fib(n - 1) + fib(n - 2)

# def fib_iter_count(n):
#     if n <= 0:
#             return 0, 1
#     if n == 1:
#             return 1, 1

#     value1, count1 = fib_iter_count(n - 1)
#     value2, count2 = fib_iter_count(n - 2)
#     return value1 + value2, count1 + count2 + 1

# def fib_iter(n):
#     if n <= 0:
#         return 0, 1
#     if n == 1:
#         return 1, 1

#     a, b = 0, 1
#     for i in range(2, n+1):
#          a, b = b, a + b
#     return b

# def fib_memo(n, memo):
#     if memo is None:
#           memo = {}

#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     if n in memo:
#         return memo[n]

    
#     memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
#     return memo[n]

# print(fib_memo(10, None))
#7-------------------------------------------------
# def hanoi(n, source, target, helper):
#     if n == 1:
#         print(f"{source} -> {target}")
#         return 1
#     count = 0

#     count += hanoi(n - 1, source, helper, target)
#     print(f"{source} -> {target}")
#     count += 1
#     count += hanoi(n - 1, helper, target, source)

#     return count

# total_moves = hanoi(3, 'A', 'C', 'B')
# print(total_moves)
    
    


    
        







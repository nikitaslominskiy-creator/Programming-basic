#1
# diams = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
# deviation = 0.05
# norm = 25.00
# defect = 0
# total = 0
# count = len(diams)

# for i, diam in enumerate(diams, start= 1):
#     if norm - deviation <= diam <= norm + deviation:
#         total += 1
#         print(f"{i:2d}: {diam:.2f} mm == OK")
#     elif diam < norm - deviation:
#         defect += 1
#         print(f"{i:2d}: {diam:.2f} mm == TOO SMALL")
#     elif diam > norm + deviation:
#         defect += 1
#         print(f"{i:2d}: {diam:.2f} mm == TOO BIG")

# proc = (defect/co) * 100

# print(f"Defective parts {defect} from {count} : ({proc:.1f} %)")
#--------------------------------------
#2
# year = int(input("Enter year: "))
# if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
#     print(f"{year} is leap")
# else:
#     print(f"{year} is not leap")
#--------------------------------------

# leap = []
# string_size = 10
# count = 0
# for year in range(1890, 2031):
#     if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
#         leap.append(year)
#         count = count + 1

# for i in range(0, len(leap), string_size):
#     string = leap[i : i + string_size]
#     print((", ").join(map(str, string)))

# print(f"\nAll leap yers: {len(leap)}")
#--------------------------------------
#3
# import math
# num = int(input("Enter number: "))

# if num < 2:
#     print(f"Number {num} is not prime number")
# else: 
#     isPrime = True
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             isPrime = False
#             break

# if isPrime:
#     print("The number is primme")
# else:
#     print("The number is not prime")
#--------------------------------------

# import math

# string_size = 5
# primenums = []
# for num in range(0,100):
#     if num < 2:
#         isPrime = False
#     else: 
#         isPrime = True
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 isPrime = False
                
#     if isPrime:
#         primenums.append(num)

# for i in range(0, len(primenums), string_size):
#     string = primenums[i : i + string_size]
#     print((", ").join(map(str, string)))
#--------------------------------------

# num = int(input("Enter number: "))
# enterednum = num
# remain = 1
# delitel = 2
# mutipliers = []

# while delitel * delitel <= num:
#     if num % delitel == 0:
#         mutipliers.append(delitel)
#         num = num // delitel
        
#     else:
#         delitel += 1

# if num > 1:
#     mutipliers.append(num)

# resut_str = " * ".join(map(str, mutipliers))
# print(f"{enterednum}:  {resut_str}")
#--------------------------------------
#4
# height_true = False

# while height_true == False:
#     height = int(input("Enter height(must be odd): "))
#     if(height % 2 == 0 or height < 0):
#         height = int(input("Enter height(must be odd): "))
#     else:
#         height_true = True
#         k = height//2

#         for r in range(height):
#             if r <= k:
#                 stars = 2*r + 1       
#             else:
#                 stars = 2*(height - 1 - r) + 1
#             spaces =  (height - stars) // 2
#             print(" " * spaces, "*" * stars)
#--------------------------------------
#6

# def f(x):
#     return x**3 - 2 * x - 5 

# low = 2.0
# top = 3.0
# aim = 0.000001
# iteration = 0



# while(top - low) / 2 > aim:
#     middle = (low + top) / 2
#     iteration += 1

#     if f(middle) == 0:
#         break
#     elif f(low) * f(middle) < 0:
#         top = middle
#     else:
#         low = middle

# root = (low + top)/2
# print(f"The root is {root:.6f}")
# print(f"Num of iterations = {iteration}")
#--------------------------------------
#7
import math

velocity = 20.0
angel = 45.0
g = 9.81
alpa = math.radians(45)

primedistance = 40.77
primeheight = 10.19
primetime = 2.88

dts = [0.1, 0.01, 0.001]

print(f"{"dt":<8} | {"Flying time (s)":<14} | {'Distance (m)':<14} | {'Max Height (m)':<15} | {'Δ Time':<10} | {'Δ Distance':<12} | {'Δ Height':<10}")

for dt in dts:
    t = 0.0
    x = 0.0
    y = 0.0
    vx = velocity * math.cos(alpa)
    vy = velocity * math.sin(alpa)

    max_y = 0

    while y >= 0:
        max_y = max(max_y, y)
        x_past, y_past, t_past = x, y, t

        x += vx * dt
        y += vy * dt 
        vy -= g * dt
        t += dt

    fraction = -y_past / (y - y_past)
    t_final = t_past + fraction * dt
    x_final = x_past + fraction * (x - x_past)

    d_time = abs(t_final - primetime)
    d_distance = abs(x_final - primedistance)
    d_height = abs(max_y - primeheight)

    print(f"{dt:<8} | {t_final:<16.3f} | {x_final:<14.3f} | {max_y:<15.3f} | {d_time:<10.3f} | {d_distance:<12.3f} | {d_height:<10.3f}")






#1
# length = float(input("Enter length [mm]: "))

# sm = length / 100
# m = length / 1000
# inch = length / 25.4

# print(f"{length:.3f} mm = {sm:.3f} sm = {m:.3f} = m {inch:.3f} in")
#--------------------------------------
#2

# time = int(input("Enter time [s]: "))

# days = time // 86400
# remainingsec= time % 86400

# hours = remainingsec // 3600
# remainingsec = remainingsec % 3600

# minutes = remainingsec // 60
# remainingsec = remainingsec % 60

# if(days > 0):
#     print(f"{days}:{hours:02d}:{minutes:02d}:{remainingsec:02d}")
# else:
#      print(f"{hours:02d}:{minutes:02d}:{remainingsec:02d}")   
#--------------------------------------
#3

# word = input("Enter a word: ")

# length = len(word)
# firs_char = word[0]
# last_char = word[-1]
# upper = word.upper()
# reverse = word[::-1]

# is_palindrome = word.lower() == reverse.lower()

# print(f"Amount of charachters: {length}")
# print(f"First charchter: {firs_char}")
# print(f"Last charchter: {last_char}")
# print(f"Upper case: {upper}")
# print(f"Reverse: {reverse}")
# print(f"Word is palindrome: {is_palindrome}")
#--------------------------------------
#4

# bit_depth = [8, 16, 32, 64] 
# for bit in bit_depth:
#     pos_min = 0
#     pos_max = 2**bit - 1
#     neg_min = -2**(bit - 1)
#     neg_max = 2**(bit - 1) - 1
#     print(f"For {bit} bits positive from {pos_min} to {pos_max} negative from {neg_min} to {neg_max}")
#--------------------------------------
#5

# num = int(input("Enter a positive number: "))
# div = num
# bits = []
# if(num > 0):
#     while(div > 0):
#         remain = div % 2
#         bits.append(str(remain))        
#         div = div // 2

#     bin_string = "".join(reversed(bits))


# elif(num == 0):
#       bin_string = "0"
    
# elif(num < 1):
#         print("ERROR 324(You have entered a negative number try again)")
#         exit()

# bits_count = len(bin_string)
# one_amount = bin_string.count("1")
# print(f"Binar number = {bin_string}")
# print(f"Check number = {bin(num)}")
# print(f"Amount of bits = {bits_count}")
# print(f"Amount of ones = {one_amount}")   
#--------------------------------------
#6

# text = input("Enter text: ")

# symbols_count = len(text)
# bait_count = 0

# for symbol in text:
#     baits = len(symbol.encode("utf-8"))
#     bait_count = bait_count + baits
#     print(f"{symbol}  {ord(symbol):04X}  {baits} B")

# print(f"Number of charachters: {symbols_count},  Number of baits: {bait_count}")
#--------------------------------------
#7

text = input("Enter text: ")
amount = 0

f = {}

for symbol in text.lower():
    if symbol.isalpha():
        if symbol in f:
            f[symbol] += 1
        else:
            f[symbol] = 1 
            amount += 1  


sorted = sorted(f)

print(sorted)

print(f"Amount of different charachters: {amount}")



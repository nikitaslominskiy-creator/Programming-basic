file_name = "poznamky.txt"

num_of_lines = 0
num_of_not_empthy_lines = 0
num_of_symbols = 0

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        num_of_lines += 1

        clean_line = line.strip("\r\n")

        num_of_symbols += len(clean_line)

        if clean_line.strip():
            num_of_not_empty_lines += 1
            print(f"{num_of_not_empty_lines}. {clean_line}")

print(num_of_lines)
print(num_of_not_empty_lines)
print(num_of_symbols)

        

    


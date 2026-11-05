from datetime import datetime

#1
# def text_statistic(path):
#     with open(path, "r", encoding="utf-8") as file:
#         num_of_lines = 0
#         num_of_not_empthy_lines = 0
#         num_of_words = 0
#         num_of_symbols = 0
#         the_longest_line = 0
        

#         for line in file:
#             num_of_lines += 1

#             clean_line = line.strip("\r\n")
#             num_of_symbols += len(clean_line)

#             if the_longest_line < len(clean_line):
#                 the_longest_line = len(clean_line)

#             if clean_line.strip():
#                 num_of_not_empthy_lines += 1

#             words = clean_line.split()
#             num_of_words += len(words)

#         return  {
#             "Number of lines" : num_of_lines,
#             "Number of not empthy lines" : num_of_not_empthy_lines,
#             "Number of words" : num_of_words,
#             "Number of symbols" : num_of_symbols,
#             "The longest line" : the_longest_line
#         }

# if __name__ == "__main__":
#     path = input("Enter path to the txt file: ")

#     try:
#         stats = text_statistic(path)

#         print(f"Number of lines: {stats["Number of lines"]}")
#         print(f"Number of not empthy lines: {stats["Number of not empthy lines"]}")
#         print(f"Number of words: {stats["Number of words"]}")
#         print(f"Number of symbols: {stats["Number of symbols"]}")
#         print(f"Lengh of the longest line:  {stats["The longest line"]}")

#     except (FileNotFoundError, OSError):
#         print(f"Error: file is not found")
#------------------------------------------------------------------------------
# 2

FILE_NAME = "journal.txt"

def add(text):
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"{time} | {text}"
    with open(FILE_NAME, "a", encoding="utf-8") as journal:
        journal.write(entry)
    print("Note was added succesfully")

def list():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("The journal is empthy")
                return

            for index, line in enumerate(lines, start = 1):
                print(f"{index}. {line.strip()}")

    except (FileNotFoundError, OSError):
        print(f"Error: file is not found")    

def search(text):
    try:
        found = False
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for index, line in enumerate(lines, start = 1):
                if text.lower() in line.lower():
                    print(f"{index}. {line}")
                    found = True

            if not found:
                print("Error: The requested element is not found")

    except(FileNotFoundError, OSError):
           print(f"Error: file is not found")

add("Dokončit laboratorní protokol")
list()
search("protokol")

                                       

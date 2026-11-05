#1
def text_statistic(path):
    with open(path, "r", encoding="utf-8") as file:
        num_of_lines = 0
        num_of_not_empthy_lines = 0
        num_of_words = 0
        num_of_symbols = 0
        the_longest_line = 0
        

        for line in file:
            num_of_lines += 1

            clean_line = line.strip("\r\n")
            num_of_symbols += len(clean_line)

            if the_longest_line < len(clean_line):
                the_longest_line = len(clean_line)

            if clean_line.strip():
                num_of_not_empthy_lines += 1

            words = clean_line.split()
            num_of_words += len(words)

        return  {
            "Number of lines" : num_of_lines,
            "Number of not empthy lines" : num_of_not_empthy_lines,
            "Number of words" : num_of_words,
            "Number of symbols" : num_of_symbols,
            "The longest line" : the_longest_line
        }

if __name__ == "__main__":
    path = input("Enter path to the txt file: ")

    try:
        stats = text_statistic(path)

        print(f"Number of lines: {stats["Number of lines"]}")
        print(f"Number of not empthy lines: {stats["Number of not empthy lines"]}")
        print(f"Number of words: {stats["Number of words"]}")
        print(f"Number of symbols: {stats["Number of symbols"]}")
        print(f"Lengh of the longest line:  {stats["The longest line"]}")

    except (FileNotFoundError, OSError):
        print(f"Error: file is not found")
        

                                       

from solutions.day_one.word_to_number import WORD_TO_NUMBER

def read_text_file():
    text_file_lines = []
    with open("solutions/day_one/temp.txt", "r") as f:
        text_file_lines = f.readlines()
        text_file_lines = [line.strip() for line in text_file_lines if line.strip() != ""]
    return text_file_lines

def convert_word_to_int(word):
    try:
        return WORD_TO_NUMBER[word]
    except KeyError:
        return None

def get_first_and_last_nums(line):
    for key, value in WORD_TO_NUMBER.items():
        if key in line.lower():
            return value


def day_one():
    text_file_lines = read_text_file()
    total_sum = 0
    for line in text_file_lines:
        total_sum += get_first_and_last_nums(line)
    print(f"Sum of all number is: {total_sum}")



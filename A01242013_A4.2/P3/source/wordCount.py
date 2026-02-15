#pylint: disable=invalid-name

"Program computes statistics from a file given"

import argparse
import time

def count_words(words):
    "Function to calculate frequency of words"
    unique_words = list(set(words))
    words_dict = {}

    for word in unique_words:
        count = 0
        for current_word in words:
            if current_word == word:
                count += 1

        words_dict[word] = count

    return words_dict

start_time = time.perf_counter()

parser = argparse.ArgumentParser(description="Process words file")
parser.add_argument("file", help="Name of the file")

input_file = parser.parse_args()
data_list = []
counter = 0


with open(input_file.file, "r", encoding="utf-8") as f:
    for line in f:
        counter += 1
        try:
            data_list.append(str(line.strip()))
        except ValueError:
            print(f"Error of invalid value in line {counter}: {line}")


print(f"Results for {input_file.file}")
words_res = count_words(data_list)
for i, j in words_res.items():
    print(f"{i}: {j}")

print(f"\nTotal count: {counter}")

end_time = time.perf_counter()
run_time = end_time - start_time
print(f"\nTIME: {run_time} seconds")

with open("WordCountResults.txt", "w", encoding="utf-8") as res_f:
    res_f.write(f"Results for {input_file.file}\n")
    for i, j in words_res.items():
        res_f.write(f"{i}: {j} \n")
    res_f.write(f"\nTIME: {run_time} seconds")

#pylint: disable=invalid-name

"Program converts decimal numbers to hexadecimal"

import argparse
import time

def convert_hex(nums):
    "Function to convert a decimal to hexadecimal"
    replace_dict = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    hex_dict = {}

    for num in nums:
        hex_num = ""
        if num < 0:
            num_abs = num * -1
        else:
            num_abs = num

        if num_abs > 0:
            while num_abs != 0:
                remainder = num_abs % 16
                if remainder > 9:
                    hex_num = replace_dict[remainder] + hex_num
                else:
                    hex_num = str(remainder) + hex_num

                num_abs = num_abs // 16
        else:
            hex_num = "0"

        if num < 0:
            hex_num = "-" + hex_num
            hex_dict[num] = hex_num
        else:
            hex_dict[num] = hex_num

    return hex_dict

start_time = time.perf_counter()

parser = argparse.ArgumentParser(description="Process nums file")
parser.add_argument("file", help="Name of the file")

input_file = parser.parse_args()
data_list = []
counter = 0


with open(input_file.file, "r", encoding="utf-8") as f:
    for line in f:
        counter += 1
        try:
            data_list.append(int(line))
        except ValueError:
            print(f"Error of invalid value in line {counter}: {line}")


print(f"Results for {input_file.file}\n")
hex_res = convert_hex(data_list)
print("HEXADECIMAL\n")
for i, j in hex_res.items():
    print(f"{i}: {j}")

end_time = time.perf_counter()
run_time = end_time - start_time
print(f"\nTIME: {run_time} seconds")

with open("ConvertionResults.txt", "w", encoding="utf-8") as res_f:
    res_f.write(f"Results for {input_file.file}\n")
    res_f.write("HEXADECIMAL\n")
    for i, j in hex_res.items():
        res_f.write(f"{i}: {j}")
    res_f.write(f"\nTIME: {run_time} seconds")

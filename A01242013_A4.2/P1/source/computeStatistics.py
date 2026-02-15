#pylint: disable=invalid-name

"Program computes statistics from a file given"

import argparse
import time

def calc_mean(nums):
    "Function to calculate mean"
    mean = 0
    for i in nums:
        mean += i
    mean = mean / len(nums)
    return mean

def calc_median(nums):
    "Function to calculate median"
    for i, _ in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    if len(nums) % 2 == 0:
        median = (nums[int(len(nums)/2)] + nums[(int(len(nums)/2) - 1)]) / 2
    else:
        median = nums[int((len(nums)/2))]

    return median

def calc_mode(nums):
    "Function to calculate mode"
    unique_nums = list(set(nums))
    count = 0
    mode = 0

    for i in unique_nums:
        i_count = nums.count(i)
        if i_count > count or i_count == count:
            mode = i
            count = i_count

    if count == 1:
        mode = None

    return mode

def calc_std_dev(nums, mean):
    "Function to calculate standard deviation"
    sum_var = 0

    for i in nums:
        n = i - mean
        square = n ** 2
        sum_var += square

    variance = sum_var / (len(nums))

    std_dev = variance ** 0.5

    return std_dev

def calc_variance(nums, mean):
    "Function to calculate variance"
    sum_var = 0

    for i in nums:
        n = i - mean
        square = n ** 2
        sum_var += square

    variance = sum_var / (len(nums) - 1)
    return variance

start_time = time.perf_counter()

parser = argparse.ArgumentParser(description="Process numbers file")
parser.add_argument("file", help="Name of the file")

input_file = parser.parse_args()
data_list = []
counter = 0


with open(input_file.file, "r", encoding="utf-8") as f:
    for line in f:
        counter += 1
        try:
            data_list.append(float(line))
        except ValueError:
            print(f"Error of invalid value in line {counter}: {line}")


print(f"Results for {input_file.file}")
print(f"COUNT: {counter}")
mean_res = calc_mean(data_list)
print(f"MEAN: {mean_res}")
median_res = calc_median(data_list)
print(f"MEDIAN: {median_res}")
mode_res = calc_mode(data_list)
print(f"MODE: {mode_res}")
std_dev_res = calc_std_dev(data_list, mean_res)
print(f"SD: {std_dev_res}")
variance_res = calc_variance(data_list, mean_res)
print(f"VARIANCE: {variance_res}")

end_time = time.perf_counter()
run_time = end_time - start_time
print(f"TIME: {run_time} seconds")

with open("StatisticsResults.txt", "w", encoding="utf-8") as res_f:
    res_f.write(f"Results for {input_file.file}\n")
    res_f.write(f"COUNT: {counter}\n")
    res_f.write(f"MEAN: {mean_res}\n")
    res_f.write(f"MEDIAN: {median_res}\n")
    res_f.write(f"MODE: {mode_res}\n")
    res_f.write(f"SD: {std_dev_res}\n")
    res_f.write(f"VARIANCE: {variance_res}\n")
    res_f.write(f"TIME: {run_time} seconds")

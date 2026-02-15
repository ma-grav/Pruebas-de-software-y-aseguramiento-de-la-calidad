#pylint: disable=invalid-name

"Program computes statistics from a file given"

import argparse
import time
import json

def calc_total_sales(products, sales):
    "Function to calculate total sales"
    pass


start_time = time.perf_counter()

parser = argparse.ArgumentParser(description="Process products and sales files")
parser.add_argument("prod_file", help="Name of the products file")
parser.add_argument("sale_file", help="Name of the sales file")


input_file = parser.parse_args()

with open(input_file.prod_file, "r", encoding="utf-8") as products_file, open(input_file.sale_file, "r", encoding="utf-8") as sales_file:
    products_dict = json.load(products_file)
    sales_dict = json.load(sales_file)


print(f"Results for {sales_file}")
total_sales = calc_total_sales(products_dict, sales_dict)
print(f"TOTAL SALES: {total_sales}")

end_time = time.perf_counter()
run_time = end_time - start_time
print(f"TIME: {run_time} seconds")

with open("SalesResults.txt", "w", encoding="utf-8") as res_f:
    res_f.write(f"Results for {sales_file}\n")
    res_f.write(f"TOTAL SALES: {total_sales}\n")
    res_f.write(f"TIME: {run_time} seconds")
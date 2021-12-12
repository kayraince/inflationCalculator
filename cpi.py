num_product_base = int(input("Enter the # of products in the base year: "))
cpi_base_year_total = 0
for i in range(num_product_base):

    base_year_price = float(input("Enter the price of " + str(i + 1) + "th product: "))
    base_year_quantity = int(input("Enter the quantity of " + str(i + 1) + "th product: "))
    cpi_base_year_sum = base_year_quantity * base_year_price
    cpi_base_year_total += cpi_base_year_sum
    if i == num_product_base:
        break
    print(cpi_base_year_total)
cpi_base_year = cpi_base_year_total / cpi_base_year_total * 100
print(cpi_base_year)
num_product_current = int(input("Enter the # of products in the initial year: "))
cpi_current_year_total = 0
for k in range(num_product_current):
    current_year_price = float(input("Enter the price of " + str(k + 1) + "th product: "))
    current_year_quantity = int(input("Enter the quantity of " + str(k + 1) + "th product: "))
    cpi_current_year_sum = current_year_price * current_year_quantity
    cpi_current_year_total += cpi_current_year_sum
    if k == num_product_current:
        break
    print(cpi_current_year_total)
cpi_current_year = cpi_current_year_total / cpi_base_year_total * 100
print(cpi_current_year)
num_product_final_year = int(input("Enter the # of products in the final year: "))
for w in range(num_product_final_year):

inflation = (cpi_current_year - cpi_base_year) / cpi_base_year
print("inflation ")
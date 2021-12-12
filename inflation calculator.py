num_product_base = int(input("Enter the # of products in the base year: "))
cpi_base_year_total = 0
base_year_quantity_list = []
for i in range(num_product_base):

    base_year_price = float(input("Enter the price of " + str(i + 1) + "th product in base year: "))
    base_year_quantity: int = int(input("Enter the quantity of " + str(i + 1) + "th product: "))
    base_year_quantity_list.append(base_year_quantity)
    cpi_base_year_sum = base_year_price * base_year_quantity_list[i]
    cpi_base_year_total += cpi_base_year_sum
    if i == num_product_base:
        break
    print(cpi_base_year_total)
    print(base_year_quantity_list)
cpi_base_year = cpi_base_year_total / cpi_base_year_total * 100
print(cpi_base_year)


cpi_current_year_total = 0
for k in range(num_product_base):
    current_year_price = float(input("Enter the price of " + str(k + 1) + "th product in previous year before final year: "))
    
    cpi_current_year_sum = current_year_price * base_year_quantity_list[k]
    cpi_current_year_total += cpi_current_year_sum
    if k == num_product_base:
        break
    print(cpi_current_year_total)
cpi_current_year = cpi_current_year_total / cpi_base_year_total * 100
print(cpi_current_year)

cpi_final_year_total = 0
for w in range(num_product_base):
    final_year_price = float(input("Enter the price of " + str(w + 1) + "th product in final year: "))
    
    cpi_final_year_sum = final_year_price * base_year_quantity_list[w]
    cpi_final_year_total += cpi_final_year_sum
    if w == num_product_base:
        break
    print(cpi_final_year_total)
cpi_final_year = cpi_final_year_total / cpi_base_year_total * 100


inflation = (cpi_final_year - cpi_current_year) / cpi_current_year
print("Price inflation is " + str(inflation * 100) + "%.")


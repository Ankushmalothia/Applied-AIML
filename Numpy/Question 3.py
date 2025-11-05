#You are provided with 2 lists that contain the data of an ecommerce website.
# The first list contains the data for the number of items sold for a particular product and the second list contains the price of the product sold.
# As a part of this exercise, solve the questions that are provided below.

#1. How many different products are sold by the company in total?
#2. How many items were sold in total?
#3. What is the average price of the products sold by the e-commerce company?
#4. What is the price of the costliest item sold?
#5. What is the total revenue of the company? [Revenue = Price*Quantity]
#6. Demand for the 20th product on the list is higher than that for the 50th product. [True/False]
#7. How many products fall under the category of expensive goods? An expensive good is one whose price is higher than the average price of the products sold by the company.


import numpy as np

number = [8, 9, 9, 1, 6, 9, 5, 7, 3, 9, 7, 3, 4, 8, 3, 5, 8, 4, 8, 7, 5, 7, 3, 6, 1, 2, 7, 4, 7, 7, 8, 4, 3, 4, 2, 2, 2, 7, 3, 5, 6, 1, 1, 3, 2, 1, 1, 7, 7, 1, 4, 4, 5, 6, 1, 2, 7, 4, 5, 8, 1, 4, 8, 6, 2, 4, 3, 7, 3, 6, 2, 3, 3, 3, 2, 4, 6, 8, 9, 3, 9, 3, 1, 8, 6, 6, 3, 3, 9, 4, 6, 4, 9, 6, 7, 1, 2, 8, 7, 8, 1, 4]
price = [195, 225, 150, 150, 90, 60, 75, 255, 270, 225, 135, 195, 30, 15, 210, 105, 15, 30, 180, 60, 165, 60, 45, 225, 180, 90, 30, 210, 150, 15, 270, 60, 210, 180, 60, 225, 150, 150, 120, 195, 75, 240, 60, 45, 30, 180, 240, 285, 135, 165, 180, 240, 60, 105, 165, 240, 120, 45, 120, 165, 285, 225, 90, 105, 225, 45, 45, 45, 75, 180, 90, 240, 30, 30, 60, 135, 180, 15, 255, 180, 270, 135, 105, 135, 210, 180, 135, 195, 225, 75, 225, 15, 240, 60, 15, 180, 255, 90, 15, 150, 230, 150]

diffent_items_sold = len(number)
print("Total different products sold by the company:", diffent_items_sold)

total_items_sold = np.sum(number)
print("Total items sold by the company:", total_items_sold)

average_price = np.mean(price)
print("Average price of the products sold by the company:", average_price)

costliest_item_price = np.max(price)
print("Price of the costliest item sold by the company:", costliest_item_price)

total_revenue = np.sum(np.array(number) * np.array(price))
print("Total revenue of the company:", total_revenue)

demand_higher_20th_50th = number[19] > number[49]
print("Demand for the 20th product is higher than that for the 50th product:", demand_higher_20th_50th)

expensive_goods_count = np.sum(np.array(price) > average_price)
print("Number of products that are expensive goods:", expensive_goods_count)
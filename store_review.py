products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products
total_price = sum(prices)
average_price = total_price / len(prices)
print("Total Price Average:", average_price)

# Create a new price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Calculate the total revenue generated from the products
total_revenue = 0
for i in range(len(products)):
    product_revenue = prices[i] * last_week[i]
    total_revenue += product_revenue
print("Total Revenue:", total_revenue)

# Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / 7  # Assuming 7 days in a week
print("Average Daily Revenue:", average_daily_revenue)

# Based on the new prices, identify products less than $30
products_less_than_30 = []
for i in range(len(products)):
    if new_prices[i] < 30:
        products_less_than_30.append(products[i])
print("Products Less Than $30:", products_less_than_30)

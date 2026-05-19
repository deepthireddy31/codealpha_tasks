# Step 1: Create a dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
}

# Step 2: Initialize total investment
total_investment = 0

print(" Welcome to Stock Portfolio Tracker")

# Step 3: Ask user how many stocks they want to enter
n = int(input("Enter number of stocks: "))

# Step 4: Loop to get stock details
for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Step 5: Check if stock exists
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment for {stock_name}: ${investment}")

    else:
        print(" Stock not found!")

# Step 6: Display total investment
print("\n Total Investment Value: $", total_investment)

# Step 7: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print(" Portfolio saved to portfolio.txt")
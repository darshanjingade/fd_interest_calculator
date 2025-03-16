import pandas as pd

# Constants
monthly_deposit = 20000  # Monthly deposit in INR
interest_rate = 7.25 / 100  # Annual interest rate
years_of_deposit = 10  # First 10 years of monthly deposits
years_total = 25  # Total years for the investment
compounding_frequency = 1  # Compounding frequency (annually)

# Function to calculate FD value for each year considering monthly deposits
def calculate_fd_value(monthly_deposit, interest_rate, years):
    # Total amount invested each year
    total_invested = monthly_deposit * 12 * years
    # Apply the compound interest formula for monthly contributions
    future_value = 0
    for year in range(1, years + 1):
        # For each deposit made, calculate its compounded value after the relevant years
        future_value += monthly_deposit * 12 * ((1 + interest_rate) ** (years - year + 1) - 1) / interest_rate
    return future_value

# Initialize an empty list for each year's final FD amount
fd_values = []

# Calculate FD values for each year
for year in range(1, years_total + 1):
    if year <= years_of_deposit:
        # Yearly calculation for first 10 years (with monthly deposits)
        fd_value = calculate_fd_value(monthly_deposit, interest_rate, year)
    else:
        # After 10 years, no new deposits, only compounding interest on the accumulated value
        fd_value = fd_values[years_of_deposit - 1] * (1 + interest_rate) ** (year - years_of_deposit)
    fd_values.append(fd_value)

# Create a table with years and corresponding FD values
df = pd.DataFrame({
    'Year': list(range(1, years_total + 1)),
    'FD Value (INR)': [round(value, 2) for value in fd_values]
})

# Show the table
print(df.head(25))

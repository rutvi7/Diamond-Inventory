import pandas as pd
from datetime import datetime

# Load the diamonds data
diamonds_file = 'diamonds.csv'
diamonds_df = pd.read_csv(diamonds_file)

# Authentication for manager
def authenticate_manager():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username == "rutvi" and password == "R123@":
        return True
    elif username == "Jeevna" and password == "J123@":
        return True
    else:
        print("Authentication failed!")
        return False

# Adjust prices
def adjust_prices(diamonds_df):
    try:
        adjustment = float(input("Enter percentage to adjust prices (e.g., 10 for +10%, -10 for -10%): "))
        confirm = input(f"This will adjust prices by {adjustment}%. Do you want to proceed? (yes/no): ").strip().lower()
        if confirm == 'yes':
            diamonds_df['total_sales_price'] = diamonds_df['total_sales_price'] * (1 + adjustment / 100)
            print("Prices adjusted successfully.")
            return diamonds_df, adjustment
        else:
            print("Operation canceled.")
            return diamonds_df, None
    except Exception as e:
        print(f"Error: {e}")
        return diamonds_df, None

# Logging adjustments
def log_adjustment(adjustment, reason):
    if adjustment is not None:
        with open("adjustment_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} | Adjustment: {adjustment}% | Reason: {reason}\n")
        print("Adjustment logged.")
    else:
        print("No adjustment to log.")

# Main script
if __name__ == "__main__":
    if authenticate_manager():
        reason = input("Enter reason for price adjustment: ").strip()
        diamonds_df, adjustment = adjust_prices(diamonds_df)
        log_adjustment(adjustment, reason)
        if adjustment is not None:
            # Overwrite the original diamonds.csv file
            diamonds_df.to_csv(diamonds_file, index=False)
            print(f"Prices updated directly in '{diamonds_file}'.")
    else:
        print("Access denied.")


import pandas as pd

# Load the data files
diamonds_df = pd.read_csv('diamonds.csv')
order_details_df = pd.read_csv('order_details.csv')

# Group the sales by color and clarity
sales_summary = order_details_df.groupby(['cut', 'clarity']).size().reset_index(name='sold_quantity')

# Merge sales summary with diamonds stock to understand the remaining stock
diamonds_stock_summary = diamonds_df.groupby(['cut', 'clarity']).size().reset_index(name='stock_quantity')

# Merge the sales summary with stock summary
inventory_status = pd.merge(diamonds_stock_summary, sales_summary, on=['cut', 'clarity'], how='left')

# Fill NaN values in sold_quantity with 0 (no sales for that category)
inventory_status['sold_quantity'] = inventory_status['sold_quantity'].fillna(0)

# Calculate remaining stock
inventory_status['remaining_stock'] = inventory_status['stock_quantity'] - inventory_status['sold_quantity']

# Flag low stock items (threshold can be customized; using 5 as default)
low_stock_threshold = 5
inventory_status['low_stock'] = inventory_status['remaining_stock'] < low_stock_threshold

# Save the results to a new CSV file
inventory_status.to_csv('inventory_status.csv', index=False)

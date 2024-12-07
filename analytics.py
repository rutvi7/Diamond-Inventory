import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, OptionMenu

# Load the diamonds data
diamonds_file = 'diamonds.csv'
diamonds_df = pd.read_csv(diamonds_file)

# Perform analytics: Group by shape (cut) and carat
analytics_df = diamonds_df.groupby(['cut', 'carat_weight']).size().reset_index(name='stone_count')


# Function to plot the graph for the selected shape
def plot_shape_graph(shape):
    # Filter data for the selected shape
    shape_data = analytics_df[analytics_df['cut'] == shape]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(
        shape_data['carat_weight'],
        shape_data['stone_count'],
        color='skyblue',  # Customizable color
        alpha=0.7
    )

    # Add labels and title
    plt.xlabel('Carat Weight')
    plt.ylabel('Stone Count')
    plt.title(f'Stone Availability for {shape} Shape')
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Show the plot
    plt.tight_layout()
    plt.show()


# Function to handle dropdown selection
def on_select(*args):
    selected_shape = shape_var.get()
    plot_shape_graph(selected_shape)


# Tkinter GUI setup
root = Tk()
root.title("Select Diamond Shape")

# Dropdown setup
shapes = analytics_df['cut'].unique()
shape_var = StringVar(root)
shape_var.set(shapes[0])  # Default value

# Create the dropdown and button
Label(root, text="Select Diamond Shape:").pack(pady=10)
dropdown = OptionMenu(root, shape_var, *shapes)
dropdown.pack(pady=10)
Button(root, text="Show Graph", command=on_select).pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

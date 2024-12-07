from diamond_gui import DiamondRecommendationSystem  # Import the reusable class
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os


class DiamondOrderGUI:
    def __init__(self, master, order_system):
        self.master = master
        self.order_system = order_system

        master.title("Diamond Order System")

        # Load the sold stones list from file
        self.sold_stones = self.load_sold_stones()

        # Dropdown Menus and Input Fields
        tk.Label(master, text="Cut:").grid(row=0, column=0, padx=8, pady=5)
        self.cut_var = tk.StringVar()
        self.cut_menu = ttk.Combobox(master, textvariable=self.cut_var, state="readonly")
        self.cut_menu['values'] = order_system.get_unique_values('cut')
        self.cut_menu.grid(row=0, column=1, padx=8, pady=5)

        tk.Label(master, text="Carat Min:").grid(row=1, column=0, padx=8, pady=5)
        self.carat_min_var = tk.DoubleVar()
        self.carat_min_menu = ttk.Combobox(master, textvariable=self.carat_min_var, state="readonly")
        self.carat_min_menu['values'] = order_system.get_unique_values('carat')
        self.carat_min_menu.grid(row=1, column=1, padx=8, pady=5)

        tk.Label(master, text="Carat Max:").grid(row=2, column=0, padx=8, pady=5)
        self.carat_max_var = tk.DoubleVar()
        self.carat_max_menu = ttk.Combobox(master, textvariable=self.carat_max_var, state="readonly")
        self.carat_max_menu['values'] = order_system.get_unique_values('carat')
        self.carat_max_menu.grid(row=2, column=1, padx=8, pady=5)

        tk.Label(master, text="Clarity:").grid(row=3, column=0, padx=8, pady=5)
        self.clarity_var = tk.StringVar()
        self.clarity_menu = ttk.Combobox(master, textvariable=self.clarity_var, state="readonly")
        self.clarity_menu['values'] = order_system.get_unique_values('clarity')
        self.clarity_menu.grid(row=3, column=1, padx=8, pady=5)

        tk.Label(master, text="Cut Quality:").grid(row=4, column=0, padx=8, pady=5)
        self.cut_quality_var = tk.StringVar()
        self.cut_quality_menu = ttk.Combobox(master, textvariable=self.cut_quality_var, state="readonly")
        self.cut_quality_menu['values'] = order_system.get_unique_values('cut_quality')
        self.cut_quality_menu.grid(row=4, column=1, padx=8, pady=5)

        tk.Label(master, text="Lab:").grid(row=5, column=0, padx=8, pady=5)
        self.lab_var = tk.StringVar()
        self.lab_menu = ttk.Combobox(master, textvariable=self.lab_var, state="readonly")
        self.lab_menu['values'] = order_system.get_unique_values('lab')
        self.lab_menu.grid(row=5, column=1, padx=8, pady=5)

        tk.Label(master, text="Customer Name:").grid(row=6, column=0, padx=8, pady=5)
        self.customer_name_var = tk.StringVar()
        self.customer_name_entry = tk.Entry(master, textvariable=self.customer_name_var)
        self.customer_name_entry.grid(row=6, column=1, padx=8, pady=5)

        tk.Label(master, text="Number of Stones:").grid(row=7, column=0, padx=8, pady=5)
        self.num_stones_var = tk.IntVar()
        self.num_stones_entry = tk.Entry(master, textvariable=self.num_stones_var)
        self.num_stones_entry.grid(row=7, column=1, padx=8, pady=5)

        # Buttons
        self.order_button = tk.Button(master, text="Place Order", command=self.place_order)
        self.order_button.grid(row=8, column=0, columnspan=2, pady=8)

        # Results Display
        self.results_frame = tk.Frame(master)
        self.results_frame.grid(row=9, column=0, columnspan=2, pady=8)

        self.results = tk.Text(self.results_frame, height=15, width=80)
        self.results.pack()

    def load_sold_stones(self):
        """Load sold stones from file to keep track of unavailable stock."""
        if os.path.exists("sold_stones.csv"):
            sold_stones = pd.read_csv("sold_stones.csv")["stock_id"].tolist()
            return set(sold_stones)
        return set()

    def update_sold_stones(self, sold_ids):
        """Update the sold stones file."""
        with open("sold_stones.csv", mode="a") as file:
            pd.DataFrame({"stock_id": sold_ids}).to_csv(file, index=False, header=file.tell() == 0)

    def place_order(self):
        # Get user input
        cut = self.cut_var.get().strip()
        carat_min = self.carat_min_var.get()
        carat_max = self.carat_max_var.get()
        clarity = self.clarity_var.get().strip()
        cut_quality = self.cut_quality_var.get().strip()
        lab = self.lab_var.get().strip()
        customer_name = self.customer_name_var.get().strip()
        num_stones = self.num_stones_var.get()

        # Validate input
        if not cut or not carat_min or not carat_max or not clarity or not cut_quality or not lab or not customer_name or num_stones <= 0:
            messagebox.showerror("Input Error", "Please fill in all fields and specify a valid number of stones.")
            return

        if carat_min > carat_max:
            messagebox.showerror("Input Error", "Carat Min cannot be greater than Carat Max.")
            return

        # Filter diamonds based on criteria
        filtered = self.order_system.filter_diamonds(
            cut=cut, carat_min=carat_min, carat_max=carat_max, clarity=clarity, cut_quality=cut_quality, lab=lab
        )

        # Exclude sold stones
        filtered = filtered[~filtered["stock_id"].isin(self.sold_stones)]

        self.results.delete(1.0, tk.END)  # Clear previous results

        if filtered is not None and not filtered.empty:
            if num_stones > len(filtered):
                messagebox.showerror("Input Error", f"Only {len(filtered)} stones are available for the selected criteria.")
                return

            # Select the top stones based on availability
            selected_stones = filtered.head(num_stones)
            total_price = selected_stones['total_sales_price'].sum()
            total_carat = selected_stones['carat'].sum()

            # Update sold stones
            sold_ids = selected_stones["stock_id"].tolist()
            self.update_sold_stones(sold_ids)
            self.sold_stones.update(sold_ids)

            # Save order details to a file
            selected_stones["Customer Name"] = customer_name
            selected_stones.to_csv("order_details.csv", mode="a", index=False, header=not os.path.exists("order_details.csv"))

            # Display order summary
            self.results.insert(tk.END, f"Order Details for {customer_name}:\n")
            self.results.insert(tk.END, f"Total Stones: {num_stones}\n")
            self.results.insert(tk.END, f"Total Carat: {total_carat:.2f}\n")
            self.results.insert(tk.END, f"Total Price: ${total_price:,.2f}\n")
            self.results.insert(tk.END, f"Order saved to 'order_details.csv'.\n")
        else:
            self.results.insert(tk.END, "No diamonds match the given criteria.")

    def clear_fields(self):
        # Reset all fields
        self.cut_var.set("")
        self.carat_min_var.set("")
        self.carat_max_var.set("")
        self.clarity_var.set("")
        self.cut_quality_var.set("")
        self.lab_var.set("")
        self.customer_name_var.set("")
        self.num_stones_var.set(0)
        self.results.delete(1.0, tk.END)


# Main Function
if __name__ == "__main__":
    FILE_PATH = "diamonds.csv"  # Update this to your dataset's file path
    order_system = DiamondRecommendationSystem(FILE_PATH)  # Reusing the imported class

    root = tk.Tk()
    gui = DiamondOrderGUI(root, order_system)  # Pass the instance to the GUI
    root.mainloop()

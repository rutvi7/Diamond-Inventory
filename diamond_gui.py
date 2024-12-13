import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox


class DiamondRecommendationSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, low_memory=False)
        print("Dataset loaded successfully with", len(self.df), "rows.")
        if 'carat_weight' in self.df.columns:
            self.df.rename(columns={'carat_weight': 'carat'}, inplace=True)

    def get_unique_values(self, column_name):
        """Return unique values for a column."""
        if column_name in self.df.columns:
            return sorted(self.df[column_name].dropna().unique())
        return []

    def filter_diamonds(self, cut, carat_min, carat_max, clarity, cut_quality, lab):
        required_columns = {'cut', 'carat', 'clarity', 'cut_quality', 'lab', 'total_sales_price', 'stock_id'}
        if not required_columns.issubset(self.df.columns):
            missing = required_columns - set(self.df.columns)
            messagebox.showerror("Data Error", f"Missing columns in dataset: {', '.join(missing)}")
            return None

        # Apply filtering logic
        filtered = self.df[
            (self.df['cut'].str.lower() == cut.lower()) &
            (self.df['carat'] >= carat_min) &
            (self.df['carat'] <= carat_max) &
            (self.df['clarity'].str.lower() == clarity.lower()) &
            (self.df['cut_quality'].str.lower() == cut_quality.lower()) &
            (self.df['lab'].str.lower() == lab.lower())
        ]
        return filtered[["stock_id", "cut", "carat", "clarity", "cut_quality", "lab", "total_sales_price"]]


class DiamondGUI:
    def __init__(self, master, recommendation_system):
        self.master = master
        self.recommendation_system = recommendation_system

        master.title("Diamond Recommendation System")

        # Dropdown Menus
        tk.Label(master, text="Cut:").grid(row=0, column=0, padx=8, pady=5)
        self.cut_var = tk.StringVar()
        self.cut_menu = ttk.Combobox(master, textvariable=self.cut_var, state="readonly")
        self.cut_menu['values'] = recommendation_system.get_unique_values('cut')
        self.cut_menu.grid(row=0, column=1, padx=8, pady=5)

        tk.Label(master, text="Carat Min:").grid(row=1, column=0, padx=8, pady=5)
        self.carat_min_var = tk.DoubleVar()
        self.carat_min_menu = ttk.Combobox(master, textvariable=self.carat_min_var, state="readonly")
        self.carat_min_menu['values'] = recommendation_system.get_unique_values('carat')
        self.carat_min_menu.grid(row=1, column=1, padx=8, pady=5)

        tk.Label(master, text="Carat Max:").grid(row=2, column=0, padx=8, pady=5)
        self.carat_max_var = tk.DoubleVar()
        self.carat_max_menu = ttk.Combobox(master, textvariable=self.carat_max_var, state="readonly")
        self.carat_max_menu['values'] = recommendation_system.get_unique_values('carat')
        self.carat_max_menu.grid(row=2, column=1, padx=8, pady=5)

        tk.Label(master, text="Clarity:").grid(row=3, column=0, padx=8, pady=5)
        self.clarity_var = tk.StringVar()
        self.clarity_menu = ttk.Combobox(master, textvariable=self.clarity_var, state="readonly")
        self.clarity_menu['values'] = recommendation_system.get_unique_values('clarity')
        self.clarity_menu.grid(row=3, column=1, padx=8, pady=5)

        tk.Label(master, text="Cut Quality:").grid(row=4, column=0, padx=8, pady=5)
        self.cut_quality_var = tk.StringVar()
        self.cut_quality_menu = ttk.Combobox(master, textvariable=self.cut_quality_var, state="readonly")
        self.cut_quality_menu['values'] = recommendation_system.get_unique_values('cut_quality')
        self.cut_quality_menu.grid(row=4, column=1, padx=8, pady=5)

        tk.Label(master, text="Lab:").grid(row=5, column=0, padx=8, pady=5)
        self.lab_var = tk.StringVar()
        self.lab_menu = ttk.Combobox(master, textvariable=self.lab_var, state="readonly")
        self.lab_menu['values'] = recommendation_system.get_unique_values('lab')
        self.lab_menu.grid(row=5, column=1, padx=8, pady=5)

        # Buttons
        self.recommend_button = tk.Button(master, text="Get Recommendations", command=self.get_recommendations)
        self.recommend_button.grid(row=6, column=0, columnspan=2, pady=8)

        # Results Display with Scrollbar
        self.results_frame = tk.Frame(master)
        self.results_frame.grid(row=7, column=0, columnspan=2, pady=8)

        self.scrollbar = tk.Scrollbar(self.results_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results = tk.Text(self.results_frame, height=15, width=80, yscrollcommand=self.scrollbar.set)
        self.results.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.results.yview)

        # Clear Button 
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=8, column=1, pady=8, sticky="e", padx=8)

    def get_recommendations(self):
        # Get user input from dropdown menus
        cut = self.cut_var.get().strip()
        carat_min = self.carat_min_var.get()
        carat_max = self.carat_max_var.get()
        clarity = self.clarity_var.get().strip()
        cut_quality = self.cut_quality_var.get().strip()
        lab = self.lab_var.get().strip()

        # Validate selection
        if not cut or not carat_min or not carat_max or not clarity or not cut_quality or not lab:
            messagebox.showerror("Input Error", "Please select values for all fields.")
            return

        if carat_min > carat_max:
            messagebox.showerror("Input Error", "Carat Min cannot be greater than Carat Max.")
            return

        # Generate recommendations
        filtered = self.recommendation_system.filter_diamonds(
            cut=cut, carat_min=carat_min, carat_max=carat_max, clarity=clarity, cut_quality=cut_quality, lab=lab
        )
        self.results.delete(1.0, tk.END)  

        if filtered is not None and not filtered.empty:
            # Display the count of stones
            self.results.insert(tk.END, f"Total Stones: {len(filtered)}\n\n")
            self.results.insert(tk.END, filtered.to_string(index=False))
        else:
            self.results.insert(tk.END, "No diamonds match the given preferences.")

    def clear_fields(self):
        # Reset all dropdown menus and results
        self.cut_var.set("")
        self.carat_min_var.set("")
        self.carat_max_var.set("")
        self.clarity_var.set("")
        self.cut_quality_var.set("")
        self.lab_var.set("")
        self.results.delete(1.0, tk.END)


# Main Function
if __name__ == "__main__":
    FILE_PATH = "diamonds.csv"  
    recommendation_system = DiamondRecommendationSystem(FILE_PATH)  

    root = tk.Tk()
    gui = DiamondGUI(root, recommendation_system)  # Pass the instance to the GUI
    root.mainloop()

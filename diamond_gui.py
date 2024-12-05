import pandas as pd
import tkinter as tk
from tkinter import messagebox

class DiamondRecommendationSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        print("Dataset loaded successfully with", len(self.df), "rows.")

    def filter_diamonds(self, cut, carat, clarity):
        # Apply filtering logic
        filtered = self.df[(self.df['cut'].str.lower() == cut.lower()) &
                           (self.df['carat'] == carat) &
                           (self.df['clarity'].str.lower() == clarity.lower())]
        # Select only relevant columns to display
        return filtered[["cut", "carat", "clarity", "total_sales_price"]]

    def validate_cut(self, cut):
        return cut.isalpha()

    def validate_carat(self, carat):
        try:
            float(carat)
            return True
        except ValueError:
            return False

    def validate_clarity(self, clarity):
        return clarity.isalnum()

class DiamondGUI:
    def __init__(self, master, recommendation_system):
        self.master = master
        self.recommendation_system = recommendation_system

        master.title("Diamond Recommendation System")

        # Input Labels and Entry Fields
        tk.Label(master, text="Cut:").grid(row=0, column=0, padx=8, pady=5)
        self.cut_entry = tk.Entry(master)
        self.cut_entry.grid(row=0, column=1, padx=8, pady=5)

        tk.Label(master, text="Carat:").grid(row=1, column=0, padx=8, pady=5)
        self.carat_entry = tk.Entry(master)
        self.carat_entry.grid(row=1, column=1, padx=8, pady=5)

        tk.Label(master, text="Clarity:").grid(row=2, column=0, padx=8, pady=5)
        self.clarity_entry = tk.Entry(master)
        self.clarity_entry.grid(row=2, column=1, padx=8, pady=5)

        # Buttons
        self.recommend_button = tk.Button(master, text="Get Recommendations", command=self.get_recommendations)
        self.recommend_button.grid(row=3, column=0, columnspan=2, pady=8)

        # Results Display with Scrollbar
        self.results_frame = tk.Frame(master)
        self.results_frame.grid(row=4, column=0, columnspan=2, pady=8)

        self.scrollbar = tk.Scrollbar(self.results_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results = tk.Text(self.results_frame, height=15, width=50, yscrollcommand=self.scrollbar.set)
        self.results.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.results.yview)

        # Clear Button (placed after results, aligned right)
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=1, pady=8, sticky="e", padx=8)


        # Bind "Enter" key to navigate to the next entry field
        self.cut_entry.bind("<Return>", lambda event: self.carat_entry.focus())
        self.carat_entry.bind("<Return>", lambda event: self.clarity_entry.focus())
        self.clarity_entry.bind("<Return>", lambda event: self.get_recommendations())

        # Bind "Enter" key to click the recommend button after entering in the last field
        self.clarity_entry.bind("<Return>", lambda event: self.get_recommendations())

    def get_recommendations(self):
        # Get user input
        cut = self.cut_entry.get().strip()
        carat = self.carat_entry.get().strip()
        clarity = self.clarity_entry.get().strip()

        # Validate user inputs only when submitting
        if not self.recommendation_system.validate_cut(cut):
            messagebox.showerror("Input Error", "Invalid cut type. Please enter alphabetic characters only.")
            return

        if not self.recommendation_system.validate_carat(carat):
            messagebox.showerror("Input Error", "Invalid carat. Please enter a numeric value.")
            return

        if not self.recommendation_system.validate_clarity(clarity):
            messagebox.showerror("Input Error", "Invalid clarity. Please use alphanumeric characters only.")
            return

        # Convert carat to float
        carat = float(carat)

        # Generate recommendations
        filtered = self.recommendation_system.filter_diamonds(cut=cut, carat=carat, clarity=clarity)
        self.results.delete(1.0, tk.END)  # Clear previous results
        if filtered is not None and not filtered.empty:
            self.results.insert(tk.END, filtered.to_string(index=False))
        else:
            self.results.insert(tk.END, "No diamonds match the given preferences.")

    def clear_fields(self):
        # Reset all fields to their default state
        self.cut_entry.delete(0, tk.END)
        self.carat_entry.delete(0, tk.END)
        self.clarity_entry.delete(0, tk.END)
        self.results.delete(1.0, tk.END)

# Main Function
if __name__ == "__main__":
    FILE_PATH = "diamonds_updated.csv"  # Update this to your dataset's file path
    recommendation_system = DiamondRecommendationSystem(FILE_PATH)  # Create an instance

    root = tk.Tk()
    gui = DiamondGUI(root, recommendation_system)  # Pass the instance to the GUI
    root.mainloop()

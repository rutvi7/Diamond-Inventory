import pandas as pd
import tkinter as tk
from tkinter import messagebox

class DiamondQualityRecommendationSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
            print("Dataset loaded successfully with", len(self.df), "rows.")
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
            self.df = None

    def filter_diamonds(self, color, polish, clarity):
        if self.df is None:
            return None

        # Apply filtering logic
        filtered = self.df[(self.df['color'].str.lower() == color.lower()) &
                           (self.df['polish'].str.lower() == polish.lower()) &
                           (self.df['clarity'].str.lower() == clarity.lower())]

        return filtered[["color", "polish", "clarity", "total_sales_price"]]

    def validate_color(self, color):
        return color.isalpha()

    def validate_polish(self, polish):
        return polish.isalpha()

    def validate_clarity(self, clarity):
        return clarity.isalnum()

class DiamondQualityGUI:
    def __init__(self, master, recommendation_system):
        self.master = master
        self.recommendation_system = recommendation_system

        master.title("Diamond Quality Recommendation System")

        # Input Labels and Entry Fields
        tk.Label(master, text="Color:").grid(row=0, column=0, padx=8, pady=5)
        self.color_entry = tk.Entry(master)
        self.color_entry.grid(row=0, column=1, padx=8, pady=5)

        tk.Label(master, text="Polish:").grid(row=1, column=0, padx=8, pady=5)
        self.polish_entry = tk.Entry(master)
        self.polish_entry.grid(row=1, column=1, padx=8, pady=5)

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

        # Clear Button
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=1, pady=8, sticky="e", padx=8)

        # "Enter" key for navigation and submission
        self.color_entry.bind("<Return>", lambda event: self.polish_entry.focus())
        self.polish_entry.bind("<Return>", lambda event: self.clarity_entry.focus())
        self.clarity_entry.bind("<Return>", lambda event: self.get_recommendations())

    def get_recommendations(self):
        # User input
        color = self.color_entry.get().strip()
        polish = self.polish_entry.get().strip()
        clarity = self.clarity_entry.get().strip()

        # Validate user inputs
        if not self.recommendation_system.validate_color(color):
            messagebox.showerror("Input Error", "Invalid color. Please enter alphabetic characters only.")
            return

        if not self.recommendation_system.validate_polish(polish):
            messagebox.showerror("Input Error", "Invalid polish. Please enter alphabetic characters only.")
            return

        if not self.recommendation_system.validate_clarity(clarity):
            messagebox.showerror("Input Error", "Invalid clarity. Please use alphanumeric characters only.")
            return

        # Generate recommendations
        filtered = self.recommendation_system.filter_diamonds(color=color, polish=polish, clarity=clarity)
        self.results.delete(1.0, tk.END)  # Clear previous results
        if filtered is not None and not filtered.empty:
            self.results.insert(tk.END, filtered.to_string(index=False))
        else:
            self.results.insert(tk.END, "No diamonds match the given preferences.")

    def clear_fields(self):
        # Reset all fields 
        self.color_entry.delete(0, tk.END)
        self.polish_entry.delete(0, tk.END)
        self.clarity_entry.delete(0, tk.END)
        self.results.delete(1.0, tk.END)

# Main Function
if __name__ == "__main__":
    FILE_PATH = "diamonds_updated.csv"  
    recommendation_system = DiamondQualityRecommendationSystem(FILE_PATH)  
    root = tk.Tk()
    gui = DiamondQualityGUI(root, recommendation_system)  # Pass the instance to the GUI
    root.mainloop()

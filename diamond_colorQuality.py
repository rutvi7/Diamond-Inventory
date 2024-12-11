import pandas as pd
import re  # Regular expression module for validation


class DiamondRecommendationSystem:
    def __init__(self, file_path):
        """
        Initialize the system with the diamonds dataset.
        """
        try:
            self.df = pd.read_csv(file_path)
            print(f"Dataset loaded successfully with {len(self.df)} rows.")
        except FileNotFoundError:
            print("Error: The file was not found. Please check the file path.")
            self.df = None

    def filter_diamonds(self, color=None, polish=None, clarity=None):
        """
        Filter diamonds based on user preferences: color, polish, and clarity.
        """
        if self.df is None:
            print("Dataset not loaded. Cannot perform filtering.")
            return None

        filtered_df = self.df.copy()

        # Filter by color
        if color:
            if 'color' in self.df.columns:
                filtered_df = filtered_df[filtered_df['color'].str.lower() == color.lower()]
            else:
                print("Error: 'color' column not found in the dataset.")
                return None

        # Filter by polish
        if polish:
            if 'polish' in self.df.columns:
                filtered_df = filtered_df[filtered_df['polish'].str.lower() == polish.lower()]
            else:
                print("Error: 'polish' column not found in the dataset.")
                return None

        # Filter by clarity
        if clarity:
            if 'clarity' in self.df.columns:
                filtered_df = filtered_df[filtered_df['clarity'].str.lower() == clarity.lower()]
            else:
                print("Error: 'clarity' column not found in the dataset.")
                return None

        if filtered_df.empty:
            print("No diamonds match the given preferences. Please refine your criteria.")
            return None

        return filtered_df

    def recommend(self, color=None, polish=None, clarity=None):
        """
        Provide diamond recommendations based on user preferences.
        Display all matching diamonds, not just the top 5.
        """
        print("\n--- User Preference-Based Recommendations ---")
        filtered = self.filter_diamonds(color=color, polish=polish, clarity=clarity)
        if filtered is not None and not filtered.empty:
            print(filtered[['color', 'polish', 'clarity']])
        else:
            print("No diamonds to recommend based on the given preferences.")

    def validate_color(self, color):
        """
        Validate that the color input contains only alphabetic characters and spaces.
        """
        return color.isalpha()

    def validate_polish(self, polish):
        """
        Validate that polish input contains only alphabetic characters (no numbers or special characters).
        """
        return polish.isalpha()

    def validate_clarity(self, clarity):
        """
        Validate that the clarity input contains only letters and numbers (no special characters).
        """
        return bool(re.match("^[A-Za-z0-9]+$", clarity))  # Only letters and numbers allowed

    def recommend_top_selling(self, top_n=5):
        """
        Recommend the top-selling diamonds based on sales count or popularity.
        """
        if 'total_sales_price' in self.df.columns:
            top_selling_df = self.df.sort_values(by='total_sales_price', ascending=False).head(top_n)
            print("\n--- Top-Selling Diamonds ---")
            print(top_selling_df[['color', 'polish', 'clarity', 'total_sales_price']])
        else:
            print("Error: 'total_sales_price' column not found for top-selling recommendation.")

FILE_PATH = "diamonds_updated.csv"
recommendation_system = DiamondRecommendationSystem(FILE_PATH)

print("\nWelcome to the Diamond Recommendation System!")

# Step 1: Ask for color type
color = input("Enter the desired color type (e.g., 'D', 'E', 'G'): ").strip()

# Validate the color type
while not recommendation_system.validate_color(color):
    print("Error: Invalid color type. Please enter only alphabetic characters (no special characters or numbers).")
    color = input("Enter the desired color type (e.g., 'D', 'E', 'G'): ").strip()

# Step 2: Ask for polish
polish = input("Enter the desired polish (e.g., Good, Very Good, Excellent): ").strip()

# Validate polish input
while not recommendation_system.validate_polish(polish):
    print("Error: Invalid input for polish. Please enter alphabetic characters (no numbers or special characters).")
    polish = input("Enter the desired polish (e.g., Good, Very Good, Excellent): ").strip()

# Step 3: Ask for clarity
clarity = input("Enter the desired clarity (e.g., 'VS1', 'VS2', 'SI1'): ").strip()

# Validate clarity input
while not recommendation_system.validate_clarity(clarity):
    print("Error: Invalid clarity input. Please enter letters and numbers only (no special characters).")
    clarity = input("Enter the desired clarity (e.g., 'VS1', 'VS2', 'SI1'): ").strip()

recommendation_system.recommend(color=color, polish=polish, clarity=clarity)

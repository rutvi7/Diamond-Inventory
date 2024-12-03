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

    def filter_diamonds(self, cut=None, carat=None, clarity=None):
        """
        Filter diamonds based on user preferences: cut, carat, and clarity.
        """
        if self.df is None:
            print("Dataset not loaded. Cannot perform filtering.")
            return None

        filtered_df = self.df.copy()

        # Filter by cut
        if cut:
            if 'cut' in self.df.columns:
                filtered_df = filtered_df[filtered_df['cut'].str.lower() == cut.lower()]
            else:
                print("Error: 'cut' column not found in the dataset.")
                return None

        # Filter by carat
        if carat:
            if 'carat' in self.df.columns:
                filtered_df = filtered_df[filtered_df['carat'] == carat]
            else:
                print("Error: 'carat' column not found in the dataset.")
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

    def recommend(self, cut=None, carat=None, clarity=None):
        """
        Provide diamond recommendations based on user preferences.
        Display all matching diamonds, not just the top 5.
        """
        print("\n--- User Preference-Based Recommendations ---")
        filtered = self.filter_diamonds(cut=cut, carat=carat, clarity=clarity)
        if filtered is not None and not filtered.empty:
            print(filtered[['cut', 'carat', 'clarity']])
        else:
            print("No diamonds to recommend based on the given preferences.")

    def validate_cut(self, cut):
        """
        Validate that the cut input contains only alphabetic characters and spaces.
        """
        if not cut.isalpha() or any(char in cut for char in "!@#$%^&*()_+=-1234567890"):
            return False
        return True

    def validate_carat(self, carat):
        """
        Validate that carat is a numeric value.
        """
        try:
            float(carat)
            return True
        except ValueError:
            return False

    def validate_clarity(self, clarity):
        """
        Validate that the clarity input contains only letters and numbers (no special characters).
        """
        if re.match("^[A-Za-z0-9]+$", clarity):  # Only letters and numbers allowed
            return True
        return False
    
    def recommend_top_selling(self, top_n=5):
        """
        Recommend the top-selling diamonds based on sales count or popularity.
        """
        if 'satotal_sales_price' in self.df.columns:
            top_selling_df = self.df.sort_values(by='total_sales_price', ascending=False).head(top_n)
            print("\n--- Top-Selling Diamonds ---")
            print(top_selling_df[['cut', 'carat', 'clarity', 'satotal_sales_price']])
        else:
            print("Error: 'total_sales_price' column not found for top-selling recommendation.")



# Example usage
FILE_PATH = "diamonds_updated.csv"
recommendation_system = DiamondRecommendationSystem(FILE_PATH)

# Ask for user input for cut, carat, and clarity
print("\nWelcome to the Diamond Recommendation System!")

# Step 1: Ask for Cut type
cut = input("Enter the desired cut type (e.g., 'Round', 'Oval', 'Emerald'): ").strip()

# Validate the cut type
while not recommendation_system.validate_cut(cut):
    print("Error: Invalid cut type. Please enter only alphabetic characters (no special characters or numbers).")
    cut = input("Enter the desired cut type (e.g., 'Round', 'Oval', 'Emerald'): ").strip()

# Step 2: Ask for Carat
carat = input("Enter the desired carat (e.g., 1.0, 1.5, 2.0): ").strip()

# Validate carat input
while not recommendation_system.validate_carat(carat):
    print("Error: Invalid input for carat. Please enter a numeric value.")
    carat = input("Enter the desired carat (e.g., 1.0, 1.5, 2.0): ").strip()

carat = float(carat)

# Step 3: Ask for Clarity
clarity = input("Enter the desired clarity (e.g., 'VS1', 'VS2', 'SI1'): ").strip()

# Validate clarity input
while not recommendation_system.validate_clarity(clarity):
    print("Error: Invalid clarity input. Please enter letters and numbers only (no special characters).")
    clarity = input("Enter the desired clarity (e.g., 'VS1', 'VS2', 'SI1'): ").strip()

# Step 4: Generate recommendations based on user input
recommendation_system.recommend(cut=cut, carat=carat, clarity=clarity)

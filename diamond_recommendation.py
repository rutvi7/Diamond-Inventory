import pandas as pd
import os  

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

    def filter_diamonds(self, cut=None, carat_weight=None, clarity=None):
        """
        Filter diamonds based on user preferences: cut, carat_weight, and clarity.
        """
        if self.df is None:
            print("Dataset not loaded. Cannot perform filtering.")
            return pd.DataFrame()  # Return an empty DataFrame

        filtered_df = self.df.copy()

        # Filter by cut
        if cut:
            if 'cut' in self.df.columns:
                filtered_df = filtered_df[filtered_df['cut'].str.lower() == cut.lower()]
            else:
                print("Error: 'cut' column not found in the dataset.")
                return pd.DataFrame()  # Return an empty DataFrame

        # Filter by carat_weight
        if carat_weight:
            if 'carat_weight' in self.df.columns:
                filtered_df = filtered_df[filtered_df['carat_weight'] == carat_weight]
            else:
                print("Error: 'carat_weight' column not found in the dataset.")
                return pd.DataFrame()  # Return an empty DataFrame

        # Filter by clarity
        if clarity:
            if 'clarity' in self.df.columns:
                filtered_df = filtered_df[filtered_df['clarity'].str.lower() == clarity.lower()]
            else:
                print("Error: 'clarity' column not found in the dataset.")
                return pd.DataFrame()  # Return an empty DataFrame

        if filtered_df.empty:
            print("No diamonds match the given preferences. Please refine your criteria.")
            return pd.DataFrame()  # Return an empty DataFrame

        return filtered_df

    def recommend(self, cut=None, carat_weight=None, clarity=None):
        """
        Display all matching diamonds.
        """
        print("\n--- User Preference-Based Recommendations ---")
        filtered = self.filter_diamonds(cut=cut, carat_weight=carat_weight, clarity=clarity)
        if filtered is not None and not filtered.empty:
            print(filtered[['cut', 'carat_weight', 'clarity']])
        else:
            print("No diamonds match the given preferences.")

    def validate_cut(self, cut):
        """
        Validate that the cut input contains only alphabetic characters and spaces.
        """
        return cut.isalpha()

    def validate_carat(self, carat_weight):
        """
        Validate that carat_weight is a numeric value.
        """
        try:
            float(carat_weight)
            return True
        except ValueError:
            return False

    def validate_clarity(self, clarity):
        """
        Validate that the clarity input contains only letters and numbers (no special characters).
        """
        return clarity.isalnum()


if __name__ == "__main__" and "PYTEST_CURRENT_TEST" not in os.environ:
    # Only execute when not testing
    cut = input("Enter the desired cut type (e.g., 'Round', 'Oval', 'Emerald'): ").strip()
    carat_weight = float(input("Enter the desired carat weight (e.g., 1.0, 1.5): ").strip())
    clarity = input("Enter the desired clarity (e.g., 'VS1', 'VS2', 'SI1'): ").strip()

    recommendation_system = DiamondRecommendationSystem("diamonds.csv")
    recommendation_system.recommend(cut=cut, carat_weight=carat_weight, clarity=clarity)

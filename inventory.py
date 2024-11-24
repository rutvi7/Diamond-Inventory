import pandas as pd

class Inventory:
    def __init__(self, file_path='diamonds.csv'):
        self.file_path = file_path
        self.data = pd.read_csv(file_path) if self._file_exists() else pd.DataFrame(columns=['ID', 'Type', 'Carat', 'Price', 'Stock'])

    def _file_exists(self):
        try:
            with open(self.file_path, 'r'):
                return True
        except FileNotFoundError:
            return False

    def add_item(self, item):
        self.data = pd.concat([self.data, pd.DataFrame([item])], ignore_index=True)
        self.save_data()

    def remove_item(self, item_id):
        self.data = self.data[self.data['ID'] != item_id]
        self.save_data()

    def update_stock(self, item_id, new_stock):
        self.data.loc[self.data['ID'] == item_id, 'Stock'] = new_stock
        self.save_data()

    def save_data(self):
        self.data.to_csv(self.file_path, index=False)

    def get_inventory(self):
        return self.data

    def get_low_stock_items(self, threshold=5):
        return self.data[self.data['Stock'] < threshold]

    def get_high_stock_items(self, threshold=50):
        return self.data[self.data['Stock'] > threshold]

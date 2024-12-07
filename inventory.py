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
        print("Item added successfully!")

    def remove_item(self, item_id):
        if item_id in self.data['ID'].values:
            self.data = self.data[self.data['ID'] != item_id]
            self.save_data()
            print(f"Item with ID {item_id} removed successfully!")
        else:
            print(f"No item found with ID {item_id}.")

    def update_stock(self, item_id, new_stock):
        if item_id in self.data['ID'].values:
            self.data.loc[self.data['ID'] == item_id, 'Stock'] = new_stock
            self.save_data()
            print(f"Stock for item {item_id} updated successfully!")
        else:
            print(f"No item found with ID {item_id}.")

    def save_data(self):
        self.data.to_csv(self.file_path, index=False)

    def get_inventory(self):
        return self.data

    def display_inventory(self):
        if self.data.empty:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            print(self.data)

# User Interaction Function
def inventory_interaction():
    inv = Inventory()
    while True:
        print("\nInventory Management Menu:")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Stock")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            inv.display_inventory()
        elif choice == "2":
            item = {
                "ID": input("Enter item ID: ").strip(),
                "Type": input("Enter item Type: ").strip(),
                "Carat": float(input("Enter item Carat: ").strip()),
                "Price": float(input("Enter item Price: ").strip()),
                "Stock": int(input("Enter item Stock: ").strip()),
            }
            inv.add_item(item)
        elif choice == "3":
            item_id = input("Enter the ID of the item to remove: ").strip()
            inv.remove_item(item_id)
        elif choice == "4":
            item_id = input("Enter the ID of the item to update: ").strip()
            new_stock = int(input("Enter the new stock value: ").strip())
            inv.update_stock(item_id, new_stock)
        elif choice == "5":
            print("Exiting Inventory Management. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the user interaction function
if __name__ == "__main__":
    inventory_interaction()

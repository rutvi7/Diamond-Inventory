import pytest
import pandas as pd
from inventory import Inventory

# Load the diamonds.csv file
DIAMONDS_CSV_PATH = 'diamonds.csv'

@pytest.fixture
def inventory():
    # Initialize Inventory with diamonds.csv
    return Inventory(file_path=DIAMONDS_CSV_PATH)

def test_add_item(inventory):
    initial_count = len(inventory.get_inventory())
    inventory.add_item({'ID': 'D1001', 'Type': 'Emerald', 'Carat': 1.5, 'Price': 15000, 'Stock': 20})
    assert len(inventory.get_inventory()) == initial_count + 1

def test_remove_item(inventory):
    inventory.add_item({'ID': 'D1002', 'Type': 'Heart', 'Carat': 2.0, 'Price': 20000, 'Stock': 5})
    initial_count = len(inventory.get_inventory())
    inventory.remove_item('D1002')
    assert len(inventory.get_inventory()) == initial_count - 1

def test_update_stock(inventory):
    inventory.add_item({'ID': 'D1003', 'Type': 'Round', 'Carat': 0.8, 'Price': 4000, 'Stock': 10})
    inventory.update_stock('D1003', 25)
    updated_stock = inventory.get_inventory().loc[inventory.get_inventory()['ID'] == 'D1003', 'Stock'].iloc[0]
    assert updated_stock == 25

def test_low_stock_items(inventory):
    # Filter low-stock items (threshold: 5)
    low_stock_items = inventory.get_low_stock_items(threshold=5)
    # Ensure that all returned items have stock < 5
    assert all(low_stock_items['Stock'] < 5)

def test_high_stock_items(inventory):
    # Filter high-stock items (threshold: 50)
    high_stock_items = inventory.get_high_stock_items(threshold=50)
    # Ensure that all returned items have stock > 50
    assert all(high_stock_items['Stock'] > 50)

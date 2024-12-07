# **Diamond Inventory Management System**

This project is a comprehensive **Diamond Inventory Management System** designed to manage diamond stock efficiently. It includes functionalities for inventory management, diamond recommendations, and stock analysis.

---

## **GitHub Repository**
[Diamond Inventory Management System](https://github.com/rutvi7/Diamond-Inventory.git)


---

## **Understanding the Data**

The project revolves around managing an inventory of diamonds. Here’s a detailed explanation of the dataset used (`diamonds.csv`) to ensure that anyone can understand it:

### **Dataset Columns**
1. **stock-id**:
   - A unique identifier for each diamond item in the inventory.
   - Example: `6890889890`.

2. **Type**:
   - Refers to the shape or cut of the diamond, which determines its appearance.
   - Common Types:
     - **Round**: A classic and popular diamond shape.
     - **Oval**: An elongated round shape.
     - **Princess**: A square shape with sharp edges.
     - **Emerald**: A rectangular shape with step cuts.

3. **Carat**:
   - The weight of the diamond, measured in carats.
   - Heavier diamonds (higher carats) are usually more expensive.
   - Example:
     - `1.0`: A diamond weighing 1 carat.
     - `0.5`: A diamond weighing 0.5 carats.

4. **Price**:
   - The cost of the diamond, usually in USD or another currency.
   

5. **Stock**:
   - The quantity of a specific diamond type available in the inventory.
   - Example:
     - `10`: 10 diamonds of this type are available.
     - `0`: No diamonds of this type are left in stock.

---

## **Project Files and Details**

### **1. `inventory.py`**
- **Purpose**: Core file for managing the diamond inventory.
- **Features**:
  - **Display Inventory**: Prints all items in the inventory.
  - **Add Item**: Adds a new diamond item to the inventory.
  - **Remove Item**: Deletes an item based on its unique ID.
  - **Update Stock**: Updates the stock levels for an item.
- **Returns**:
  - Displays or updates inventory data as requested.
  - Saves all changes to the `diamonds.csv` file.

---

### **2. `diamonds.csv`**
- **Purpose**: Stores inventory data.
- **Returns**:
  - Provides input data for the `inventory.py` and other scripts.
  - Automatically updated by `inventory.py` when changes are made.

---

### **3. `diamond_recommendation.py`**
- **Purpose**: Filters and recommends diamonds based on user-defined preferences.
- **Features**:
  - Filter diamonds by:
    - **Cut** (e.g., `Round`, `Oval`).
    - **Carat Weight** (e.g., 1.0, 1.5).
    - **Clarity** (e.g., `VS1`, `SI2`).
  - Displays matching diamonds based on the given criteria.
- **Returns**:
  - A list of diamonds matching the filters.
  - If no matches are found, it returns a message: `No diamonds match the given preferences.`

---

### **4. `test_recommendation.py`**
- **Purpose**: Tests the functionalities of `diamond_recommendation.py`.
- **Tests**:
  - Filtering diamonds by attributes.
  - Validation of user inputs for attributes like cut, carat, and clarity.
- **Returns**:
  - `PASSED` or `FAILED` for each test case to verify the system’s functionality.

---

### **5. `smart_restocking.py`**
- **Purpose**: Analyzes stock and sales data to identify low-stock items.
- **Features**:
  - Merges inventory and sales data.
  - Flags items with stock below a defined threshold.
- **Returns**:
  - Generates a file `inventory_status.csv` with the following columns:
    - **Cut**: Cut type of the diamond.
    - **Clarity**: Clarity of the diamond.
    - **Stock Quantity**: Current stock levels.
    - **Sold Quantity**: Quantity sold.
    - **Remaining Stock**: Remaining stock levels.
    - **Low Stock**: Indicates whether the item is low on stock (`True`/`False`).

---

### **6. `test_inventory.py`**
- **Purpose**: Tests the functionalities of `inventory.py`.
- **Tests**:
  - Adding a new item to the inventory.
  - Removing an item by its unique ID.
  - Updating the stock levels of an existing item.
- **Returns**:
  - `PASSED` or `FAILED` for each test case to verify the system’s functionality.
    
---

### **7. `analytics.py`**
- **Purpose**: Generates analytics and visualizations for the inventory.
- **Features**:
  - Creates graphs and charts to analyze:
    - Diamond availability by cut type.
    - Stock distribution by carat weight and clarity.
  - Helps in understanding inventory trends visually.
- **Returns**:
  - Displays charts using `matplotlib` or saves them as image files.

---

### **8. `diamond_gui.py`**
- **Purpose**: Provides a graphical user interface (GUI) for the Diamond Recommendation System.
- **Features**:
  - Allows users to select:
    - Cut type (e.g., `Round`, `Oval`).
    - Carat weight range.
    - Clarity level.
  - Displays matching diamonds in a user-friendly GUI window.
- **Returns**:
  - A list of matching diamonds displayed in the GUI.
  - An error message if no matches are found.

---

### **9. `manager.py`**
- **Purpose**: Provides tools for manager-level access to the inventory system.
- Login Details: For Manager.py file
  - username : rutvi and password : R123@
  - username : Jeevna and password : J123@
- **Features**:
  - Adjust pricing of diamonds based on market trends.
  - Log and track changes made to the inventory.
- **Returns**:
  - Saves logs of changes made to pricing or stock in a separate file.
  - Updates the `diamonds.csv` file with new prices.

---

### **10. `order.py`**
- **Purpose**: Manages customer orders and integrates them with the inventory system.
- **Features**:
  - GUI for placing customer orders.
  - Automatically updates stock levels when an order is placed.
  - Saves order details in `order_details.csv`.
- **Returns**:
  - Updates the inventory.
  - Logs all orders in `order_details.csv` with the following columns:
    - **Order ID**: Unique identifier for the order.
    - **Diamond ID**: ID of the diamond being ordered.
    - **Quantity**: Number of items ordered.
    - **Total Price**: Total cost of the order.

---

### **. `11README.md`**
- **Purpose**: Provides documentation for understanding the project files, their purpose, and how they work.

---

## **Project Structure**

| File/Folder          | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `inventory.py`       | Core script for managing inventory with options to add, remove, update, and view items. |
| `diamonds.csv`       | Dataset containing initial diamond inventory data.                         |
| `diamond_recommendation.py` | Core logic for filtering and recommending diamonds based on user preferences. |
| `analytics.py`       | Generates visual analytics for inventory trends and stock distribution.    |
| `diamond_gui.py`     | GUI for user-friendly diamond recommendation system.                       |
| `manager.py`         | Manager-level tools for adjusting pricing and logging changes.             |
| `order.py`           | GUI for placing customer orders and updating inventory.                   |
| `smart_restocking.py`| Analyzes inventory and sales data to flag low-stock items.                 |
| `test_recommendation.py` | Unit tests for diamond recommendation functionality.                   |
| `test_inventory.py`  | Unit tests for inventory management functionality.                        |
| `README.md`          | Documentation for understanding and running the project.                  |

---

## **Contributors**

| Contributor Name                |
|---------------------------------|
| **Rutvi Kishorbhai Sutariya**   | 
| **Jeevana Dova**   		  |

---

## **License**

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project for educational or commercial purposes, provided proper credit is given to the contributors.

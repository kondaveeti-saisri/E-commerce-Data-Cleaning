#  E-commerce Data Cleaning (User Input Version)

##  Overview
This project cleans duplicate product IDs entered by the user.  
It simulates cleaning duplicate records from supplier data in an e-commerce system.



##  How It Works
1. The user enters product IDs separated by commas.
2. The program removes duplicates and sorts them.
3. It displays both the original and cleaned product lists.



##  Example
**Input:**
1001,1001,1002,1003,1003


**Output:**

Original product IDs: [1001, 1001, 1002, 1003, 1003]
Cleaned product IDs: [1001, 1002, 1003]




##  Run Instructions
1. Open the folder in **VS Code**.
2. Run the script:
   ```bash
   python clean_data.py

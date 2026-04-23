import csv
import json

# reading csv file
input_file = "products_raw.csv"
output_file = "cleaned_products.json"

cleaned_data = []

with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # cleaning values
        product_id = row["Product ID"].strip()
        product_name = row["Product Name"].strip()
        category = row["Category"].strip()

        # handling missing price
        if row["Price"].strip() == "":
            price = 0
        else:
            price = int(row["Price"])

        # handling missing stock
        if row["Stock"].strip() == "":
            stock = 0
        else:
            stock = int(row["Stock"])

        # building cleaned row
        clean_row = {
            "product_id": product_id,
            "product_name": product_name,
            "category": category,
            "price": price,
            "stock": stock
        }

        cleaned_data.append(clean_row)

# writing to json
with open(output_file, "w") as file:
    json.dump(cleaned_data, file, indent=4)

print("task1 completed")

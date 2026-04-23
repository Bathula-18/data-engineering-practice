import os
import csv
import json
import logging
from pathlib import Path

# reading folder paths
DATA_FOLDER = "input"
OUTPUT_FOLDER = "output"
LOG_FOLDER = "logs"

# creating folders if not exist
Path(OUTPUT_FOLDER).mkdir(exist_ok=True)
Path(LOG_FOLDER).mkdir(exist_ok=True)

# setup logging
logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, "pipeline.log"),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# standard columns
EXPECTED_COLUMNS = ["product_id", "product_name", "category", "price"]

def read_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        headers = reader.fieldnames
    return headers, rows

def standardize_row(row, file_name):
    if file_name == "vendor1.csv":
        return {
            "product_id": row.get("Product ID", "").strip(),
            "product_name": row.get("Product Name", "").strip(),
            "category": row.get("Category", "").strip(),
            "price": row.get("Price", "").strip()
        }

    elif file_name == "vendor2.csv":
        return {
            "product_id": row.get("id", "").strip(),
            "product_name": row.get("name", "").strip(),
            "category": row.get("category", "").strip(),
            "price": row.get("price", "").strip()
        }

    elif file_name == "vendor3.csv":
        return {
            "product_id": row.get("item_code", "").strip(),
            "product_name": row.get("item_name", "").strip(),
            "category": row.get("item_group", "").strip(),
            "price": row.get("cost", "").strip()
        }

def clean_data(row, row_number, file_name):
    if row["product_name"] == "":
        logging.error(f"{file_name} row {row_number}: missing name")
        row["product_name"] = "Unknown"

    if row["category"] == "":
        logging.error(f"{file_name} row {row_number}: missing category")
        row["category"] = "Unknown"

    if row["price"] == "":
        logging.error(f"{file_name} row {row_number}: missing price")
        row["price"] = 0
    else:
        try:
            row["price"] = int(row["price"])
        except:
            logging.error(f"{file_name} row {row_number}: invalid price")
            row["price"] = 0

    return row

def remove_duplicates(data):
    unique = []
    seen = set()

    for row in data:
        if row["product_id"] in seen:
            logging.error(f"duplicate product {row['product_id']}")
            continue

        seen.add(row["product_id"])
        unique.append(row)

    return unique

def main():
    all_data = []

    files = ["vendor1.csv", "vendor2.csv", "vendor3.csv"]

    for file_name in files:
        file_path = os.path.join(DATA_FOLDER, file_name)

        headers, rows = read_data(file_path)

        for i, row in enumerate(rows, start=1):
            try:
                std_row = standardize_row(row, file_name)
                clean_row = clean_data(std_row, i, file_name)
                all_data.append(clean_row)
            except Exception as e:
                logging.error(f"{file_name} row {i} failed")
                continue

    final_data = remove_duplicates(all_data)

    output_path = os.path.join(OUTPUT_FOLDER, "final_cleaned_products.json")

    with open(output_path, "w") as f:
        json.dump(final_data, f, indent=4)

    print("pipeline completed")

if __name__ == "__main__":
    main()

import csv

# expected columns
EXPECTED_COLUMNS = ["product_id", "product_name", "category", "price", "stock"]

# function to validate schema
def validate_schema(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        actual_columns = reader.fieldnames
        rows = list(reader)

    # checking missing columns
    missing_columns = []
    for col in EXPECTED_COLUMNS:
        if col not in actual_columns:
            missing_columns.append(col)

    # printing result
    if len(missing_columns) == 0:
        print("schema is valid")
    else:
        print("missing columns:", missing_columns)

    print("total rows:", len(rows))


# calling function
validate_schema("products_schema_sample.csv")

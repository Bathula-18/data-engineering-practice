import csv
import logging

# setting up log file
logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

valid_rows = []

with open("customers_raw.csv", "r") as file:
    reader = csv.DictReader(file)

    for row_number, row in enumerate(reader, start=1):
        try:
            # checking missing name
            if row["name"].strip() == "":
                logging.error(f"Row {row_number}: missing name")
                continue

            # checking missing city
            if row["city"].strip() == "":
                logging.error(f"Row {row_number}: missing city")
                continue

            # checking invalid age
            age = int(row["age"])

            valid_rows.append({
                "customer_id": row["customer_id"].strip(),
                "name": row["name"].strip(),
                "age": age,
                "city": row["city"].strip()
            })

        except ValueError:
            logging.error(f"Row {row_number}: invalid age -> {row['age']}")
            continue

print("Valid rows processed:")
print(valid_rows)

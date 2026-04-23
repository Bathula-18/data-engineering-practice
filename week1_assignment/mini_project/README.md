# Week 1 Mini Project - Vendor CSV Ingestion

This mini project is my Week 1 end-to-end pipeline update based on the review feedback.

I used three vendor CSV files with different column names and combined them into one clean output.

## What this pipeline does
- reads multiple vendor csv files
- standardizes column names into one common format
- cleans missing or invalid values
- validates rows
- removes duplicates
- logs bad rows
- writes one final cleaned json output

## Final output
The final cleaned file is written to:
output/final_cleaned_products.json
